
nh = input("Enter the hours worked: ")
nr = input("Enter the Rate: ")
try:
    nnh = float(nh)
    nnr = float(nr)
except:
    print("Error! Please enter a numeric input.")
    quit()

def computepay(h,r):
        if h > 40 :
            np = ((40 * r) + (h-40) * r * 1.5)
        else: np = h * r
        return np

print("You have to pay:", computepay(nnh, nnr))