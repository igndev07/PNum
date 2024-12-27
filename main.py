#pre assuming 2,3 as prime numbers
#you can edit the range :) 

x = {}
for i in range(4,10000):  
  x[i] = "None"
  y=2
  while y<i:
    if i%y == 0:
      x[i] = "one"
      y+=1
    else:
      y+=1
      continue


print("The prime numbers are:")
for xx in x:
  if x[xx] == "None":
    print(xx)
