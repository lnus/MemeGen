import textwrap
from PIL import Image, ImageDraw, ImageFont

class memeGen():
	def generate(self, top, bot, meme):
		#Opens up your SPICY MEME TEMPLATE
		im = Image.open("templates/{image}".format(image=meme+".png"))

		#Resizes the image for perfect MEME size
		im = im.resize((500, 500), Image.ANTIALIAS)

		#Stupid fucking useless arguments
		width, height = im.size
		draw = ImageDraw.Draw(im)
		font = ImageFont.truetype("impact.ttf", 60)
		topH, topP = 0, 10
		botH, botP = 420, 10
		pTop = textwrap.wrap(top, width=15)
		pBot = textwrap.wrap(bot, width=15)

		
		#Writes the text with a spicy meme outline
		for line in pTop:
			w, h = draw.textsize(line, font=font)
			draw.text((((width - w)/2)-2, topH), top, font=font, fill="black")
			draw.text((((width - w)/2)+2, topH), top, font=font, fill="black")
			draw.text((((width - w)/2), topH-2), top, font=font, fill="black")
			draw.text((((width - w)/2), topH+2), top, font=font, fill="black")
			draw.text(((width - w)/2, topH), top, font=font, fill="white")
			topH += h + topP
		
		for line in pBot:
			w, h = draw.textsize(line, font=font)
			draw.text((((width - w)/2)-2, botH), bot, font=font, fill="black")
			draw.text((((width - w)/2)+2, botH), bot, font=font, fill="black")
			draw.text((((width - w)/2), botH-2), bot, font=font, fill="black")
			draw.text((((width - w)/2), botH+2), bot, font=font, fill="black")
			draw.text(((width - w)/2, botH), bot, font=font, fill="white")
			botH += h + botP

		#saves the dank meme	
		im.save(meme+".png", "PNG")