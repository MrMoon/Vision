# -*- coding: utf-8 -*-
"""Fast-SRGAN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1spk0XJ1ZFhLKJDMWxEDzbAxE7nJLORUC
"""

!git clone https://github.com/MrMoon/Fast-SRGAN.git

# Commented out IPython magic to ensure Python compatibility.
# %cd Fast-SRGAN/

!pip install -r requirements.txt

# Commented out IPython magic to ensure Python compatibility.
# %cd tools/
!python video_to_image.py --input $VIDEO_PATH
# %cd ../

!python infer.py --image_dir 'tools/' --output_dir 'output/'