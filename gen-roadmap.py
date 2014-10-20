#!/usr/bin/env python2

import os,json

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
  print root, dirs, files
  for f in files:
    add(root, f)

print result
print
js = json.dumps(result, indent=2)
with open('roadmap.json', 'w') as f:
  f.write(js)
