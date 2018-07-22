# coding=utf-8
import matplotlib.pyplot as plt

decisionNode = dict(boxstyle='sawtooth', fc="0.8")
leafNode = dict(boxstyle='round4', fc="0.8")

arrow_args = dict(arrowstyle='<-')

def plotNode(nodeTxt, sPoint, ePoint, nodeType):
  createPlot.ax1.annotate(
    nodeTxt, 
    xy=sPoint, 
    xycoords='axes fraction',
    xytext=ePoint,
    textcoords='axes fraction',
    va='center',
    ha='center',
    bbox=nodeType,
    arrowprops=arrow_args
  )

def createPlot():
  fig = plt.figure(1, facecolor='white')
  fig.clf()
  createPlot.ax1 = plt.subplot(111, frameon=False)
  plotNode('decision node', (0.1, 0.5), (0.5, 0.1), decisionNode)
  plotNode('leaf node', (0.3, 0.8), (0.8, 0.1), leafNode)
  plt.show()

# createPlot()

def getLeafNum(myTree):
  leafNum = 0
  firstStr = myTree.keys()[0]
  secondDict = myTree[firstStr]

  for key in secondDict.keys():
    if (type(secondDict[key]).__name__ == 'dict'):
      leafNum += getLeafNum(secondDict[key])
    else:
      leafNum += 1
  
  return leafNum

def getTreeDepth(myTree):
  maxDepth = 0
  firstStr = myTree.keys()[0]
  secondDict = myTree[firstStr]

  for key in secondDict.keys():
    if (type(secondDict[key]).__name__ == 'dict'):
      thisDepth = getTreeDepth(secondDict[key]) + 1
    else: thisDepth = 1
    
    if thisDepth > maxDepth:
      maxDepth = thisDepth
  
  return maxDepth

def createTree(): 
  return {'first cate': {0: 'no', 1: {'second cate': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'yes'}}}}

# ---------------------画树-------------------
def plotMidText(sPoint, ePoint, txtString):
  xMid = (ePoint[0] - sPoint[0]) / 2 + sPoint[0]
  yMid = (ePoint[1] - sPoint[1]) / 2 + sPoint[1]

  createTreePlot.ax1.text(xMid, yMid, txtString, va='center', ha='center', rotation=30)

def plotTreeNode(nodeTxt, sPoint, ePoint, nodeType):
  createTreePlot.ax1.annotate(
    nodeTxt, 
    xy=sPoint, 
    xycoords='axes fraction',
    xytext=ePoint,
    textcoords='axes fraction',
    va='center',
    ha='center',
    bbox=nodeType,
    arrowprops=arrow_args
  )


def plotTree(myTree, sPoint, nodeTxt):
  leafNum = getLeafNum(myTree)
  # depth = getTreeDepth(myTree)
  firstStr = myTree.keys()[0]
  # plotTree.xOff = -1/2/plotTree.totalW + 1.0 / plotTree.totalW * n (n个叶子节点，从0计数)
  # 1.0 / plotTree.totalW * n + leafNum / 2.0 / plotTree.totalW = 前n个叶子节点的偏移 + 剩下叶子占据的宽度/2
  ePoint = (plotTree.xOff + (1.0 + float(leafNum)) / 2.0 / plotTree.totalW, plotTree.yOff) # TODO
 
  plotMidText(sPoint, ePoint, nodeTxt)
  plotTreeNode(firstStr, sPoint, ePoint, decisionNode)
  secondDict = myTree[firstStr]
  plotTree.yOff -= 1.0 / plotTree.totalD

  for key in secondDict.keys():
    if type(secondDict[key]).__name__ == 'dict':
      plotTree(secondDict[key], ePoint, str(key))
      pass
    else:
      plotTree.xOff += 1.0 / plotTree.totalW
      print plotTree.xOff
      plotTreeNode(secondDict[key], ePoint, (plotTree.xOff, plotTree.yOff), leafNode)
      plotMidText(ePoint, (plotTree.xOff, plotTree.yOff), str(key))
    
  plotTree.yOff += 1.0 / plotTree.totalD # 画完子树，将y移动回父节点

def createTreePlot(iniTree):
  fig = plt.figure(1, facecolor='white')
  fig.clf()
  axprops = {} # dict(xticks=[], yticks=[])
  createTreePlot.ax1 = plt.subplot(111, frameon=False, **axprops)

  plotTree.totalW = float(getLeafNum(iniTree))
  plotTree.totalD = float(getTreeDepth(iniTree))
  plotTree.xOff = -0.5 / plotTree.totalW
  plotTree.yOff = 1.0

  plotTree(iniTree, (0.5, 1.0), 'o')
  plt.show()

# createTreePlot(createTree())