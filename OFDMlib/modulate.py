
import qam

SAMPLE_RATE = 48000



def stream(inStream, outStream, bandwidth, symbolDuration):
	qamType = qam.Qam64
	ofdm = OFDM(bandwidth, symbolDuration, qamType)
	bitReader = BitReader(inStream, ofdm.getSymbolSize())

	while True:
		data = bitReader.read()
		if data == None:
			break
		print data
		print ofdm.encode(data)




class BitReader:
	def __init__(self, inStream, numBits):
		self.inStream = inStream
		self.numBits = numBits
		self.buffer = ''

	def read(self):
		try:
			while len(self.buffer) < self.numBits:
				self.buffer += self.toBinary(self.readByte())
			output = self.buffer[:self.numBits]
			self.buffer = self.buffer[self.numBits:]
			return output
		except EOFError:
			if self.buffer <> '':
				output = (self.buffer + ('0'*self.numBits))[:self.numBits]
				self.buffer = ''
				return output
			else:
				return None
			
	def toBinary(self, char):
		return ('00000000' + bin(ord(char))[2:])[-8:]
	
	def readByte(self):
		output = self.inStream.read(1)
		if output == "":
			raise EOFError
		return output



class OFDM:
	def __init__(self, bandwidth, symbolDuration, qamType):
		spacing = 1.0 / symbolDuration
		numChannels = int(bandwidth / spacing)
		freqs = [(c*float(bandwidth)+bandwidth/2.0)/numChannels for c in range(numChannels)]
		self.qamType = qamType
		self.channels = [qamType(f, symbolDuration, SAMPLE_RATE) for f in freqs]
		
	def getSymbolSize(self):
		return self.qamType.getSymbolSize() * len(self.channels)

	def encodeSymbol(self, bits):
		assert len(bits) == self.getSymbolSize()
		return sum([self.channels[i].waveOut(bits[i*self.qamType.getSymbolSize():(i+1)*self.qamType.getSymbolSize()]) for i in range(len(self.channels))])



