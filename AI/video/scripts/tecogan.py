!git clone https://github.com/thunil/TecoGAN.git

!pip3 install -r requirements.txt

!python3 runGan.py 0

!pip install youtube_dl

!youtube-dl -f 18 -o "video.mp4" https://youtu.be/-uAZdIJIl8o

!mkdir /content/TecoGAN/LR/My_video
!mkdir /content/TecoGAN/HR/My_video

import cv2

import warnings
warnings.filterwarnings("ignore")
from google.colab import files

vidcap = cv2.VideoCapture('/content/TecoGAN/video.mp4')
success, image = vidcap.read()
count = 1

# %cd ESRGAN
while success:
  cv2.imwrite("/content/TecoGAN/LR/My_video/%04d.png" % count, image)    
  success, image = vidcap.read()
  print('Saved image ', count)
  count += 1

cd /content/TecoGAN

!python3 runGan.py 1

!ffmpeg -f image2 -framerate 30 -i /content/TecoGAN/results/My_video/output_%04d.png -c:v h264_nvenc -preset slow -qp 18 -pix_fmt yuv420p bridge.mp4

files.download('frames.zip')

import shutil


shutil.move("./frames.zip", "/content/gdrive/My Drive/frames.zip")
