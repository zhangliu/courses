import tree
import treePlotter

fp = open('./data.txt')
lenses = [line.strip().split(' ') for line in fp.readlines()]
labels = ['age', 'prescript', 'astigmatic', 'tearRate', 'other']

myTree = tree.createTree(lenses, labels)
treePlotter.createTreePlot(myTree)