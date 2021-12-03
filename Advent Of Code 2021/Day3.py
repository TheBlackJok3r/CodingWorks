def AoC3(input):
  gamma = ''
  epsilon = ''
  for i in range(len(input[0])):
    zeros = 0
    ones = 0
    for j in input:
      if j[i] == '0':
        zeros += 1
      else:
        ones += 1

    if ones > zeros:
      gamma += '1'
    else:
      gamma += '0'
  
  for k in gamma:
    if k == '0':
      epsilon += '1'
    else:
      epsilon += '0'
  
  return int(gamma, 2) * int(epsilon, 2)
#3969000

def AoC31(input):
  oxygen = helper(input, True)
  co2 = helper(input, False)
  return int(oxygen, 2) * int(co2, 2)

def helper(inp, most):
  for i in range(len(inp[0])):
    if len(inp) == 1:
      break

    zeros = 0
    ones = 0
    z = []
    o = [] 
    for j in inp:
      if j[i] == '0':
        zeros += 1
        z.append(j)
      else:
        ones += 1
        o.append(j)
    
    if most:
      if ones >= zeros:
        inp = o
      else:
        inp = z

    else:
      if ones >= zeros:
        inp = z
      else:
        inp = o

  return inp[0]
#4267809



def main():
  with open('3.txt') as file:
    input = file.read().split('\n')
    print(AoC3(input))
    print(AoC31(input))

main()
