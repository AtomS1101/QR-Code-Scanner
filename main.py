import cv2
import sys
import webbrowser

def capture():
	camera = cv2.VideoCapture(0)
	camera.read()  # First capture is invalid
	ret, frame = camera.read()
	if not ret:
		print("\n  !Failed to capture image.")
		sys.exit()
	camera.release()
	return frame

def getLink(image):
	qrcode = cv2.QRCodeDetector()
	isExists, decodedInfo, points, straight = qrcode.detectAndDecodeMulti(image)
	if isExists:
		return decodedInfo[0]
	else:
		print("\n  !No QR code found")
		sys.exit()

def openLink(link):
	print(f'\n  link: "{link}"')
	userConfirm = input("Open link? (y/n): ")
	if userConfirm.lower() == 'y':
		webbrowser.open(link)

def main():
	image = capture()
	link = getLink(image)
	openLink(link)

if __name__ == "__main__":
	main()
