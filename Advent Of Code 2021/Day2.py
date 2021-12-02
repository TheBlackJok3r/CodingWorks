def AoC2(input):
  x = 0
  y = 0
  for i in input:
    i = i.split(' ')
    if i[0] == 'forward':
      x += int(i[1])
    elif i[0] == 'down':
      y += int(i[1])
    elif i[0] == 'up':
      y -= int(i[1])
        
  return x*y

def AoC21(input):
  x = 0
  depth = 0
  aim = 0
  for i in input:
    i = i.split(' ')
    if i[0] == 'forward':
      x += int(i[1])
      depth += aim * int(i[1])
    elif i[0] == 'down':
      aim += int(i[1])
    elif i[0] == 'up':
      aim -= int(i[1])
        
  return x*depth

def main():
  with open('2.txt') as file:
    input = file.read().split('\n')
    print(AoC2(input))
    print(AoC21(input))

main()
