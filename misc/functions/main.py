from exercise import *

def main():
    my_numbers = []
    with open('./data/numbers.txt') as in_file:
        for number in in_file:
            my_numbers.append(int(number))

    arg1 = 'sum'
    print("SUM: {}".format(my_exercise(arg1, my_numbers)))

    arg1 = 'subtract'
    print("SUBTRACTION: {}".format(my_exercise(arg1, my_numbers)))

if __name__ == '__main__':
    main()
