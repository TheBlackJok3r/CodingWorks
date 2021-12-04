def rows(bin, picked):
  for i in range(len(bin)):
    count = 0
    for j in range(len(bin[i])):
      if bin[i][j] in picked:
        count += 1
    if count == 5:
      return True

def columns(bin, picked):
  for i in range(len(bin)):
    count = 0
    for j in range(len(bin[i])):
      if bin[j][i] in picked:
        count += 1
    if count == 5:
      return True

def sum(bingo, picked):
  s = 0
  for i in range(len(bingo)):
    for j in range(len(bingo[i])):
      if not (bingo[i][j] in picked):
        s += int(bingo[i][j])
  return s

def AoC4(bingos, numbers):
  picked = []
  for w in numbers:
    picked += [w]
    for k in bingos:
      if rows(k, picked) or columns(k, picked):
        return sum(k, picked) * int(w)

  return 0
#45031


def AoC41(bingos, numbers):
  picked = []
  saved = []
  for w in numbers:
    saved = bingos
    picked += [w]
    for k in bingos:
      if len(saved) == 1 and (rows(k, picked) or columns(k, picked)):
        print(saved, w)
        return sum(saved[0], picked) * int(w)
      elif rows(k, picked) or columns(k, picked):
        saved.remove(k)

  return 0
#2568

def main():
  with open('4.txt') as file:
    input = file.read().split('\n\n')
    nums = input[0]
    bingos = input[1:]

    for k in range(len(bingos)):
      bingos[k] = bingos[k].split('\n')
      for i in range(len(bingos[k])):
        bingos[k][i] = bingos[k][i].split(' ')
        try:
          bingos[k][i].remove('')
          bingos[k][i].remove('')
          bingos[k][i].remove('')
          bingos[k][i].remove('')
          bingos[k][i].remove('')
        except:
          pass

    print(AoC4(bingos, nums.split(',')))
    print(AoC41(bingos, nums.split(',')))

main()
