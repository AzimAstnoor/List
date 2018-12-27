import re
try:
    with open('q4', 'r') as f:
        q = f.read()
        regex = re.search("\w{2}[:]+[0-9]+[:]\w{2}",q)
        print(regex)
except Exception as e: print(e)