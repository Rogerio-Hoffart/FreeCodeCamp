fhan = open('romeo.txt')
allWords = []
for lineOne in fhan:
    lineOne = lineOne.rstrip()
    words = lineOne.split()
    for item in words:
        repeat = False
        if allWords == []:
            allWords.append(item)
            continue
        for check in allWords:
            if check == item:
                repeat = True
                continue
        if repeat == True:
            continue
        allWords.append(item)
        #print(allWords)
allWords.sort()
#allWords.remove('')
print(allWords)

