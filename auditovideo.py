from moviepy.editor import VideoFileClip

# Input video file path
input_video_path = 'input_video.mp4'

# Output audio file path
output_audio_path = 'output_audio.mp3'

# Load the video file
video = VideoFileClip(input_video_path)

# Extract the audio from the video
audio = video.audio

# Write the audio to an audio file
audio.write_audiofile(output_audio_path)

# Close the video and audio objects
video.close()
audio.close()

print(f'Video "{input_video_path}" has been converted to audio "{output_audio_path}"')
