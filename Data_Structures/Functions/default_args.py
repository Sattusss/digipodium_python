# function can have  default parameters if u want
# defaults params are added after required params
def add(a,b,c=0,d=0):
    return a+b+c+d


if __name__== "__main__":
   out = add(20,20)
   print(out)
   out = add(20,20,20)
   print(out)
   out = add(20,20,10,100)
   print(out)

