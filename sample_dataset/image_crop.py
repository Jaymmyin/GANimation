import cv2
import numpy as np 
import os
import sys
sys.path.insert(0, 'C:\\Files\\Course\\AI 240\\Proj\\GANimation-20190112\\utils')
import face_utils as face

#modified by Jie Yin
# input_image_path  = 'C:\\Files\\Course\\AI 240\\Proj\\wiki_crop\\'
# output_image_path = 'C:\\Files\\Course\\AI 240\\Proj\\output_wiki_crop\\'
input_path_list, output_path_list = [], []
for i in range(24, 100):
    if i < 10:
        input_image_path = 'C:\\Files\\Course\\AI 240\\Proj\\wiki_crop\\' + '0' + str(i) + '\\'
        output_image_path = 'C:\\Files\\Course\\AI 240\\Proj\\output_wiki_crop\\' + '0' + str(i) + '\\'
        input_path_list.append(input_image_path)
        output_path_list.append(output_image_path)
    else:
        input_image_path = 'C:\\Files\\Course\\AI 240\\Proj\\wiki_crop\\' + str(i) + '\\'
        output_image_path = 'C:\\Files\\Course\\AI 240\\Proj\\output_wiki_crop\\' + str(i) + '\\'
        input_path_list.append(input_image_path)
        output_path_list.append(output_image_path)


for i in range(len(input_path_list)): 
    print(input_path_list[i])
    image_names = os.listdir(input_path_list[i])
    error = open('error.txt', 'w')
    # print(len(image_names))
    count = 0
    for name in image_names:
        img = cv2.imread(input_path_list[i]+name)
        name = name.split('.')[0]
        try:
            output, face_origin_pos = face.face_crop_and_align(img)
        except:
            try:
                bb = face.detect_biggest_face(img)
                output = img[bb[1]:bb[1]+bb[3], bb[0]:bb[0]+bb[2]]
            except:
                count += 1
                print('cannot find face')
                continue
        if output.shape[0] != 128 or output.shape[1] != 128:
            output = cv2.resize(output, (128,128))
            # print('resize : ',name)
        cv2.imwrite(output_path_list[i]+name+'.jpg', output)
    print(count)
    error.close()