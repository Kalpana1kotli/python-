# pgm to print fibonacci sequence of length (10) 
 n = int(input("Enter the value of n:")) 
 a = 0 
 b = 1 
 count = 0 
  
 if n <= 0: 
     print("Please enter a valid integer") 
 elif n == 1: 
     print("Fibonacci series upto 1") 
     print(a) 
 else: 
     print("Fibonacci sequence") 
     while(count < n): 
         print(a, end = " ") 
         c = a + b 
         a = b 
         b = c 
         count += 1
