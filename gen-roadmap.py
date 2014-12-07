#!/usr/bin/env python

import os,json
import collections

result = {}

def add(root, f):
  l = root.split('/')
  l.remove(l[0])
  tmp = result
  for li in l:
    if not li in tmp.keys():
      tmp[li] = {}
    tmp = tmp[li]
  tmp[f]=False

for root,dirs,files in os.walk('src'):
  dirs.sort()
  files.sort()
  for f in files:
    add(root, f)

js = json.dumps(result,indent=2)
with open('roadmap.json', 'w') as f:
  f.write(js)
print('generated roadmap.json')

def func(node, path, indent, f):
    for k in node.keys():
        if (node[k]==False):
            f.write(' '*indent+'* ['+k+']('+path+'/'+k+')\n')
        else:
            f.write(' '*indent+'* ['+k+']()\n')
            func(node[k], path+'/'+k, indent+2, f)


with open('SUMMARY.md', 'w') as f:
    func(result, 'src', 0, f)
print('generated SUMMARY.md')
