import numpy as np

def genData():
  points = np.array([
    [1.1, 5], [1.5, 8], [1.3, 9],
    [10, 4], [9, 1.2], [8, 0.3]
  ])
  labels = ['love', 'love', 'love', 'action', 'action', 'action']
  return points, labels