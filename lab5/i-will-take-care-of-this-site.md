# Challenge `I will take care of this site` Writeup

- Vulnerability: 
  - SQLi attack
- Where:
  - Password text field
- Impact:
  - allows non-admin users to access the admin account

## Analyzing the server

This challenges consists in viewing the admin's account information by logging in with his account.  
The website as a Login page with a username and password input fields.
Trying to inject SQL code in the password field reveals a SQLi vulnerability.

## Exploit

First start by intensionally generate an error to analyze what query is being made to verify the login information.
Typing `admin` in the username and `'` in password will display the error `SELECT id, username, password, bio, age, jackpot_val FROM user WHERE username = 'admin' AND password = '''`.
This SQL statements is exploitable since we can comment out the verification of the password by inserting the username `admin'; --` and a random password.
The resulting query will be `SELECT id, username, password, bio, age, jackpot_val FROM user WHERE username = 'admin'`, granting access to the admin account.  
This reveals the flag `SSof{You_are_granted_super_powers_by_a_SQLi_on_SELECT}`

## Implementation

No script needed.
