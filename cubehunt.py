import math
import time
import decimal
import os

def pythag ( a , b):
  face = decimal.Decimal((a * a) + (b * b))
  face = face.sqrt()
  return face

def checktriangle(a, v1, v2 ):
  if a %1 == 0:
          file = open('2.txt', 'a')
          file.write('\n')
          file.write(str(v1) + ", " + str(v2))
          file.close()

decimal.getcontext().prec = 50
print ("x offset ")
xoffset = int(input())
print ("y offset ")
yoffset = int(input())
print ("z offset ")
zoffset = int(input())
print ("z runsize ")
runsize = int(input())

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
  x = xoffset
  while x < runcount + xoffset:
    x += 1
    y = yoffset
    while y < runcount + yoffset:
      y += 1
      z = zoffset
      #os.system('cls')
      print ("boxes: " + str(totalboxes) + " Euler Bricks found: " + str(eulerfound) + " Perfect Cuboids found: " + str(perfectfound))
      print ("X: " + str(x) + " y: " + str(y) + " z: " + str(z))
        
      while z < runsize + zoffset:
        totalboxes += 1
        z += 1
        
        face1 = pythag(x, y)
        face2 = pythag(x,z)
        face3 = pythag(y,z)
        
        checktriangle(face1, x, y)
        checktriangle(face2, x, z)
        checktriangle(face3, y, z)
        
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
        
          
      


