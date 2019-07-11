import math
import time
import decimal
import os
import random

decimal.getcontext().prec = 200

runsize = 250000

x = 0 
y = 0 
z = 0 

face1 = decimal.Decimal(int(0))
face2 = decimal.Decimal(int(0))
face3 = decimal.Decimal(int(0))

runcount = 0 

diagonal = decimal.Decimal(int(0))

eulerfound = 0
perfectfound = 0

totalboxes = 0
msgprint = 0

while 1 > 0:
  Filehandle = open("merged.txt","r")
  Filecontents = Filehandle.readlines()
  linenum = random.randint(1, len(Filecontents) - 1)
  Linecontents = Filecontents[linenum].split()
  x = int(Linecontents[1])
  y = int(Linecontents[3])
  z = 0
  Filehandle.close()
  runsize = (x + y) * 5
  while z < runsize:
    totalboxes += 1
    z += 1
    msgprint += 1
    if msgprint > 1000:
      msgprint = 0
      os.system('cls')
      print ("boxes: " + str(totalboxes) + " Euler Bricks found: " + str(eulerfound) + " Perfect Cuboids found: " + str(perfectfound))
      print ("X: " + str(x) + " y: " + str(y) + " z: " + str(z))
    face2 = decimal.Decimal((x * x) + (z * z))
    face2 = face2.sqrt()
    face3 = decimal.Decimal((y * y) + (z * z))
    face3 = face3.sqrt()
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
    if face2 %1 == 0 and face3 %1 == 0:
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
  
    



