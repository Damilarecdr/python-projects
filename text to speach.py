from gtts import gTTS
import os

# Text you want to convert to speech
text = "Hello, this is a test of text-to-speech conversion in Python."

# Create a gTTS object
tts = gTTS(text)

# Save the speech as an audio file
tts.save("output.mp3")

# Play the audio file (platform-dependent, may not work on all systems)
os.system("mpg321 output.mp3")  # Linux
# os.system("afplay output.mp3")  # macOS
# os.system("start output.mp3")   # Windows
