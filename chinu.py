import numpy as np


filename = np.loadtxt("filename.txt",unpack=True)

f1=[np.loadtxt(i,unpack=True,usecols=1) for i in filename]
