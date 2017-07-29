import cv2
import numpy as np
import os
import pickle
#import pylab as plt

if __name__ == '__main__': #histgram.pyがモジュールではなくスクリプトとして実行される時は
    img_size=(50,50)
    target_file = 'target.jpg'
    img_dir = os.path.abspath(os.path.dirname(__file__)) + '/pictures/'
    #プログラムを実行するディレクトリの下にpictureというディレクトリを作り、画像はここに置く

    print(img_dir)
    target_img_path = img_dir + target_file


    target_img=cv2.imread(target_img_path)
    target_img=cv2.resize(target_img, img_size)

    hdims = [256]
    hranges = [0, 256]
    target_histgram = cv2.calcHist([target_img],[0],None,hdims,hranges)

    files=os.listdir(img_dir)

    print(files)

    list=dict()


    for file in files:
        print(file)
        if file=='.DS_Store' or file==target_file:
            continue

        comparing_img_path=img_dir+file
        print(comparing_img_path)
        comparing_img=cv2.imread(comparing_img_path)
        print(img_size)
        print(comparing_img.shape)
        comparing_img=cv2.resize(comparing_img, img_size)
        comparing_histgram=cv2.calcHist([comparing_img],[0],None,hdims,hranges)
        #comparing_histgramはリスト型


        list.update({file:comparing_histgram})
        with open('sample.pickle', mode='wb') as f:
            pickle.dump(list, f)

        #ret = cv2.compareHist(target_histgram, comparing_histgram,0)
        #print(file, ret)





with open('sample.pickle', mode='rb') as f:
    comparing_histgram_list=pickle.load(f)

max=0
key=""
for filename, histgram in comparing_histgram_list.items():
    ret = cv2.compareHist(target_histgram, histgram,0)
    if ret>max:
        max=ret
        key=filename

print(key, max)
