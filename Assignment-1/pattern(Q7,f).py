n=int(input())
for i in range(1,n):
  for j in range(1,n-i):
    print(" ",end="")
  for k in range(1,i+1):
      print("*")
  print()
  for i in range(n,1):
      for j in range(1,i+1):
          print(" ",end="")
        for k in range(1,i+1):
            print("*")
        print()
