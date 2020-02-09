import os
import subprocess

videoPath = 'video_path'
video_file_name_array= os.listdir(videoPath)
    
for video_file_name in video_file_name_array:
  os.chdir(videoPath)
  subprocess.call(['ffmpeg', '-i', video_file_name, '-vf', 'fps=1', '../final/'+video_file_name+'_img%06d.jpg'])

