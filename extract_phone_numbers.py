
import re

def extract(s):
    maxlen = len(s) - 1
    i = 0
    while i <= maxlen:
        if s[i].isdigit():
            extract = re.findall(r'(\d{3})\D+(\d{3})\D+(\d{4})',s[i:i+15])
            #extract = re.search(r'.*(\d{3}).*(\d{3}).*(\d{4}).*',s[i:i+15])
            if not extract:
                print extract
        i += 1
        


s = "Tanvir's number is 103-245-5678 and his's other is (123)-456-7890 and (123) 456-8789"
extract(s)
