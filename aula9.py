fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)
    for w in wds:
        #idiom retrieve/cerate/update counter
        di[w] = di.get(w,0) + 1
        #print(w, di[w])
#print(di)
#Now we want to find the most common word
largest = -1
theWord = None
for k,v in di.items():
    #print(k,v)
    if largest < v:
        largest = v #capture/remenber value
        theWord = k #capture/remenber Key
print('Done:', theWord, largest)
