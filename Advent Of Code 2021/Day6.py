def rotate(l, n):
    return l[-n:] + l[:-n]

def sum(l):
  count = 0
  for i in l:
    count += i
  return count

def AoC6(input, days):
  fishes = [0,0,0,0,0,0,0,0,0]
  for i in input:
    fishes[i] += 1

  for i in range(days):
    fishes[7] += fishes[0]
    fishes = rotate(fishes, -1)
  
  return sum(fishes)
#376194 first solution

def main():
  with open('6.txt') as file:
    input = file.read().split(',')
    for i in range(len(input)):
      input[i] = int(input[i])
    print(AoC6(input, 80))
    print(AoC6(input, 256)) #input already gets extended by first 80 days

main()
