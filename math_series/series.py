fibonacci_Arr=[]
lucas_Arr=[]
def fibonacci(n):
    a = 0
    b = 1
    # print("*************This is fibonacci numbers*************")
    if n == 1: # it will print a and b without it 
        # print(a)
        fibonacci_Arr.append(a)
        # print(fibonacci_Arr)
        # return fibonacci_Arr 
        for i in fibonacci_Arr:
            # print(i)
            return i
    elif n < 0: # To solve the negative numbers
        print("Please enter positive numbers only")
    else:
        # print(a)
        # print(b)
        fibonacci_Arr.append(a)
        fibonacci_Arr.append(b)
        for i in range(2,n):
            c = a + b
            a = b 
            b = c
            # print(c)
            fibonacci_Arr.append(c)
    # print(fibonacci_Arr)
    for i in fibonacci_Arr:
        return i

# fibonacci(7) 
def lucas(n):
    a = 2
    b = 1
    print("*************This is lucas numbers*************")
    if n == 1:
        # print(a)
        lucas_Arr.append(a)
        print(lucas_Arr)
        return lucas_Arr 
    elif n < 0:
        print("Please enter positive numbers only")
    else:
        # print(a)
        # print(b)
        lucas_Arr.append(a)
        lucas_Arr.append(b)
        for i in range(2,n):
            c = a + b
            a = b 
            b = c
            # print(c)
            lucas_Arr.append(c)
    print(lucas_Arr)
    return lucas_Arr 
# lucas(1) 

def sum_series(n, first=0, second=1):
  
    if first == 0 and second == 1:  #Calling with no optional parameters will produce numbers from the fibonacci series
        return fibonacci(n)
    elif first == 2 and second == 1: #Calling with the optional arguments 2 and 1 will produce values from the lucas numbers.
        return lucas(n)
    else :
        # return sum_series(n - 1, first, second) + sum_series(n - 2, first, second)
        return fibonacci(n) + lucas(first)
      
# sum_series(8,6,3)
