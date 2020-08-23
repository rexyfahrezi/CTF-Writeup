myBytes = [
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0o142, 0o131, 0o164, 0o63 , 0o163, 0o137, 0o142, 0o71 ,
            'e' , '9' , '2' , 'f' , '7' , '6' , 'a' , 'c' 
        ]

flag = ''
for x in range(0,24):
    flag += chr(myBytes[x])
    
for x in range(24,32):
    flag += str(myBytes[x])

print (flag)