#Challenge `Money, money, money!` Writeup

- Vulnerability: 
  - SQLi attack
- Where:
  - Bio text field
- Impact:
  - allows users to manipulate tokens or jackpot values

## Analyzing the server

This challenges consists in getting enough tokens to achieve the jackpot.
The user profile can be editted, but only the Bio text field allows us to write something.
By typing `'` in the Bio and then pressing `Update profile` we get an error that shows the SQL statement being executed `UPDATE user SET bio = ''' WHERE username = 'teste1'`.

## Exploit

From the previous challenge, it's known that the table `user` has a `jackpot_val` column and since this is an `UPDATE` statement, it possible to set this parameter to any value.
Currently the user has zero tokens, so to hit the jackpot set the `jackpot_val` to zero.
Writing `',jackpot_val = '0` will create the statement `UPDATE user SET bio = '',jackpot_val='0' WHERE username = 'teste1'` that when executed show the flag hidden in the jackpot: `SSof{SQLi_can_also_happen_on_UPDATEs}`

## Implementation

No script needed.
