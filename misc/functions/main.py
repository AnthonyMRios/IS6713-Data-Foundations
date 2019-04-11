# You should NOT edit this file!
from exercise import *

from subdir.newFunc import printHello

def main():
    newC = TestClass()
    printHello()
    arg1 = 'sum'
    print("SUM: {}".format(my_exercise("sum", './data/numbers.txt')))

    arg1 = 'subtract'
    print("SUBTRACTION: {}".format(my_exercise("subtract", './data/numbers.txt')))

if __name__ == '__main__':
    main()
