from moviepy.editor import *

video = VideoFileClip("travel.mp4")
subclip = video.subclip(10,30)
text= (TextClip("Hello, Moviepy!", fontsize=50, color='white').set_position('center','bottom')).set_duration(5)
result = CompositeVideoClip([subclip, text])

result.write_videofile("output.mp4")