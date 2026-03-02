import cv2
import time

class QRScanner:
	def __init__(self, timeout = 30):
		self._camera = cv2.VideoCapture(0)
		self._decoder = cv2.QRCodeDetector()
		self._timeout = timeout

	def capture(self):
		success, frame = self._camera.read()
		if not success:
			print("\n  !Failed to capture image.\n")
		isExists, decoded, _, qr_image = self._decoder.detectAndDecodeMulti(frame)
		return isExists, decoded, qr_image

	def checkTimeout(self, start_time):
		if time.time() - start_time > self._timeout:
			self._camera.release()
			print("\n  !Timeout: No QR code detected.\n")
			return True
		return False

	def close(self):
		self._camera.release()

	def scan(self):
		print("\n\n  Scanning...")
		start_time = time.time()
		while True:
			isExists, decoded, qr_image = self.capture()
			if isExists:
				if decoded[0]:
					return decoded, qr_image, "success"
				else:
					print("  Unable to decode. Make sure it's in focus.")
			if self.checkTimeout(start_time):
				return None, None, "timeout"
			time.sleep(0.1)
