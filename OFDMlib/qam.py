
import scipy
from scipy import pi



class Qam64:
	def __init__(freq, duration, sampleRate):
		self.freq = freq
		self.duration = duration
		self.sampleRate = sampleRate
		self.grayCode = [0b000, 0b001, 0b011, 0b010, 0b110, 0b111, 0b101, 0b100]
	
	def getInputBitSize():
		return 6
		
	def waveOut(bits):
		a = amplitude(bits)
		return 	a[0] * scipy.sin(2 * pi * self.freq * scipy.linspace(0, self.duration, self.duration*self.sampleRate)) + \
				a[1] * scipy.cos(2 * pi * self.freq * scipy.linspace(0, self.duration, self.duration*self.sampleRate))

	def amplitude(bits):
		high = self.grayCode.index((bits % 64) >> 3) / 7.0 * 2 - 1
		low = self.grayCode.index(bits % 8) / 7.0 * 2 - 1
		return high, low

