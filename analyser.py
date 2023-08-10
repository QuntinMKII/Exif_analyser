# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 21:12:02 2022

@author: quntin
"""

from PIL import Image
from PIL.ExifTags import TAGS
import matplotlib.pyplot as plt
import os
from os import walk
import pandas as pd


focal = []
for (dirpath, dirnames, filenames) in walk(os.curdir):
    for f in filenames:
        if f.endswith(('.jpg','.JPG')):
            image = Image.open(os.path.join(dirpath, f))
            if image._getexif():
                if 272 in image._getexif().keys():
                    if image._getexif()[272] == 'X-T30':                
                        focal.append(image._getexif()[37386]) 

focal = pd.Series(focal,dtype=float)
focal_group = pd.cut(focal,[0,20,30,45,65,100,300]).value_counts(normalize=True)*100
plt.figure('group by length')
focal_group.sort_index().plot.bar(ylabel='%', xlabel='focal length')
plt.show()

focal_all = focal.value_counts(normalize=True)*100
plt.figure('all')
focal_all.sort_index().plot.bar(ylabel='%', xlabel='focal length')
plt.show()

