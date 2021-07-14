from sys import argv as ag


def addTwoNumbers(number1, number2):
    print("Program already executed")
    result = number1 + number2
    return result


answer = False

def isEven (aNumber):
    if(aNumber%2 == 0):
        return True
        #print("It is even")
    else:
        return False
        #print("It is an odd")

if __name__ == "__main__":
    #print(f'La suma de dos números = {addTwoNumbers(int(ag[1]), int(ag[2]))}')
    n1 =int(input('Número 1:\t'))
    n2 =int(input('Número 2:\t'))

    #print(f'La suma de dos números = { addTwoNumbers(n1,n2)}')

    if(isEven (addTwoNumbers(n1,n2))):
        print(f'N1: "{n1}" and N2:"{n2}" are lucky numbers')    
    else:
        print(f'N1: "{n1}" and N2:"{n2}" arent lucky numbers')