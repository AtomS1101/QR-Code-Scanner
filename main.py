import sys
import webbrowser

from qrscanner import QRScanner
from argmanager import ArgManager

def openLink(text):
	if text.startswith("http"):
		print(f'\n  link: "{text}"')
		user_confirm = input("\n  Do you want to open the link? (y/n): ")
		if user_confirm.lower() == 'y':
			webbrowser.open(text)
	else:
		print(f'\n  text: "{text}"')

def main():
	scanner = QRScanner()
	link, qr_image, status = scanner.scan()
	scanner.close()
	if status == "success":
		ArgManager(sys.argv, qr_image).checkArg()
		openLink(link[0])

if __name__ == "__main__":
	main()
