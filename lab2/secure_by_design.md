# Challenge `Secure by Design` Writeup

- Vulnerability: 
  - cookie forgery
- Where:
  - cookie
- Impact:
  - allows privilege access to the admin account

## Analyzing the server

This challenges consists in accessing the admin page.
Upon entering a nickname, the server responds with _"Unfortunately our page is still under construction for non-admin users."_
It also adds a cookie with a `user` key and a base64 encoded value (evident by the `==` at the end).
Decoding this value reveals that it's the nickname entered by the user.

## Exploit

A logical step is to try to enter with the admin nickname.
However, the server prevents this by changing it to `fake-admin`. It's even possible to verify this by decoding the `user` key value and checking that it's the same whether the nickname is `admin` or `fake-admin`.
To bypass this send a request with the cookie value forged equal to the base64 encoded value of `admin`.
```python
adminEncoded = base64.b64encode(b"admin").decode("utf-8")
r = requests.get(URL, cookies={'user': adminEnded})
```
Then the flag is displayed `SSof{Base64_encoding_is_not_the_solution}`.

## Implementation

These code snippets and full implementation can be found [here](security_by_design.py).
