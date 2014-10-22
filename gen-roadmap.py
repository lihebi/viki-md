#!/usr/bin/env python2

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
  print root, dirs, files
  for f in files:
    add(root, f)

od = collections.OrderedDict(sorted(result.items()))

js = json.dumps(od,indent=2)
with open('roadmap.json', 'w') as f:
  f.write(js)
