import re
matcher=re.finditer("\D","a7@ b9a zW")
for match in matcher:
    print(match.start(),"...",match.group())