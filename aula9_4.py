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
    print(lineList)
    email = lineList[1]
    '''ipos = line.find('m')
    #print(ipos)
    start = line[ipos + 2:]
    #print(start)
    midlle = line.find('@')
    #print(midlle)
    stop = line.find(' ', midlle )
    #print(stop)
    email = line[ipos + 2:stop]
    email = email.lstrip()
    #print(email)'''
    di[email] = di.get(email, 0) + 1
    #print(di)
largest = -1
theEmail = None
for k,v in di.items():
    if largest < v:
        largest = v
        theEmail = k
print(theEmail, largest)



