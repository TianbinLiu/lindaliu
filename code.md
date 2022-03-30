---
# Code Snippets
# TT1
## Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
## List with dictionary records placed in a list  
InfoDb.append({  
               "GroupName": "Tomorrow X Together",   
               "DebutDate": "March 4, 2019",   
               "Members":["Yeonjun","Soobin","Beomgyu ","Taehyun ","Huening Kai"]  
              }) 

InfoDb.append({  
               "GroupName": "Blackpink",   
               "DebutDate": "August 8, 2016",   
               "Members":["Lisa","Jennie","Rose ","Jisoo "]  
              })  

## given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["GroupName"]) 
    print("\t", "DebutDate: ", end="") 
    print(InfoDb[n]["DebutDate"]) 
## using comma puts space between values
    print("\t", "Members: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Members"]))  # join allows printing a string list with separator
    print()



# TT2
## Factorial Class
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

## Function to find the Factors of a Number
def findFactors(number):
    print("Factors of a Given Number {0} are:".format(number))
    for value in range(1, number + 1):
        if number % value == 0:
            print("{0}".format(value), end=" ")
    print()

def factors():
    print("hello from factors")
    num = int(input("Enter any Number to find its factors: "))
    findFactors(num)

if __name__ == "__main__":
    factors()
