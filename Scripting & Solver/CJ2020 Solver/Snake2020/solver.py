flag = ''
temp = 0
pivot = 0
c = ''

with open('milestone.txt') as f:
   for line in f:
       pivot = int(line) - temp
       temp = int(line)
       c = int(pivot)
       if c <= 256:
          flag += chr(c)
print(flag)
