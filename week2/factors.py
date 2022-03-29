def findFactors(number):
    print("Factors of a Given Number {0} are:".format(number))
    for value in range(1, number + 1):
        if number % value == 0:
            print("{0}".format(value), end=" ")
    print()

def factors():
    num = int(input("Enter any Number to find its factors: "))
    findFactors(num)

def factorsTester():
    num = 999
    findFactors(num)
    print()
    num = 555
    findFactors(num)
    print()
    num = 123
    findFactors(num)

if __name__ == "__main__":
    factors()
    factorsTester()