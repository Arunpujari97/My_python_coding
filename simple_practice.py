##for i in range(5):
##    print(end='\n')
##    for j in range(5):
##        print("*",end='')
##n=int(input("enter the number of rows"))
##for i in range(n):
##   for j in range():
##        print("*",end=' ')
# from tkinter.font import names


##n=int(input())
##if (n%2!=0)or(n%2==0 and n in range(6,20)):
##    print("weird")
##    
##elif n%2==0 and n>20 or n in range(2,5):
##    print("not weird")
##
##    n=int(input())
##if (n%2!=0)or(n%2==0 and n in range(6,20)):
##    print("weird")
##    
##elif n%2==0 and n>20 or n in range(2,5):
##    print("not weird")

# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print("")

# class a():
#     def arun(self):
#         global n
#         n=10
# class b(a):
#     @classmethod
#     def praveen(self):
#         print("arun")
# b.praveen()
#
# class parent():
#     def __init__(self,name):
#         self.name=name
#     def name1(self):
#         return f"hello {self.name}"
# class child(parent):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age=age
#     def name2(self):
#         return f"hello {self.name} and your ange {self.age}"
# child=child("arun",22)
# print(child.name2())
# print(child.name1())

# class parent():
#     def greet(self):
#         print("arun")
# class child(parent):
#     def greet(self):
#         print("praveen")
# c=child()
# c.greet()
#
# k=parent()
# k.greet()

# class a():
#     def greet(self):
#         print("arun")
# class b():
#     def greet(self):
#         print("praveen")
# class c(a,b):
#     pass
# c=c()
# print(c.greet())

# num=11
#
# for i in range(2,num):
#     if num%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")
#
# def prime(num):
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return False
#         return True
# c=prime(5)
# print(c)

# arr=[]
# length=int(input("enter the lenth of the array"))
# for i in range(length):
#     a=int(input("enter the number sepereted by comma"))
#     arr.append(a)
# counter=0
# value_to_search=int(input("enter the elemnt to serch"))
# for k in arr:
#     if k==value_to_search:
#         print("found at",counter)
#     counter += 1
# else:
#     print("value not found")

# arr=[]
# a=input("enter the elemt").split(",")
# for i in a:
#     arr.append(int(i))
# arr=sorted(arr)
# elem_to_search=int(input())
# lower=0
# upper=len(arr)+1
#
# while lower<upper:
#     mid = (lower + upper) // 2
#     if arr[mid]==elem_to_search:
#         print("found")
#         break
#     elif elem_to_search>arr[mid]:
#         lower=mid
#     else:
#         upper=mid

# arr=[]
# a=input("enter tge inputs").split()
# for i in a:
#     arr.append((int(i)))
# first=0
# while first<len(arr)-1:
#     last=first+1
#     while last<len(arr):
#         if arr[first]>arr[last]:
#             arr[first],arr[last]=arr[last],arr[first]
#         last+=1
#     first+=1
# print(arr)
#
# def bouble(arr):
#     for i in range(len(arr)-1):
#         for j in range(len(arr)-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]= arr[j+1],arr[j]
#     print(arr)
# arr=[]
# a=input("enter thgae numbers").split()
# for i in a:
#     arr.append(i)
# bouble(arr)

# def selection_sort(arr):
#     first=0
#     second = first + 1
#     while first<len(arr):
#         if arr[first]>arr[second]:
#             arr[first]=arr[second]
#         else:
#             second+=1
#     return arr
# arr=[]
# a=input("enter").split()
# for i in a:
#     arr.append(int(i))
# selection_sort(arr)

# number=int(input("enter thge number"))

# if number<=1:
#     print('not prime')
# else:
#     for i in range(2,number):
#         if number%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")

# number=int(input("enter the number"))
# for i in range(2,number+1):
#     is_prime=True
#     for j in range(2,i):
#         if i%j==0:
#             is_prime=False
#             break
#     if is_prime:
#         print(i)

# numbers=input().split()
# arr=[]
# for i in numbers:
#     arr.append(int(i))
# arr=sorted(arr)
# print(arr[-2::])

# name=input("enter the name").split()
# key=input('enetr the key').split()
# dict={}
# for i,j in zip(name,key):
#     dict[i]=j
# print(dict)

