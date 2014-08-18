
import qam

SAMPLE_RATE = 48000



def stream(inStream, outStream, bandwidth, symbolDuration):
	spacing = 1.0 / symbolDuration
	numChannels = int(bandwidth / spacing)
	freqs = [(c*float(bandwidth)+bandwidth/2.0)/numChannels for c in range(numChannels)]
	channels = [qam.Qam64(f, symbolDuration, SAMPLE_RATE) for f in freqs]

	data = readStream(inStream)
	while data <> "":
		outStream.write(data)
		data = readStream(inStream)



def readStream(inStream):
	return inStream.read(30)

