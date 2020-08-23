import math 
import numpy as np 
from scipy.linalg import solve

a = np.array([[50, 11, 18, 12], [18, 12, 23, 2], [21, 11, 35, 42], [47, 2, 12, 40]])
b = [7681, 4019, 7160, 8080]
x = solve(a, b)
print("=======")
print("Nilai X :")
print(list(x))
print("=======")

#cast int
print("Integer :")
hasil = list(map(round, list(x)))
print(list(hasil))

print("=======")
password = ""
for i in hasil:
	temp = int(i)
	password += chr(temp)
	
print("Password : "+password)


#uji AX=B
print("=======")
print("Uji AX = B")
result = list(np.matmul(a, x))

print("A : "+str(list(a)))
print("X : "+str(hasil))

print("\nB : "+str(result))
