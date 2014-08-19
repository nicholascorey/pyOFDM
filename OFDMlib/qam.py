
import scipy
from scipy import pi



class Qam64:
	def __init__(self, freq, duration, sampleRate):
		self.freq = freq
		self.duration = duration
		self.sampleRate = sampleRate
		self.grayCode = [0b000, 0b001, 0b011, 0b010, 0b110, 0b111, 0b101, 0b100]
	
	@staticmethod
	def getSymbolSize():
		return 6
		
	def waveOut(self, bits):
		a = self._amplitude(bits)
		return 	a[0] * scipy.sin(2 * pi * self.freq * scipy.linspace(0, self.duration, self.duration*self.sampleRate)) + \
				a[1] * scipy.cos(2 * pi * self.freq * scipy.linspace(0, self.duration, self.duration*self.sampleRate))

	def _amplitude(self, bits):
		high = self.grayCode.index(int(bits[0:3], 2)) / 7.0 * 2 - 1
		low = self.grayCode.index(int(bits[3:6], 2)) / 7.0 * 2 - 1
		return high, low

