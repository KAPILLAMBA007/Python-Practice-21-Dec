sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

def countElement(a):
  g = {}
  for i in a:
    if i in g:
      g[i] +=1
    else:
      g[i] =1
  return g

print(countElement(sample_list))