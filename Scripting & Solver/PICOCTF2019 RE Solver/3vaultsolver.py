buffer = list('jU5t_a_sna_3lpm11ga4e_u_4_m9rf48')
password = list('jU5t_a_sna_3lpm11ga4e_u_4_m9rf48')

for x in range(0,8):
    buffer[x] = password[x]
for x in range(8, 16):
    buffer[x] = password[23-x]
for x in range(16,32,2):
    buffer[x] = password[46-x]
for x in range(31,17,2):
    buffer[x] = password[x]

print(''.join(buffer))