 n = input("Enter a number: ")
 s = 0
 power = len(n)
 for i in n:
     s += int(i) ** power
 if s == int(n):
     print("Armstrong")
 else:
     print("Not Armstrong")

 # Print Armstrong numbers in a given range
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for num in range(start, end + 1):
    power = len(str(num))
    s = sum(int(digit) ** power for digit in str(num))
    if s == num:    
        print(num)


 def is_prime(m):
     is_prime = True
     if m <= 1:
         is_prime = False
     else:
         for i in range(2,int(m**0.5) + 1):
             if m % i == 0:
                 is_prime = False
                 break
     if is_prime:
         print(m)
 m=int(input())
 for i in range(1, m + 1):

      is_prime(i)
