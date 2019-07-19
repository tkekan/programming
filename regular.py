import re

#Replace all white-space characters with the digit "9":

str = "The rain in Spain"
x = re.sub('(\W+)', "9", str)

regex = "([a-zA-Z]+) \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12")
for m in matches:
    print m
