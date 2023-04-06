han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[1])

fhan = open('romeo.txt')
allWords = ['']
for lineOne in fhan:
    lineOne = lineOne.rstrip()
    words = lineOne.split()
    for item in words:
        for check in allWords:
            if check == item:
                allWords.remove(item)
        allWords.append(item)
        #print(allWords)
allWords.sort()
allWords.remove('')
print(allWords)
