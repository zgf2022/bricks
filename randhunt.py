import math
import time
import decimal
import os
import random

decimal.getcontext().prec = 200
#print ("x offset ")
#xoffset = int(input())
#print ("y offset ")
#yoffset = int(input())
#print ("z offset ")
#zoffset = int(input())
#print ("z runsize ")
#runsize = int(input())
xoffset = random.randint(1,10000000000)
yoffset = random.randint(1,10000000000)
zoffset = random.randint(1,10000000000)
runsize = 100000

x = 0 + xoffset
y = 0 + yoffset
z = 0 + zoffset

face1 = decimal.Decimal(int(0))
face2 = decimal.Decimal(int(0))
face3 = decimal.Decimal(int(0))

runcount = 0 

diagonal = decimal.Decimal(int(0))

eulerfound = 0
perfectfound = 0

totalboxes = 0

while True:
  runcount += runsize
  xoffset = random.randint(1,10000000000)
  yoffset = random.randint(1,10000000000)
  zoffset = random.randint(1,10000000000)
  x = xoffset
  while x < runsize + xoffset:
    x += 1
    y = yoffset
    while y < runsize + yoffset:
      y += 1
      z = zoffset
      os.system('cls')
      print ("boxes: " + str(totalboxes) + " Euler Bricks found: " + str(eulerfound) + " Perfect Cuboids found: " + str(perfectfound))
      print ("X: " + str(x) + " y: " + str(y) + " z: " + str(z))
        
      while z < runsize + zoffset:
        totalboxes += 1
        z += 1
        face1 = decimal.Decimal((x * x) + (y * y))
        face1 = face1.sqrt()
        face2 = decimal.Decimal((x * x) + (z * z))
        face2 = face2.sqrt()
        face3 = decimal.Decimal((y * y) + (z * z))
        face3 = face3.sqrt()
        if face1 %1 == 0:
          file = open('face1.txt', 'a')
          file.write('\n')
          file.write('x: ' + str(x)+ " y: " + str(y))
          file.close()
        if face2 %1 == 0:
          file = open('face2.txt', 'a')
          file.write('\n')
          file.write('x: ' + str(x)+ " z: " + str(z))
          file.close()
        if face3 %1 == 0:
          file = open('face3.txt', 'a')
          file.write('\n')
          file.write('y: ' + str(y)+ " z: " + str(z))
          file.close()
        if face1 %1 == 0 and face2 %1 == 0 and face3 %1 == 0:
          file = open('brick.txt', 'a')
          file.write('\n')
          file.write('x: ' + str(x)+ " y: " + str(y) + " z:  " + str(z))
          file.close()
          eulerfound += 1
          diagonal = decimal.Decimal((x * x) + (y * y) + (z * z))
          diagonal = diagonal.sqrt()
          if diagonal % 1 == 0:
            print (diagonal)
            perfectfound += 1
            file = open('perfectcube.txt', 'a')
            file.write('\n')
            file.write('x: ' + str(x)+ " y: " + str(y) + " z:  " + str(z))
            file.close()


