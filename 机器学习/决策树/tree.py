# coding=utf-8
import math
import operator

def calcShannonEnt(dataSet):
  dataLength = len(dataSet)
  labelCounts = {}

  for row in dataSet:
    label = row[-1]
    if label not in labelCounts.keys():
      labelCounts[label] = 0
    labelCounts[label] += 1

  shannonEnt = 0.0
  for key in labelCounts:
    prob = float(labelCounts[key]) / dataLength
    shannonEnt -= prob * math.log(prob, 2)
  
  return shannonEnt

# print calcShannonEnt([
#   [1, 1, 'yess'],
#   [1, 1, 'yes'],
#   [1, 0, 'no'],
#   [0, 1, 'no'],
#   [0, 1, 'no'],
# ])

# 想象一个分布在二维空间的数据散点图，需要在数据之间划条线（按照x轴或者y轴），将它们分成两部分
def splitDataSet(dataSet, axis, value):
  retDataSet = []
  for row in dataSet:
    if row[axis] == value:
      newRow = row[:axis]
      newRow.extend(row[axis + 1:])
      retDataSet.append(newRow)

  return retDataSet

# print splitDataSet([
#   [1, 1, 'yes'],
#   [1, 1, 'yes'],
#   [1, 0, 'no'],
#   [0, 1, 'no'],
#   [0, 1, 'no'],
# ], 0, 0)

def chooseBestSplit(dataSet):
  featureNum = len(dataSet[0])
  baseEnt = calcShannonEnt(dataSet)
  bestInfoGain = 0.0
  bestFeature = -1

  for i in range(featureNum):
    values = [row[i] for row in dataSet]
    values = set(values)
    newEnt = 0.0
    for value in values:
      subDataSet = splitDataSet(dataSet, i, value)
      prob = len(subDataSet) / float(len(dataSet))
      newEnt += prob * calcShannonEnt(subDataSet) 
    infoGain = baseEnt - newEnt

    if infoGain > bestInfoGain:
      bestInfoGain = infoGain
      bestFeature = i

  return bestFeature

# print chooseBestSplit([
#   [1, 1, 'yes'],
#   [1, 1, 'yes'],
#   [1, 0, 'no'],
#   [0, 1, 'no'],
#   [0, 1, 'no'],
# ])

def majorityCnt(classList):
  classCount = {}
  for value in classList:
    if value not in classCount.keys():
      classCount[value] = 0
    classCount[value] += 1
  
  sortClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse=True)
  return sortClassCount[0][0]

def createTree(dataSet, labels):
  classList = [row[-1] for row in dataSet]

  if classList.count(classList[0]) == len(classList):
    return classList[0]
  
  if len(dataSet[0]) == 1:
    return majorityCnt(classList)

  bestFeature = chooseBestSplit(dataSet)
  # print bestFeature
  bestFeatureLabel = labels[bestFeature]
  myTree = {bestFeatureLabel: {}}

  del(labels[bestFeature])
  featValus = [row[bestFeature] for row in dataSet]
  featValus = set(featValus)
  for value in featValus:
    sublabels = labels[:]
    # 挑选出值为value的分类，加入到myTree中
    subDataSet = splitDataSet(dataSet, bestFeature, value)
    myTree[bestFeatureLabel][value] = createTree(subDataSet, sublabels)
  
  return myTree

# print createTree([
#   [1, 1, 'yes'],
#   [1, 1, 'yes'],
#   [1, 0, 'no'],
#   [0, 1, 'no'],
#   [0, 1, 'no'],
# ], ['first cate', 'second cate'])