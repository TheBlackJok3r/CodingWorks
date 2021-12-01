def AoC1(input):
  currVal = int(input[0])
  increased = 0
  for i in input:
    v = int(i)
    if v > currVal:
      increased += 1
    currVal = v
  return increased

def AoC11(input):
  currVal = int(input[0]) + int(input[1]) + int(input[2])
  increased = 0
  i = 1
  while i < len(input)-2:
    v = int(input[i]) + int(input[i+1]) + int(input[i+2])
    if v > currVal:
      increased += 1
    currVal = v
    i += 1
  return increased

def main():
  with open('1.txt') as file:
    input = file.read().split('\n')
    print(AoC1(input))
    print(AoC11(input))

main()
