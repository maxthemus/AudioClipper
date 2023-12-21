import sounddevice as sd
import numpy as np
import sys
import asyncio

#print(sd.query_devices())
sample_rate = 44100
channels = 4
duration = 5  # in seconds

insertIndex = 0
audio_data = []


async def audio_stream(callback):
    print(sd.query_devices())
    stream = sd.InputStream(device=("default", "Blue Snowball"), callback=callback, samplerate=sample_rate, channels=2)
    stream.start()

    sd.sleep(duration * 1000)

    stream.stop()


# Callback function to process audio data (you can customize this function)
def audio_callback(indata, frames, time, status):
    global audio_data
    if status:
        print(status)
    for sub_array in indata:
        array = sub_array.tolist()
        audio_data.append(array)


print(sd.query_devices(kind='input'))



# Start the audio stream with the callback function
asyncio.run(audio_stream(audio_callback))



print("PLAY BACK")
value = input("TEST")
sd.default.device = "default"
sd.play(audio_data, sample_rate)
sd.wait()


sys.exit()

#https://www.reddit.com/r/Ubuntu/comments/se4vl7/pulseaudio_audio_output_to_send_virtual/
#https://bbs.archlinux.org/viewtopic.php?id=257270