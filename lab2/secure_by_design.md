# Challenge `Secure by Design` Writeup

- Vulnerability: 
  - cookie forgery
- Where:
  - cookie
- Impact:
  - allows privilege access to the admin account

## Analyzing the server

This challenges consists in "logging in" as the admin user.
Upon entering a nickname, the server responds saying that the page is still under construction.
It also sets a 'user' cookie with a base64 encoded value (ends with `==`).

## Exploit

Since the cookie has a base64 encoded value, I started by decoding it and it matched the nickname submitted.
A fun fact is that entering `admin` would set your nickname to `fake-admin` and the cookie value would store the `fake-admin` encoded value.
Therefore, I sent a request with the cookie value equal to the base64 encoded value of `admin`.
```python
adminEnconded = base64.b64encode(b"admin").decode("utf-8")
r = requests.get(URL, cookies={'user': adminEnconded})
```

## Implementation

These code snippets and full implementation can be found [here](security_by_design.py).
