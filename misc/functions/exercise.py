class TestClass:
    def __init__(self):
        print("NEW CLASS")

def my_exercise(sum_or_subtract, filename):
    '''
    Sum or Average all numbers in the file filename
    :param str sum_or_subtract: A string "sum" or "subtract"
    :param filename
    :return: The float of the sum/subtraction of all numbers from 0
    '''
    total = 0
    
    myFile = open(filename, 'r')
    if sum_or_subtract == 'sum':
        for line in myFile:
            total += float(line.strip())
        myFile.close()
    else:
        for line in myFile:
            total -= float(line.strip())
        myFile.close()

    return total
