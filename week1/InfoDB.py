# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
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

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["GroupName"]) 
    print("\t", "DebutDate: ", end="") 
    print(InfoDb[n]["DebutDate"]) 
# using comma puts space between values
    print("\t", "Members: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Members"]))  # join allows printing a string list with separator
    print()

def for_loop():
  for n in range(len(InfoDb)):
    print_data(n)

# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop0(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def recursive_loop0(n):
  if n < len(InfoDb):
      print_data(n)
      recursive_loop0(n + 1)
  return # exit condition

def while_loop():
  while_loop0(0)

def recursive_loop():
  recursive_loop0(0)

if __name__ == "__main__":
    for_loop()
    while_loop()
    recursive_loop()