# coding=utf-8
import numpy as np

def loadDataset():
  lines = [
    ['my','dog','has','flea', 'problems', 'help', 'please'],
    ['maybe', 'not','take','him','to','dog', 'park', 'stupid'],
    ['my','dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
    ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
    ['mr','licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
    ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
  ]
  classVec = [0, 1, 0, 1, 0, 1] # 1代表侮辱

  return lines, classVec

def createVecabList(dataSet):
  vocabSet = set([])
  for line in dataSet:
    vocabSet = vocabSet | set(line)

  return list(vocabSet)

def line2Vec(vocabList, line):
  returnVec = [0] * len(vocabList)
  for word in line:
    if word in vocabList:
      returnVec[vocabList.index(word)] = 1
    else: print 'the word %s is not in my vocabulary' % word
  
  return returnVec

def trainNB0(mat, cate):
  lineNum = len(mat)
  wordNum = len(mat[0])
  pAbusive = sum(cate) / float(lineNum)

  # 初始化概率
  p0Num = np.ones(wordNum)
  p1Num = np.ones(wordNum)

  p0Denom = 2.0 # TODO 为什么是2
  p1Denom = 2.0

  # 计算每个word出现的概率
  for i in range(lineNum):
    if cate[i] == 1:
      p1Num += mat[i]
      p1Denom += sum(mat[i])
    else:
      p0Num += mat[i]
      p0Denom += sum(mat[i])

  p1Vect = np.log(p1Num / p1Denom) # 为什么要用log，因为f(x), 和ln(f(x))是正相关的，f(x) 可能会因为过小，影响后面的成绩计算
  p0Vect = np.log(p0Num / p0Denom)

  return p0Vect, p1Vect, pAbusive

def classifyNB(vec2classify, p0vect, p1vect, pClass1):
  # 概率相乘
  p1 = sum(vec2classify * p1vect) + np.log(pClass1)
  p0 = sum(vec2classify * p0vect) + np.log(1.0 - pClass1)

  if p1 > p0:
    return 1
  else :
    return 0

def test():
  lines, classVec = loadDataset()
  vocabList = createVecabList(lines)
  mat = []
  for line in lines:
    vec = line2Vec(vocabList, line)
    mat.append(vec)

  p0Vect, p1Vect, pAbusive = trainNB0(mat, classVec)

  # testLine = ['love', 'my', 'dalmation']
  testLine = ['stupid', 'my', 'garbage']
  testVect = line2Vec(vocabList, testLine)
  
  print classifyNB(testVect, p0Vect, p1Vect, pAbusive)

test()