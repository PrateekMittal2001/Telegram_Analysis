import re

string = """https://skillclsa.com hello world https://youtube.com"""

data = re.compile('(?:(?:https?|ftp):\/\/)[\w/\-?=%.]+\.[\w/\-&?=%.]+')
new = data.findall(string)

print(new)
