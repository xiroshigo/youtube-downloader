from pytube import YouTube  
import os, sys

def clearscreen():
	if sys.platform == "linux2":
		os.system("clear")
	elif sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")

__banner__ = """\033[1;32m
██▀▀▀▀███▀▀▀▀███▀▀▀▀██            
█┌─┐┌─┐█┌─┐┌─┐█┌─┐┌─┐█           
█└─┘└─┘█└─┘└─┘█└─┘└─┘█          
██▌└┘▐███▌└┘▐███▌└┘▐██           
██┼┼┼┼███┼┼┼┼███┼┼┼┼██           
██▄▄▄▄███▄▄▄▄███▄▄▄▄██           

•••••••••••••••••••••••••••     

"""
__text__ = """\033[1;34mdasturchi: @darknet_off1cial\nkanalimiz: @termux_uz_private\ndastur youtubedan videolarni yuklab beradi"""

clearscreen()
os.system("termux-open-url https://t.me/termux_uz_private")

print(__banner__)
print(__text__)

urlVid = input("\033[1;35mSkachat qimoqchi bogan videoizni silkasini yozing: ")

myVid = YouTube(urlVid)

print("\033[1;36m\n••••••••••••••••••••••••••••••")
print(f"\nSarlavha: {myVid.title}")
print(f"\nKanali: {myVid.author}")
print(f"\nPrasmotrlar: {myVid.views}")
print(f"\nUzunligi: {myVid.length}")
quality = int(input("\nVideoni qanday sifatda yuklab olasiz? 1080 / 720 / 360 \nvideo sifati: "))
print("video yuklanmoqda... iltimos kutig...")

if quality == 1080:
	stream = myVid.streams.get_by_itag(137)
	stream.download()
	print("Yuklab olindi...")

elif quality == 720:
	stream = myVid.streams.get_by_itag(22)
	stream.download()
	print("Yuklab olindi...")

elif quality == 360:
	stream = myVid.streams.get_by_itag(18)
	stream.download(r'/sdcard/Download/')
	print("yuklab olindi")

