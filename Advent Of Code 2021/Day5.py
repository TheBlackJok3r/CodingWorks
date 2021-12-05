def AoC5(input):
  biggestX = 0
  biggestY = 0
  for i in input:
    for j in i:
      if j[0] > biggestX:
        biggestX = j[0]
      if j[1] > biggestY:
        biggestY = j[1]
  Tab = []
  for i in range(biggestY+1):
    helpTab = []
    for j in range(biggestX+1):
      helpTab += ['.']
    Tab += [helpTab]

  for i in input:
    x1 = i[0][0]
    x2 = i[1][0]
    y1 = i[0][1]
    y2 = i[1][1]
    if x1 == x2 or y1 == y2:
      if x1 > x2:
        while x1 >= x2:
          if Tab[y1][x2] == '.':
            Tab[y1][x2] = 1
          else:
            Tab[y1][x2] += 1
          x2 += 1

      elif x1 < x2:
        while x1 <= x2:
          if Tab[y1][x1] == '.':
            Tab[y1][x1] = 1
          else:
            Tab[y1][x1] += 1
          x1 += 1

      elif y1 > y2:
        while y1 >= y2:
          if Tab[y2][x1] == '.':
            Tab[y2][x1] = 1
          else:
            Tab[y2][x1] += 1
          y2 += 1
      
      elif y1 < y2:
        while y1 <= y2:
          if Tab[y1][x1] == '.':
            Tab[y1][x1] = 1
          else:
            Tab[y1][x1] += 1
          y1 += 1

  count = 0
  for i in Tab:
    for j in i:
      try:
        if j >= 2:
          count += 1
      except:
        pass
  return count
#5576

def AoC51(input):
  biggestX = 0
  biggestY = 0
  for i in input:
    for j in i:
      if j[0] > biggestX:
        biggestX = j[0]
      if j[1] > biggestY:
        biggestY = j[1]
  Tab = []
  for i in range(biggestY+1):
    helpTab = []
    for j in range(biggestX+1):
      helpTab += ['.']
    Tab += [helpTab]

  for i in input:
    x1 = i[0][0]
    x2 = i[1][0]
    y1 = i[0][1]
    y2 = i[1][1]
    if x1 == x2 or y1 == y2:
      if x1 > x2:
        while x1 >= x2:
          if Tab[y1][x2] == '.':
            Tab[y1][x2] = 1
          else:
            Tab[y1][x2] += 1
          x2 += 1

      elif x1 < x2:
        while x1 <= x2:
          if Tab[y1][x1] == '.':
            Tab[y1][x1] = 1
          else:
            Tab[y1][x1] += 1
          x1 += 1

      elif y1 > y2:
        while y1 >= y2:
          if Tab[y2][x1] == '.':
            Tab[y2][x1] = 1
          else:
            Tab[y2][x1] += 1
          y2 += 1
      
      elif y1 < y2:
        while y1 <= y2:
          if Tab[y1][x1] == '.':
            Tab[y1][x1] = 1
          else:
            Tab[y1][x1] += 1
          y1 += 1

    else:
      if x1 > x2 and y1 > y2:
        while x1 >= x2:
          if Tab[y2][x2] == '.':
            Tab[y2][x2] = 1
          else:
            Tab[y2][x2] += 1

          y2 += 1
          x2 += 1

      elif x1 > x2 and y1 < y2:
        while x1 >= x2:
          if Tab[y2][x2] == '.':
            Tab[y2][x2] = 1
          else:
            Tab[y2][x2] += 1

          y2 -= 1
          x2 += 1

      elif x1 < x2 and y1 > y2:
        while x1 <= x2:
          if Tab[y1][x1] == '.':
            Tab[y1][x1] = 1
          else:
            Tab[y1][x1] += 1

          y1 -= 1
          x1 += 1

      elif x1 < x2 and y1 < y2:
        while x1 <= x2:
          if Tab[y1][x1] == '.':
            Tab[y1][x1] = 1
          else:
            Tab[y1][x1] += 1

          y1 += 1
          x1 += 1 

  count = 0
  for i in Tab:
    for j in i:
      try:
        if j >= 2:
          count += 1
      except:
        pass
  return count
#18144

def main():
  with open('5.txt') as file:
    input = file.read().split('\n')

    for i in range(len(input)):
      input[i] = input[i].split(' -> ')
      input[i][0] = input[i][0].split(',')
      input[i][1] = input[i][1].split(',')

      input[i][0][0] = int(input[i][0][0])
      input[i][0][1] = int(input[i][0][1])
      input[i][1][0] = int(input[i][1][0])
      input[i][1][1] = int(input[i][1][1])

    #print(AoC5(input))
    print(AoC51(input))

main()
