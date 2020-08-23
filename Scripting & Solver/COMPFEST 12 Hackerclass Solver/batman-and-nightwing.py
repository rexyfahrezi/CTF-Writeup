from PIL import Image

biner = ''
black = "(0, 0, 0)"
i = 0

while i < 359:
	print('/img/{}.png'.format(i))
	im = Image.open('img/{}.png'.format(i))
	pix = im.convert("RGB").getpixel((10,15))

	if str(pix) == black:
		biner += '1'
		
	else:
		biner += '0'
	i += 1


hexa = hex(int(biner, 2)).strip('0x')
print('Flag : '+bytearray.fromhex(hexa).decode())