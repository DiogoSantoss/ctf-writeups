# Challenge `Just my boring cookies` Writeup

- Vulnerability: 
  - XSS attack
- Where:
  - Search bar for blog posts
- Impact:
  - allows to inject JavaScript code that will be reflected in client browser

## Analyzing the server

This challenges consists in grabbing the user's own cookie.
By searching for `<script>alert(1)</script>` in the search bar, the browser will display an alert, which
reveals that the website is vulnerable to XSS attacks.

## Exploit

Since cookies are stored in the variable `document.cookie`, we can inject JavaScript code that will read the cookies and display them on the screen.
Search for `<script>alert(document.cookie)</script>` and the flag will be displayed `SSof{YOU_DO_NOT_HAVE_SECRETS}`.
Alternatively, type the link directly in the browser's search bar `http://mustard.stt.rnl.tecnico.ulisboa.pt:22251/?search=<script>alert(document.cookie)</script>`.

## Implementation

No script needed.