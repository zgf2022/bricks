import decimal

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