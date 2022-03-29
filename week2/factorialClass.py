class Factorial:
    def findFact(self, n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f

def factorial():
  print("Enter a Number: ", end="")
  num = int(input())
  ob = Factorial()
  print("\nThe factorial of", num, "is =", ob.findFact(num))

if __name__ == "__main__":
    factorial()