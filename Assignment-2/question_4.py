import re

lst = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie"]
pattern = "yourregularexpression bad cookie here"

print(len(re.findall(pattern, ", ".join(lst))) )
