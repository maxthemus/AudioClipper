import sounddevice as sd
import numpy as np
import sys
import asyncio

#print(sd.query_devices())
sample_rate = 44100
channels = 2
duration = 1  # in seconds
index = 0

audio_data = np.zeros((0, channels), dtype=np.float32)

async def audio_stream(callback):
    print(sd.query_devices())
    stream = sd.InputStream(callback=callback, samplerate=sample_rate)
    stream.start()

    sd.sleep(5000)

    stream.stop()
    print(audio_data)
    print(np.size(audio_data))

# Callback function to process audio data (you can customize this function)
def audio_callback(indata, frames, time, status):
    global audio_data
    if status:
        print(status)
    audio_data = np.vstack((audio_data, indata))


# Start the audio stream with the callback function
asyncio.run(audio_stream(audio_callback))

sd.play(audio_data, sample_rate)
sd.wait()


sys.exit()