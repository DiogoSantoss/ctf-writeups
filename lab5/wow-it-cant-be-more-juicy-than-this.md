#Challenge `Wow, it can't be more juicy than this!` Writeup

- Vulnerability: 
  - SQLi attack
- Where:
  - Search blog posts text field
- Impact:
  - allows users to find a secret blog post

## Analyzing the server

This challenges consists in finding a secret blog post yet to be released.
By typing `%'` in the search text field an error is displayed revealing the SQL statement being executed `SELECT id, title, content FROM blog_post WHERE title LIKE '%%'%' OR content LIKE '%%'%'`.

## Exploit

By testing some queries we can conclude that the table `blog_post` only contains 4 posts so the secret blog post is not on this table.
Using the `sqlite_master` table we can find the name of all tables in the database by typing `' UNION ALL SELECT name, tbl_name, sql FROM 'sqlite_master'; --`. Note that the `UNION ALL SELECT` statement must have the same number of columns as the original query.
The output of this query reveals the existence of a table named `secret_blog_post` with the fields `id INTEGER NOT NULL, title TEXT, content TEXT, PRIMARY KEY (id), UNIQUE (title)`.
To reveal the content of this table its possible to use the same `UNION ALL SELECT` statement as before `' UNION ALL SELECT id, title, content FROM 'secret_blog_post'; --`.
The blog post `Reminder` appears and the content has the flag `SSof{All_tables_are_vulnerable_with_UNION_constructor}`.

## Implementation

No script needed.
