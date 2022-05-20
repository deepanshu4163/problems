s=input("enter string:")
d={'u': 0, 'l': 0}
for c in s:
	if c.isupper():
		d['u'] += 1
	elif c.islower():
		d['l'] += 1

print("upper case:", d['u'])
print("lower case:", d['l'])
