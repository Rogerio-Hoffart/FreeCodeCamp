while True:
    score = input("Enter Score: ")
    try:
        fscore = float(score)
    except:
        print('Invalid Score')
        continue
    if fscore >= 0 and fscore <= 1.0:
        if fscore < 0.6:
            print('F')
            break
        elif fscore < 0.7:
            print('D')
            break
        elif fscore < 0.8:
            print('C')
            break
        elif fscore < 0.9:
            print('B')
            break
        elif fscore <= 1.0:
            print('A')
            break
    print('Out of Range')
    continue
