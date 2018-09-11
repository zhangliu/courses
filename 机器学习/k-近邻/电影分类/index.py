# -*- coding: utf-8 -*-
import numpy as np
import operator

def genData():
  points = np.array([
    [1.1, 5], [1.5, 8], [1.3, 9],
    [10, 4], [9, 1.2], [8, 0.3]
  ])
  labels = ['love', 'love', 'love', 'action', 'action', 'action']
  return points, labels

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

data, labels = genData()
print classify([5, 5], data, labels, 3)

