def helper(s):
    A = []
    last = ''
    result = True
    for i in s:
        if last == i:
            continue
        elif last != i and i not in A:
            A.append(i)
            last = i
        else:
            result = False
            break
    return result


def barrels(pattern, acc=0):
    if helper(pattern):
        return f'The result pattern is: {pattern}'
    else:
        pat = pattern[0:acc] + pattern[acc+3:len(pattern)] + pattern[acc:acc+3]
        if acc < len(pattern)-4:
            return f'{pat} \n {barrels(pat, acc+1)}'
        else:
            return f'{pat} \n {barrels(pat, 0)}'


def main():
    with open('Python/coloredBarrels.txt') as file:
        text = file.read().split(' ')
        try:
            print(barrels(text))
        except:
            print('There is no possible sorting result of this data')


main()
