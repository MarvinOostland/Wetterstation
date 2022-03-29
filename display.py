from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import ST7735
import datetime
import os
from bme280 import*

disp = ST7735.ST7735(port=0, cs=0, dc=25, backlight=None, rst=24, width=125, height=159, rotation=270, invert=False)

class display():
    def __init__(self, temp=None, disp=None):
        self.temp=temp
        
    def setup():
        global presmin
        global presmax
        global hvacmax
        global hvacmin
        global tempmax
        global tempmin
        temperature,pressure,humidity = readBME280All()
        presmin=int(pressure)
        presmax=int(pressure)
        hvacmin=int(humidity)
        hvacmax=int(humidity)
        tempmin=int(temperature)
        tempmax=int(temperature)
        
        
    def drawTEMP():
        
        WIDTH = disp.width
        HEIGHT = disp.height
        global tempmax
        global tempmin

        img = Image.new('RGB', (WIDTH, HEIGHT))
        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype(font='/home/pi/Desktop/schule/software_wetter_station/main_program/telegrama_render.otf', size=42)
        fonttiny=ImageFont.truetype(font='/home/pi/Desktop/schule/software_wetter_station/main_program/telegrama_render.otf', size=16)

        temperature,pressure,humidity = readBME280All()

        draw.rectangle((0, 0, WIDTH - 1, HEIGHT - 1), outline=(0, 0, 255), fill=(0, 0, 0))
        draw.text((8, 25), f'{int(temperature)}°C', font=font, fill=(255, 255, 255))
        draw.text((8, 6), "Temperature", font=fonttiny, fill=(255, 255, 255))
        if temperature>=tempmax:
            tempmax=int(temperature)
        if temperature<=tempmin:
            tempmin=int(temperature)
        #draw.text((8, 60), "", font=fonttiny, fill=(255, 255, 255))
        #draw.text((8, 75), "", font=fonttiny, fill=(255, 255, 255))
        draw.text(
            (8, 90), f"Max:{str(tempmax)}°C", font=fonttiny, fill=(255, 255, 255)
        )

        draw.text(
            (8, 105), f"Min:{str(tempmin)}°C", font=fonttiny, fill=(255, 255, 255)
        )


        disp.display(img)
        
    def drawCLOCK():
        
        WIDTH = disp.width
        HEIGHT = disp.height

        now = datetime.datetime.now()
        img = Image.new('RGB', (WIDTH, HEIGHT))
        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype(font='/home/pi/Desktop/schule/software_wetter_station/main_program/telegrama_render.otf', size=42)
        fonttiny=ImageFont.truetype(font='/home/pi/Desktop/schule/software_wetter_station/main_program/telegrama_render.otf', size=16)
        
        draw.rectangle((0, 0, WIDTH - 1, HEIGHT - 1), outline=(0, 0, 255), fill=(0, 0, 0))
        draw.text((8, 25), str(now.strftime("%H:%M")), font=font, fill=(255, 255, 255))
        draw.text((8, 6), "Time", font=fonttiny, fill=(255, 255, 255))
        #draw.text((8, 60), "", font=fonttiny, fill=(255, 255, 255))
        #draw.text((8, 75), "", font=fonttiny, fill=(255, 255, 255))
        #draw.text((8, 90), "", font=fonttiny, fill=(255, 255, 255))
        draw.text((8, 105), str(now.strftime("%d.%m.%Y")), font=fonttiny, fill=(255, 255, 255))
        
        disp.display(img)

    def drawPRES():
        WIDTH = disp.width
        HEIGHT = disp.height
        global presmax
        global presmin

        img = Image.new('RGB', (WIDTH, HEIGHT))
        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype(font='/home/pi/Desktop/schule/software_wetter_station/main_program/telegrama_render.otf', size=42)
        fonttiny=ImageFont.truetype(font='/home/pi/Desktop/schule/software_wetter_station/main_program/telegrama_render.otf', size=16)

        temperature,pressure,humidity = readBME280All()

        draw.rectangle((0, 0, WIDTH - 1, HEIGHT - 1), outline=(0, 0, 255), fill=(0, 0, 0))
        draw.text(
            (8, 25),
            f'{str(int(pressure)-1000)}hPa',
            font=font,
            fill=(255, 255, 255),
        )

        draw.text((8, 6), "Pressure", font=fonttiny, fill=(255, 255, 255))
        #draw.text((8, 60), "", font=fonttiny, fill=(255, 255, 255))
        if pressure>=presmax:
            presmax=int(pressure)
        if pressure<=presmin:
            presmin=int(pressure)
        #draw.text((8, 75), "", font=fonttiny, fill=(255, 255, 255))
        draw.text(
            (8, 90),
            f"Max:{str(presmax-1000)}hPa",
            font=fonttiny,
            fill=(255, 255, 255),
        )

        draw.text(
            (8, 105),
            f"Min:{str(presmin-1000)}hPa",
            font=fonttiny,
            fill=(255, 255, 255),
        )


        disp.display(img)

    
    def drawHVAC():
        WIDTH = disp.width
        HEIGHT = disp.height
        global hvacmax
        global hvacmin

        img = Image.new('RGB', (WIDTH, HEIGHT))
        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype(font='/home/pi/Desktop/schule/software_wetter_station/main_program/telegrama_render.otf', size=42)
        fonttiny=ImageFont.truetype(font='/home/pi/Desktop/schule/software_wetter_station/main_program/telegrama_render.otf', size=16)

        temperature,pressure,humidity = readBME280All()

        draw.rectangle((0, 0, WIDTH - 1, HEIGHT - 1), outline=(0, 0, 255), fill=(0, 0, 0))
        draw.text((8, 25), f'{int(humidity)}%', font=font, fill=(255, 255, 255))
        draw.text((8, 6), "Humidity", font=fonttiny, fill=(255, 255, 255))
        #draw.text((8, 60), "", font=fonttiny, fill=(255, 255, 255))
        if humidity>=hvacmax:
            hvacmax=int(humidity)
        if humidity<=hvacmin:
            hvacmin=int(humidity)
        #draw.text((8, 75), "", font=fonttiny, fill=(255, 255, 255))
        draw.text((8, 90), f"Max:{str(hvacmax)}%", font=fonttiny, fill=(255, 255, 255))
        draw.text(
            (8, 105), f"Min:{str(hvacmin)}%", font=fonttiny, fill=(255, 255, 255)
        )


        disp.display(img)
