import re 
count =0
matcher=re.finditer("ab","abaabababbab")
for match in matcher:
	count+=1
	print(match.start(),"....",match.end(),"...",match.group())
print(count)