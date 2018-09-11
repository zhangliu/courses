# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
# import matplotlib as mpl
import matplotlib.pyplot as plt
import operator

file = './data.txt'

def genData():
  lineNum = 1000
  data = np.random.random((lineNum, 4))
  df = pd.DataFrame(data)
  
  df[0] = df[0] * 1000
  df[1] = df[1] * 2
  df[2] = df[2] * 10
  df[3] = np.random.randint(1, 4, size=(lineNum, 1))
  # df[3] = df[3].replace(0, '不喜欢的人')
  # df[3] = df[3].replace(1, '魅力一般的人')
  # df[3] = df[3].replace(2, '极具魅力的人')

  df.to_csv(file, header=False, index=False)

# genData()

def file2matrix(filename):
  fp = open(filename)
  lines = fp.readlines()
  lineNum = len(lines)
  mat = np.zeros((lineNum, 3))

  labels = []
  index = 0
  
  for line in lines:
    line = line.strip()
    segs = line.split(',')
    mat[index, :] = segs[0:3]
    labels.append(int(segs[-1]))
    index += 1
  return mat, labels

# print file2matrix(file)

def plot():
  mat, labels = file2matrix(file)
  fig = plt.figure()
  ax = fig.add_subplot(111)
  # 玩游戏 vs 冰淇淋
  ax.scatter(mat[:, 1], mat[:, 2], s=30 * np.array(labels), c=np.array(labels))
  plt.xlabel(u'玩视频游戏所耗时间百分比')
  plt.ylabel(u'每周消费的冰琪淋公升数')
  plt.show()
  plt.close()

# plot()

def toNorm():
  mat, labels = file2matrix(file)
  min = mat.min(0) # 0表示列的最小值
  max = mat.max(0)
  range = max - min

  m = mat.shape[0]
  normMat = mat - np.tile(min, (m, 1))
  normMat = normMat / np.tile(range, (m, 1))
  return normMat

# print toNorm()

def classify(point, data, labels, k):
  size = data.shape[0]

  # 计算距离
  diffMat = np.tile(point, (size, 1)) - data
  sqDiffMat = diffMat ** 2
  sqDistances = sqDiffMat.sum(axis=1)
  distances = sqDistances ** 0.5
  sortedDistances = distances.argsort()

  # 选择距离最小的k个点
  classCount = {}
  for i in range(k): 
    label = labels[sortedDistances[i]]
    classCount[label] = classCount.get(label, 0) + 1

  sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse=True)
  return sortedClassCount[0][0]

mat, labels = file2matrix(file)
print classify([1, 1, 2], mat, labels, 10)
