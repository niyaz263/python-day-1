 list_1 = [3,4,4,5,5,6,6]
 first_sum = sum(list_1)
 second_sum = sum(set(list_1))*2
 res = second_sum-first_sum
 print(res)

 # factorial

 n=int(input("Enter a number : "))
 fact=1
 for i in range(n,1,-1):
     fact=fact*i
 print(fact)

list1=[1,2,3,4,5,6,7,8,9,10]
 target=7
 start=0
 end=len(list1)-1
 index=-1
 while(start<=end):
     middle = (start+end)//2
     if list1[middle]==target:
         index=(middle)
     elif list1[middle]>target:
         end=middle-1
     elif list1[middle]<target:
         start=middle+1
        
 print(start)

# stars
 n=int(input("Enter the value : "))
 for i in range(1,n+1):
     print("* "*i)

# for reverse

 n=int(input("Enter the value : "))
 for i in range(n,0,-1):
     print("ns " *i)

# for numbers
 n=int(input("Enter a value : "))
 for i in range(1,n+1):
     str1=""
     for j in range(1,i+1):
         str1=str1+str(j)+" "
         print(str1)

 n=int(input("Enter a value : "))
 for i in range(n,0,-1):
     str1=""
     for j in range(1,i+1):
         str1=str1+str(j)+" "
     print(str1)
n = int(input("Value: "))
 for i in range(1,n+1):
     print(" "*(n-i)+"* "*i)

 n=int(input("Value: "))
 for i in range(1,n+1):
     if i==1 or i==n:
         print("* "*i)
     else:
         print("*"+" "*(2*i-3)+"*")    

