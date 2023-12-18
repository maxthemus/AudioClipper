import sounddevice as sd
print(sd.query_devices())


fs = 48000
duration = 10
channels = 1
sd.default.device =8 
myRecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)

sd.wait()
    
print("Recording Finished!")

print(myRecording)


sd.play(myRecording, samplerate=fs)

sd.wait()
print("DONE")