import sys
import os
import pygame

from pygame.locals import *

from PIL import Image
from PIL import ImageTk, Image
from mutagen.id3 import ID3
import io
import base64

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Drag a file onto the window.')

pygame.mixer.pre_init(44100, -16, 2, 512) #hz, channel, mono, buffer
pygame.mixer.set_num_channels(4) # Max amounts of sound to play at once
pygame.mixer.music.set_volume(0.02)

def ConImg(file, file_extension):
	try:
		file_base_name = os.path.basename(file)
		fe_len = len(file_extension)
		to_remov = len(file_base_name)
		new_file = f"{file[0:-to_remov]}{file_base_name[0:-fe_len]}.png"

		im = Image.open(file).convert("RGB")
		im.save(new_file, "png")
	except:
		pass
	else:
		return GotImg(new_file, file_extension, False)
def GotImg(file, file_extension, dragged_png):
	if dragged_png:
		niko = Image.open(file).convert("RGB")
		new_ico = f"{file[0:-len(os.path.basename(file))]}new_{os.path.basename(file)[0:-len(file_extension)]}.ico"
		niko.save(new_ico, sizes=([(16,16), (32, 32), (48, 48), (64, 64), (256, 256)]))
	try:
		img = pygame.transform.scale(pygame.image.load(file), (400, 400))  # load the image given the file name.
		pygame.display.set_caption(os.path.basename(file)) # show file name in title bar.

		return img
	except:
		pass
def start():
	img_in_b64 = base64.b64decode(b'iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAIAAAD/gAIDAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAUYSURBVHhe7ZddchwhDIR9kDzm/jfLGRwN0hItCKEGZsym+MrlgNT6oWv8kK/vQ5hjFsAxC+DNrK+vW7yjtjd1fpiHzJLTOx/n4A+blZHQ3vywWflQwPHduN0s5/HxeEv5MG9LXM/C1/JLnGx81rWWQqKPUw5GV+lu72T9Qo1WXvNeSOgpynnQBrwxIXcLJ+sXakzlNTgh93ec1DBlO2gAi50Sv1t8lj/CzHKckdA0ZaN467xHPtS04oyf1Qz0yUE6ZDgyTFkf76iVrSq/29isGjNbBynCyB3H6Cgnl2Jqq6oVZ1KPf0jUYiDbKrkmJeSOUNZEutTDzCozmEk9/gn4Ssj9nVacMbN+CXEN62kKSnWkvtaYVX4raNGBVpH+pInIMqW0W28KzBIzmPGzBQOtgv2xNeRfxZLNKGIqM362wBGnOaGVTIIyBhvTStXx7hLYlpaYgozc32nFC4Iyxl5CTu9ce4VTLWWmK9Bo8TXphYQs/CzTbVJgSFv1ft8i210C21KJg4WRBYKtMobabNFtrbNdMdEVaApxah/qXyj5mpFoGKPAbNRtrQVdMRHRZMx9/A4sqJH0EHZx3bQ7RgsiO0F7m2IKOk2c1DB2x2JSZLDWRPR/fv12fkT0otWQ4k5KTusITYoMzho6+PqWI5k66zRsjXNKhrE76knBqdfKSenotU2OjNGW+WIz2+0/gN2RJuVh8amsbOn144lI21zii81spD9KsyMPo9/xqbmEr5raKVNWw4WOuNXKKRnGWyL/DnJtnZC7QjtFiC7W3DHLadKKz9DsyHsQcg/Q0hdOZVhvIopEy6xaqXFSw3jD0HlmCT21ZVaQ2iweRMjdws+OsXJe2r8smXSKyGZxf4ZTDhENyvqOBavMYiQUABIHud2seeo/w5/iM8yS009zzALY3Sxy6pgVZR+niK3N2uqzInY3S057sK9Zu31WxKZmbegUsaNZezpFYGal/3IIElrNtk4RsFlyuse4nZ0ixs3KsF+E3EfZ3CligVmZYcvYppZTYz3vYKVZRLLrQu4KM0h0P6hW4fMsNou53KqUHNFx/4PK1K18rtkvJLQIeA859aiVHOHfQZsYaCgj99VgfaE9CjFfIZuY4FCSBZXDYN2hbQrxgE1MZOjl081OEU+YpW1Kj8KadPURzRKwGfGd9AOyTXzNhwgRMdRwBmxMfC2tzF/WwMfVVULdJsHGBNcyZRTUrjk/UpDoTnzMKWKxWSRoaXTckRGOdzVOn+Vgk/zNkgNNQZFylBpfFmyyCmxjczkKZiRkUWS7esbXRDosJDosPc1GFD1qZaTW0Vyz9zSLmVmurk2P9RrOZO8Amzezn1l7zLJpmeX09FNO9iaweTP7tWqdnmOp+8BG3mSWk5JThZO6D2zkzIoDLz9mGVCqzprBjJO6D2zkzIp+bZ1F9Q+AjfwIsyiVkdAisHYz47u1hcDXd7MtRDEEVjwzrFtbCHw9tAmJIX0LrMXMyEit1vh6dBPSoyU1Rr3TdGZepDZruuKBTahkoEqDFc8Mi+yaNRGlnBDGqjJY8eywQDlrusqBTahkoEqDFU/Oi9TyCELuDbqCmoGSAqw+vWJ2ZJfIlIhGg+pNNjVLTi7xTdLWC9be0awgwWWCsgi7vHwMxwhOEXJfwWebRRSO8JWR0Do+3ixCvElI6B7+B7Me45gFcMwCOGYBHLMAjlkAxyyAYxbAMQvgmAVwzAI4ZgEcswCOWQDHLIBjVpjv77+2VfaMKGm22gAAAABJRU5ErkJggg==')
	pillow_image = Image.open(io.BytesIO(img_in_b64))
	image = pygame.transform.scale(pygame.image.fromstring(pillow_image.tobytes(), pillow_image.size, pillow_image.mode), (400, 400))
	going = True
	while going:
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				going = False
			elif event.type == pygame.DROPFILE:
				file_extension = os.path.splitext(event.file)[1]
				if file_extension in [".webp", ".jpg", ".jfif"]:
					image = ConImg(event.file, file_extension)
				else:
					pass

		screen.blit(image, (0, 0))
		pygame.display.flip()
		clock.tick(30)
start()