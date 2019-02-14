import numpy as np
import os
from tqdm import tqdm
import argparse
import glob
import re
import pickle

parser = argparse.ArgumentParser()
parser.add_argument('-ia', '--input_aus_filesdir', type=str, help='Dir with imgs aus files')
parser.add_argument('-op', '--output_path', type=str, help='Output path', default = './')
args = parser.parse_args()

def get_data(filepaths):
    data = dict()
    for filepath in tqdm(filepaths):
        content = np.loadtxt(filepath, delimiter=',', skiprows=1)
        if np.size(content.shape) == 1:
            data[os.path.basename(filepath[:-4])] = [content[-1], content[1]]
    return data

def save_dict(data, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

def main():
    sub_folder = "../sample_dataset/fuck/temp/"
    filepaths = os.listdir(sub_folder)
    
    # make relative path based on sub folder
    for x in range(len(filepaths)):
        filepaths[x] = sub_folder + filepaths[x]
        pass

    filepaths.sort()
    # create aus file
    data = get_data(filepaths)

    if not os.path.isdir(args.output_path):
        os.makedirs(args.output_path)
    save_dict(data, os.path.join(args.output_path, "aus"))

import shutil
def change_file_name():
    sub_folder = '../../out_wiki_crop/'
    desti_folder = '../../out_wiki_crop/'
    filepaths = os.listdir(sub_folder)

    # make relative path based on sub folder
    for x in range(len(filepaths)):
        filepaths[x] = sub_folder + filepaths[x]
        pass

    print(filepaths)
    # 00 01 
    for fp in filepaths:
        if not os.path.isdir(fp): continue
        image_paths = os.listdir(fp)
        for image_name in image_paths:
            shutil.move(fp + "/" + image_name, desti_folder + fp +"_" + image_name)


    for fp in filepaths:
        # remove fp
        if os.path.isdir(fp):
            image_paths = os.listdir(fp)
            if len(image_paths) == 0: shutil.rmtree(fp)
        pass

    print(filepaths)


if __name__ == '__main__':
    change_file_name()
    # main()
    # file = open("./aus.pkl",'rb')
    # object_file = pickle.load(file)
    # file.close()
    # print(object_file)