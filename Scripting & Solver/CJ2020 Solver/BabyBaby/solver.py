flag = 'CJ2020'
list = [0x58,0x1b,0x36,0x2b,0x63,0x34,0x60,0x33,0x30,0x5a,0x65,0x65,0x2f,0x13,0x46,0x79,0x33,0x33,0x62,0x28,0x79]

for i in range(len(flag)):
	print(ord(flag[i])^list[i])