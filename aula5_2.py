largest = None
smallest = None
while True:
    num = input("Enter a number: ")

    if num == "done":
        print("Maximum is", largest)
        print('Minimum is', smallest)
        break
    try:
        inum = int(num)
    except:
        print('Invalid input')
        continue
    if largest == None:
        largest = inum
        smallest = inum
    if inum > largest:
        largest = inum
    if inum < smallest:
        smallest = inum