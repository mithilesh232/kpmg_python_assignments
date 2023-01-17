import re
matcher=re.finditer("a?","abbaaaaab")
for match in matcher:
    print(match.start(),"....",match.group())
m=re.fullmatch("sandeepsomavarapu","sandeepsomavarapu")
if m!=None:
    print("exactly matched")
else:
    print("failed to match")