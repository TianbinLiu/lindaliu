def findprimes(min, max):
    for Number in range(min, max + 1):
        count = 0
        for i in range(2, (Number // 2 + 1)):
            if (Number % i == 0):
                count = count + 1
                break
        if (count == 0 and Number != 1):
            print(" %d" % Number, end='  ')
    print()


def primes():
    minimum = int(input(" Enter the Minimum Value for Primes: "))
    maximum = int(input(" Enter the Maximum Value for Primes: "))
    findprimes(minimum, maximum)

def primesTester():
    minimum = 10
    maximum = 100
    print("minimum = 10 | maximum = 100 | primes: ", end="")
    findprimes(minimum, maximum)
    print()
    minimum = 5
    maximum = 88
    print("minimum = 5 | maximum = 88 | primes: ", end="")
    findprimes(minimum, maximum)
    print()
    minimum = 66
    maximum = 123
    print("minimum = 66 | maximum = 123 | primes: ", end="")
    findprimes(minimum, maximum)

if __name__ == "__main__":
    primes()
    primesTester()