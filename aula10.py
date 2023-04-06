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
print(di)

x = sorted(di.items())
print(x[:6])

tmp = list()
for k,v in di.items():
    #print(k,v)
    newt = (v,k)
    #print(newt)
    tmp.append(newt)

#print('Flipped', tmp)
tmp = sorted(tmp, reverse=True)
#print('Sorted', tmp)
for v,k in tmp[:5]:
    print(k,v)