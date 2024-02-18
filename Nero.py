import pandas as pd
import numpy as np
from skimage import io
import os
import shutil
from sklearn.datasets import load_sample_image
dir = 'C:/faces'
os.chdir(dir)
file_list = os.listdir('.')

names = list()
image_paths = list()
pics = list()

for image in file_list:
    p = str(dir + '/' + image)
    image_paths.append(p)
    #image = image.replace('.jpg', '')
    #image = image[:(len(image)-9)]
    names.append(image)

#images = [io.imread(path) for path in image_paths]
#images_array = np.array(images)
images = [io.imread(image) for path in image_paths]
    #image = load_sample_image(image)
    #image_vector = image.reshape(-1, 1)
    #pics.append(image_vector)
images_array = np.array(images)
print(pics)
#df = pd.DataFrame({'image': pics, 'name': names})
#print(df)
#print(image)
#print(names)
##print(image_paths)
#for i in range(len(names)):
#    shutil.move(image_paths[i], 'C:/faces')

# Создаем список изображений
# image_paths = ['path/to/image1.jpg', 'path/to/image2.jpg', 'path/to/image3.jpg', ...]
#
# Создаем список идентификаторов изображений
#
## Читаем изображения и преобразуем их в массив numpy
# images = [io.imread(path) for path in image_paths]
#
# Преобразуем массив numpy в массив pandas
# images_array = np.array(images)
#
# Создаем DataFrame с изображениями и идентификаторами
# df = pd.DataFrame({'image': images_array, 'id': image_ids})
