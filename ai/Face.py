import os
import glob

path='C:/ai/Face_Recognition'
os.chdir(path)
file_list = os.listdir('Images')


# Get Image names stored in "Images" folder
image_path_names=[]
person_names=set()
for file_name in file_list:
  image_path_names.append(path+'/Images/'+file_name)
  person_names.add(image_path_names[-1].split('/')[-1][:-9])
print(image_path_names)
print(len(image_path_names))
print(len(person_names))

import cv2
import matplotlib.pyplot as plt
import dlib

dnnFaceDetector=dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")