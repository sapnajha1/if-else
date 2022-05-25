#...............LOOP QUESTIONS.....................
# i=0
# while i<=10:
#     print(i,"is even number")
#     i+=2
# # ..............................................

#.............ODD NUMBER..........................
# i=0
# while i<=10:
#     if i%2==1:
#       print(i,"is odd number")
#     i+=1

# count = 0
# while count<=20:
#   if count%2==1:
#     print(count, 'is odd')
#   count+=1
#...................................................

#.................NATURAL NUMBER...................

# i=1
# while i<=10:
#   print(i,"is natural number")
#   i+=1
#...................................................

#...............WHOLE NUMBER.............................

# i=0
# while i<=10:
#   print(i,"is whole number")
#   i+=1
#........................................................

#..............10 INTEGER AND THEIR SQUARE...............
# i=0
# while i<=10:
#   print(i,i*2)
#   i+=1
#..............................................................

#.........horizantal ascending order number...............................

# i=10
# while i<=300:
#   print(i,end=" ")
#   i+=10

#...........................................................

#........horizantal desending order number..................

# i=105
# while i>=7:
#   print(i,end=" ")
#   i-=7
#.............................................................................

#......NATURAL NUMBER IN REVERSE.............................................

# i=10
# while i>=0:
#   print(i)
#   i-=1

#...............................................................................


#................sum of natural number........................................
# sum=0
# i=1
# while i<=10:
#   sum+=i
#   i+=1
#   print(sum)
#...................................................................................

#................sum of 10 even nu.................................................


# i=0
# sum=0
# while i<=10:
#     if i%2==0:
#      sum+=1
#     i+=1
# print(sum)
#.........................................................................................


#.............TABLE...............................................
# i=1
# a=int(input("enter number"))
# while i<=10:
#   print(a*i)
#   i+=1
#......................................................................

#....EVEN NUMBER BETWEEN TWO NUMBER FOMR USER..................................

# num1=int(input("enter first number"))
# num2=int(input("enter second number"))
# while num1<num2:
#   if (num1%2==0):
#     print(num1,"is even nu.")
#   num1+=1
#........................................................................

#..................prime number or not......................................................

# num=int(input("enter a number"))
# i=1
# while i ==1:
#   if num%2!=0 or num%3!=0:
#     print(num,"is prime number")
#   else:
#     print(num,"is not prime number")
#   i+=1
#..............................................................................................

#................REVERSE NUMBER...............................................................

# a=int(input("enter a number "))
# i=0
# while i<=0:
#     b=a%10
#     print(b,end=" ")
#     a=a//10
#     break
#..................................................................................................
# 
# .......................TABLE..................................................................

# i=1
# a=int(input("enter a number"))
# while i<=10:
#     print(a*i)
#     i+=1
#.............................................................................................


#..............find the product of digit accepted by user...................................
# num=int(input("enter a number"))
# multi=1
# i=1
# while i<=num:
#     multi*=i
#     i+=1
# print(multi)
#..................................................................................


#...............REVERSE THE NUMBER.......................................................

# num=int(input("enter a number"))
# i=1
# while i<=num:
#     a=num%10
#     print(a,end="")
#     num=num//10
#.........................................................................................


#..............converet number in word form............................................

# num=int(input("enter a number  "))
# a=["one, two,three,four,five,six,seven,eight,nine zero"]
# b=["1,2,3,4,5,6,7,8,9,0"]
# i=0
# while i<num:
#     if "1" in b:
#         print("one")
#     elif "2" in b:
#         print("two")
#     elif "3" in b:
#         print("three")
#     elif "4" in b:
#         print("four")
#     elif "5" in b:
#         print("five")
#     elif "6" in b:
#         print("six")
#     elif "7" in b:
#         print("seven")
#     elif "8" in b:
#         print("eight")
#     elif "9" in b:
#         print("nine")
#     elif "0" in b:
#         print("zero")
#.....................................DOUBT...................................................

#.15................FIBONNACI SERIES.....TWO TYPES......................................
# n=int(input("enter a number "))
# i=0
# x=0
# y=1 #x and y is compulsary (0 1)
# z=0 #z is 0 we take bcoz of no effect on 
# while i<=n:
#     if z<=i:
#         print()

#.....................DOUBT..................................................


#.16.....................ARMSTRONG NUMBER.................................................



# n=int(input("enter a number"))
# n1=n
# length=len(str(n))

# sum=0
# while n>0:
#     digit=n%10
#     sum+=(digit**length)
#     n//=10
# print(sum)
   
    
# if n1==sum:
#     print(n1,"is an armstrong no.")
# else:
#     print(n1,"is not armstring no.")

#..............................................................................................


#..................FACTORIAL NUMBER........................................................
# n=int(input("enter num.  "))
# fac=1
# while n>0:
#    fac=fac*n
#    n-=1
# print(fac)
#...........................................................................................

#.........................BINARARY TO DECIMAL........................................................
# n=int(input("enter number here to decimal change  "))
# i=0
# rev=""
# while i<n:
#     i=n%2
#     rev+=str(i)
#     n//=2
# print(rev)
# print(rev[::-1])

#...................................................................................................

#......................ADD FIRST N TERM IN LOOP SERIES.....................................................

# n=int(input("enter a number "))
# i=1
# while i<=n:
#     if i==n:
#         print(str(i)+"/"+str(i)+"!")
#     else:
#         print(str(i)+"/"+str(i)+"!","+",end=" ")
#     i+=1
    
#...................................................................................................

#..................SUM THE SEQUENCE..................................................................
# n=int(input("enter a number "))
# i=1
# j=1
# sum=0
# fac=1
# while i<=n:
#     div=i/j
#     fac=fac*div
#     sum+=fac
#     j+=1
# print(sum+1)

#..................DOUBT...........................................................................

#..........................PALINDROME.....................................................................




# n=input("enter no. ")
# rev=n[::-1]
# while n==rev:
#   print("Yes")
#   break
# else:
#   print("No")   


#................................................................................................

#...................10 NUMBER AND THEIR AVERAGE...................................................

# sum=0
# i=0
# while i<=10:
#     n=int(input("enter a number "))
#     sum=sum+n
#     i+=1
# print(sum/n)
    


#......................................................................................................
#...24.......................100-500 show odd/even and sum...........................................

# i=100
# sum_a=0
# sum_b=0
# n=500
# while i<=n:
#     if i%2==0:
#       sum_a+=i
#     else:
#       sum_b+=i
#     i+=1
# print(sum_a,"is even no.")  
# print(sum_b,"is odd no.")  

#...................................................................................................
#.23................largest and smallest number from 10 accepted no. from user...........................

# i=0
# while i>=0:
#     n=int(input("enter a number "))
#     print(min(n))
#     print(max(n))
#     i+=1
        
#.................................DOUBT.................................................................

#..26.............................2 22 222 ........................................................
# n=int(input("enter a number"))
# i=0
# while i<=n:
#     print("2"*i,end=" ")
#     i+=1
    
#............................................................................................................

#..................pattern.........................................................................

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#        print(j,end=" ")
#        j+=1
#     print()
#     i+=1

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#        print(i,end=" ")
#        j+=1
#     print()
#     i+=1

# i=1
# while i<=5:
#     j=1
#     while j<=6-i:
#        print(j,end=" ")
#        j+=1
#     print()
#     i+=1

# i=1
# while i<=5:
#     j=1
#     while j<=6-i:
#        print(i,end=" ")
#        j+=1
#     print()
#     i+=1


# i=1
# while i<=5:
#     j=1
#     while j<=6-j:
#        print(i,end=" ")
#        j+=1
#     print()
#     i+=1




# # #..................PYRAMID.PATTERN....................................................................

# n=int(input("enter number"))
# i=1
# while i<=n:
#     j=1
#     while j<=n-i:
#         print(end=" ")
#         j+=1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=2


# n=int(input("enter number"))
# i=1
# while i<=n:
#     j=1
#     while j<=n-i:
#         print(end=" ")
#         j+=1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1
#................................................................................................
# r=1
# while r<=5:
#     c=1
#     while c<=9:
#         if (r==1) and (c==5):         {{{{{NOT WORKING}}}}}
#            print("*",end="")
#         if (r==2) and (c==4 or c==5 or c==6):
#             print("*",end="")
#         if (r==3) and (c==3 or c==4 or c==5 or c==6 or c==7):
#             print("*",end="")
#         if (r==4) and (c==2 or c==3 or c==4 or c==5 or c==6 or c==7 or c==8):
    #         print("*",end="")
    #     if (r==5) and (c==1 or c==2 or c==3 or c==4 or c==5 or c==6 or c==7 or c==8 or c==9):
    #         print("*",end="")
    # print()
    # r+=1   
#..21.........................................................................................


# i=1
# n=int(input("enter a number"))
# while i<=n:
#     if i==n:
#        print(str(i)+"/"+str(i)+"!")
#     else:
#         print(str(i)+"/"+str(i)+"!","+",end="")
#     i+=1


# sum=0
# i=0
# while i<=10:
#     n=int(input("enter nu."))
#     sum+=n
#     i+=1
# print(sum/2)


    


      
      


    
# sum=0
# i=0
# while i<=10:
#     n=int(input("enter nu."))
#     sum+=n
#     i+=1sum=0
# i=0
# while i<=10:
#     n=int(input("enter nu."))
#     sum+=n
#     i+=1
# print(sum/2)


# print(sum/2)

# i=1
# while i<=5:
#    print("2"*i,end=" ")
#    i+=1 

#.............HONEY QUES.............................................................
# a=5
# b=7
# while a<b:
#     print(a+b)
#     a+=1



# i=0
# sum=0
# n=int(input("enter  "))
# while i<=n:
   
#     if n>0:
#         sum+=n
#         i+=1
#     else:
#         print("wrong")
    # print(sum/2)


# a="sapna"
# b="9.5"
# c="6.0"
# d="5"
# e=float(b)
# f=int(e)
# g=float(c)
# h=int(g)
# j=int(d)
# m=(f*h)
# n=(h*j)
# print(m, a, n)

#......................................................................................................



#..................2 INTERVIEW QUESTION............................................................
# n=int(input("enter "))
# i=0
# while i<=n:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j+=1
#     print()
#     i+=1



# i=1
# while i<=50:
#     if i%3==0 and i%5==0:
#         print(i,"buzz and fizz")
        
#     elif i%5==0:
#         print(i,"fizz")
        
#     elif i%3==0:
#         print(i,"buzz")
#     else:
#         print(i)
#     i+=1

#..................................................................................................


#..27...........................SQUARE SERIES.....................................................

# i=1
# while i<=5:
#     print(i**2,end=" ")
#     i+=1
#..................................................................................................
# 
# #..30................CUBE SERIES....................................................................    

# n=int(input("enter a number"))
# i=1
# sum=0
# while i<=n:
#     sum+=i**3
#     print(i**3,end="+")
#     i+=1
#     # sum+=i**3
# print()
# print(sum)
#.................................................................................................



#....31................series..........................................................................


# n=int(input("enter a number"))
# i=1
# m=1
# while n>=i:
#     m=m*i
#     if i==n:
#       print(m,end=" ")
#     else:
#       print(m,end=" + ")
#     i+=1

# #..............................sum of series...................................................
# n=int(input("enter a number"))
# sum=0
# i=1
# m=1
# while n>=i:
#     m=m*i
#     sum+=m
#     if i==n:
#       print(m,end=" ")
#     else:
#       print(m,end=" + ")
#     i+=1
# print()
# print(sum)
# #....................................................................................................

# #..31...........................
# n=int(input("enter a number"))
# i=1
# m=1
# while n>=i:
#     m=m*i
#     if n!=0:
#        print(m,end="  ")
#     else:
#        print(m,end=" + ")
#     i+=1
#.................................................................................................

#''32'''''''''''''''''''''''''''''''''''''''''''''''''''''series'''''''''''''''''''''''
# n=int(input("enter   "))
# i=1
# while i<=n:
#     if i%2!=0:
#         if i==n:
#             print(i**2, end=" ")
#         else:
#             print(i**2,end=" + ")
#     else:
#         if i==n:
#             print(i**2, end=" ")
#         else:
#             print(i**2,end=" - ")
#     i+=1
#.................................................................................................


#..33...........................COMPUTER.PRINT.........................................................

# n="COMPUTER"
# i=0
# while i<len(n):
#     print(n[i],end="")
    
#     i+=1

# .................................................................................................

# l = [23, 45, 32, 25, 46, 33, 71, 99]
# while l>=0:
#     if l%2==0:
#         print(l)

#,35,,,,,,,,,,,,,,,FACTOR,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# n=int(input("enter a number"))
# i=1
# while n>i:
#    print(n//i)
#    i+=1
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

#,,,,,,,,,,,,,SUM OF EVEN NO,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# a=int(input("enter a num:"))
# i=10
# while a>=i:
#     if i%2==0:
#      sum1=0
#     else:
#      sum2=0
# i+=1
# print(sum1)
# print(sum2)

#.60..........IF ELSE............................................. 

# n=input("enter  ")
# e=n.split(".")
# print(e[0])

# a=input("enter ")
# if ('a','e','i','o','u','A','E','I','O','U'):
#     print("vowel")
# else:
#     print("con")
#..............................SUM OF EVEN NO BY TWO INPUT USER NO....................................


# num1=int(input("enter a number "))
# num2=int(input("enter last number "))
# sum=0
# while num1<=num2:
#     if num1%2==0:
#        sum+=num1
#        print(sum)
#     num1+=1
    

 #                            [2 METHOD ]
# num1=int(input("enter a number "))
# num2=int(input("enter last number "))
# sum=0
# while num1<=num2:
#    if num1%2==0:
#        sum+=num1
       
#    num1+=1
# print(sum)
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

#............NO. DIVISIBLE BY 5 OR 7....................................................

# num1=1500
# num2=2700
# while num1<=num2:
#     if num1%5==0 and num1%7==0:
#         print(num1,"is divisible")
#     num1+=1

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

#,,,,,,,,,,,,,,sum without use++ sing,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# a=3
# b=2
# z=a-(-b)
# print(z)

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,


#,,,,,,,,,,,,,,,,,,GUESSING GAME,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# n=int(input("guess the number 1 to 10.  "))
# k=5
# i=0
# while i==0:
#     if n==5:
#         print(n,"yes you won")
#     else:
#         print(n,"no try again")
#     i+=1





# n=int(input("guess the number 1 to 20.  "))
# k=5
# i=0
# while i==0:
#     if n==3:
#         print("you have 3 chance to guess the number")
#         r=1
#         while r<=3:
#             q=int(input("enter number again "))
#             if q==5:
#                 print(q,"won")
#             else:
#                 print(q,"no you loss ")
#             r+=1
            
#     elif k==n:
#         print(n,"yes you won")
#     else:
#         print("no out from game")
#     i+=1
    


# #..............................................................................................

# #,,,,,,,,,,,,,,,,,,,,MERAKI QUESTION............................................................


# # i=0
# # while i <=50:
# #     if i%2==0:
# #         print(i,end=", ")
# #     else:
# #         print(i,end=", -")
# #     i+=1

                    #[[[SUM OF PRODUCT WITHOUT USING MULTIPLY SING]]]

# num1=int(input("enter a number "))
# num2=int(input("enter a number "))
# sum=0
# i=1
# while i<=num2:
#     sum+=num1
#     i+=1
# print(sum)

# i=1
# while i<=5:
#     j=1
#     while j<=5-i:
#         print(" ",end="")
#         j+=1
#     k=1
#     while k<=i:
#         print("*",end="")
#         k+=1
#     print()
#     i+=1






# n=int(input("enter number"))
# i=1
# while i<=n:
#     j=1
#     while j<=n-i:
#         print(end=" ")
#         j+=1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=2


# n=int(input("enter number"))
# i=1
# while i<=n:
#     j=1
#     while j<=n-i:
#         print(end=" ")
#         j+=1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1


# num=int(input("enter "))
# i = 2
# while (i<num):
#  if (num%i == 0):
#   print(num, 'is not a prime number')
#   break
#  i = i + 1
# else:
#  print(num, 'is a prime number')

# i = 0
# while(i<5):
#    j = 0
#    while(j<5): #loop2
#      if (j > 3):       
#            break    
#      else:
#           print("*"), 
#      j = j + 1 
#    print('')
#    i = i + 1





# i=556
# while i<660:
#    z=i-555
#    if z%7==0:
#       print(z)
#    i+=1

# for i in range(5):
#    print(i)

# for i in(1,2,3):
#     print(i)

# for i in (4,3,0,2,1):
#     print(i)


# for i in range(10):
#     if i%2!=0:
        # print(i,"hello")


# for i in range(10,2,-2):
#     print(i,"hello")

# str = "Python Output based Questions"
# word=str.split()
# for i in str:
#     print(i,end="")


# for i in range(7,10):
#     print("Python Output based Questions")
    



# for i in range(7,-2,-9):
#    for j in range(i):
#        print(j)
#    i="9"
#    for k in i:
#        print(k)


# grocery_list=['flour','cheese',' carrots']
# print(grocery_list[:-1])

original=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
print(original[0][1])
i = 0
while i<len(original):
    