import re

text = "you are beautiful very "

pattern = r"you"

match = re.match(pattern,text)

if match:
    print("match found:", match.group())
else:
    print("match not found")