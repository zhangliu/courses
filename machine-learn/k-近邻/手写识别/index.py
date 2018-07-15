# coding=utf-8
import os
import numpy as np
# import struct
import matplotlib.pyplot as plt
import PIL as pil

imgFile = './t10k-images-idx3-ubyte'
labelFile = './t10k-labels-idx1-ubyte'
sampleImgFile = './sample.png'
height = 28
width = 28

def load_images(imgFile, labelFile, sampleImgFile):
  with open(labelFile, 'rb') as fp:
    # '>'-大端(see: 'http://www.ruanyifeng.com/blog/2007/10/ascii_unicode_and_utf-8.html')，'I'-无符号整形
    # magic, n = struct.unpack('>II', fp.read(8))
    fp.read(8)
    labels = np.fromfile(fp, dtype=np.uint8)

  with open(imgFile, 'rb') as fp:
    # MNIST 数据集中的每张图片由 28 x 28 个像素点构成
    fp.read(16)
    images = np.fromfile(fp, dtype=np.uint8).reshape(len(labels), width * height)

  imgInfo = np.array(pil.Image.open(sampleImgFile))
  sampleImg = []
  for i in range(width):
    for j in range(height):
      sampleImg.append(imgInfo[i][j].sum())

  return images, labels, np.array(sampleImg)

# print load_images(imgFile, labelFile, sampleImgFile)

def print_img():
  images, _, _ = load_images(imgFile, labelFile, sampleImgFile)
  fig = plt.figure()
  for i in range(10):
    img = images[i].reshape(28, 28)
    ax = fig.add_subplot(2, 5, i + 1)
    ax.imshow(img)
    ax.set_xticks([])
    ax.set_yticks([])

  plt.show()
  plt.close()

# print print_img()


