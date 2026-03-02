class ArgManager:
	def __init__(self, arg, qr_image):
		self._arg = arg
		self.qr_image = qr_image

	def drawQR(self, qr_image, marker):
		x_size = len(qr_image[0])
		y_size = len(qr_image[0][0])
		for x in range(x_size):
			for y in range(y_size):
				print(" " if qr_image[0][x][y] == 255 else marker, end="")
			print()

	def checkArg(self):
		if "-d" in self._arg:
			marker = self._arg[2] if len(self._arg) > 2 else "█"
			self.drawQR(self.qr_image, marker)
