# coding=utf-8
import os

def readFile(filePath):
  result = []
  files = os.listdir(filePath)
  for f in files:
    # 目录分隔符问题：unix使用'/'，windos使用'/'或者'\'都可以，参见：https://www.cnblogs.com/TTTTT/p/6017691.html
    # join可以避免目录相加时判断前目录是否有'/'的问题
    subFile = os.path.join(filePath, f)
    if os.path.isdir(subFile):
      result.extend(readFile(subFile))
    else: result.append(subFile)
  return result

files = readFile('/Users/ytx/Projects/courses')
for f in files: print f
# 列表生成式：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431779637539089fd627094a43a8a7c77e6102e3a811000
# files = [f for f in files]
