import os ,matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np

def probCount(num):
    return (5-num)/10
def rCount(num):
    return num/100

def main():
    textfile = open("C:\\STAT.txt")
    get_details = textfile.readlines()
    textfile.close()
    row = len(get_details)

    one, two, three, four = 0, 0 , 0 ,0
    for i in range(row):
        one += get_details[i].count("1")
        two += get_details[i].count("2")
        three += get_details[i].count("3")
        four += get_details[i].count("4")

    rfOne = rCount(one)
    rfTwo = rCount(two)
    rfThree = rCount(three)
    rfFour = rCount(four)

    pOne = probCount(1)
    pTwo = probCount(2)
    pThree = probCount(3)
    pFour = probCount(4)
    print(tabulate([["1",one,rfOne, pOne],["2", two, rfTwo, pTwo],["3", three,rfThree,pThree],["4",four, rfFour, pFour]],headers = ["X", "No of X Occurs", "Relative Frequency of X", "Probability of {X=x}, f(x)"], tablefmt="grid"))

#GRAPH CODE HERE
    n = 4
    rel = (rfOne-pOne, rfTwo-pTwo, rfThree-pThree, rfFour-pFour)
    prob = (pOne, pTwo, pThree, pFour)

    ind = np.arange(n)
    width = .4

    pl1 = plt.bar(ind,prob,width)
    pl2 = plt.bar(ind, rel, width, bottom=prob)
    plt.ylabel("h(x), f(x)")
    plt.title("Probability & Relative frequency histogram.")
    plt.xticks(ind,("1", "2", "3", "4"))
    plt.yticks(np.arange(0, 0.50, 0.05))
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()