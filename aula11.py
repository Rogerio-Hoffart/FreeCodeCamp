import re
hand = open('regex_sum_1689703.txt')
numList = list()
total = 0
for line in hand:
    line = line.rstrip()
    checkNumber = re.findall('([0-9]+)', line)
    if len(checkNumber) == 0: continue
    for num in checkNumber:
        numInt = int(num)
        total += numInt
print(total)

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
