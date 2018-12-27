import re
try:
    a = " 800-555-1212  555-1212 (800)555-1212 45758 saurabh sin-544"
    regex = re.findall("[^A-Za-z0-9]\w{0,3}[^A-Za-z0-9]\w{3}-\w{4}", a)
    print(regex)

except Exception as e: print(e)