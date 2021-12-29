for num in range(101,201,1):
  if all(num%i!=0 for i in range(2,num)):
    print(num)
