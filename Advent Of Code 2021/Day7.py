def path(Tab, pos):
  fuel = 0
  for i in range(len(Tab)):
    if Tab[i] != 0:
      fuel += abs((pos - i)*Tab[i])
  return fuel

def s(num):
  n = 0
  for i in range(num):
    n += (i+1)
  return n

def fixedPath(Tab, pos):
  fuel = 0
  for i in range(len(Tab)):
    if Tab[i] != 0:
      fuel += s(abs(pos - i))*Tab[i]

  return fuel


def AoC7(input, biggest):
  helpTab = input.sort()
  Tab = []
  for i in range(biggest+1):
    Tab += [0]
  for i in input:
    Tab[i] += 1
  leastFuel = path(Tab, 0) #1st solution
  #leastFuel = fixedPath(Tab, 0) #2nd solution
  for i in range(len(Tab)):
    f = path(Tab, i) #1st soltuion
    #f = fixedPath(Tab, i) #2nd solution
    if f < leastFuel:
      leastFuel = f
  return leastFuel
#348996 1st solution
#98231647 2nd solution (takes ~2mins to calculate)

def main():
  with open('7.txt') as file:
    input = file.read().split(',')
    biggest = 0
    for i in range(len(input)):
      input[i] = int(input[i])
      if input[i] > biggest:
        biggest = input[i]

    print(AoC7(input, biggest))
    #print(AoC31(input))

main()
