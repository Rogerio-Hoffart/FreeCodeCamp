name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
di = dict()
for line in handle:
    if not line.startswith("From"):
        continue
    if not line.find('0') > 10:
        continue
    lineList = line.split()
    #print(lineList)
    hour = lineList[5]
    x = hour.find(':')
    hour = hour[:x]
    di[hour] = di.get(hour, 0) + 1
    #print(di)

tmp = list()
for k, v in di.items():
    tempt = (k,v)
    tmp.append(tempt)

tmp = sorted(tmp)
for k in tmp:
    print(k[0], k[1])

