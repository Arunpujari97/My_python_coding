#factorial number file
# def facttorial(num):
#     if num==1 or num==0:
#         return 1
#     else:
#         return num*facttorial(num-1)
# n=int(input())
# print(facttorial(n))


# fabinacci problem
# def fabinacci(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#        return fabinacci(num-1)+fabinacci(num-2)
# num=int(input())
# for i in range(num):
#     print(fabinacci(i),end=" ")

# tower of hanoi
# def towerofhonoi(n,source,temprovery,destination):
#     if n==1:
#         print(f"desk 1 move from {source} to {destination}")
#         return
#     towerofhonoi(n-1,source,destination,temprovery)
#     print(f"desk {n} move from {source} to {destination}")
#     towerofhonoi(n-1,temprovery,source,destination)
# desk=int(input("enter the number if desk"))
# towerofhonoi(desk,'a','b','c')


# def factorial(num):
#     if num==0 or num==1:
#         return 1
#     else: 
#         return num * factorial(num-1)

# num=int(input("enter the number"))
# print(factorial(num))

# def febinacci(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return febinacci(num-1)+febinacci(num-2)
# num=int(input())
# for i in range(num):
#     print(febinacci(i),end=" ")

# def towerofhanoi(n,source,temprovery,destination):
#     if n==1:
#         print(f"desk {1} is move from {source} to {destination}")
#         return
#     towerofhanoi(n-1,source,destination,temprovery)
#     print(" move {n} is move from {source} to {destination} ")
#     towerofhanoi(n-1,temprovery,source,destination)
# num=int(input())
# towerofhanoi(num,'a','b','c')

# word=input("enter the word")
# if word==word[::-1]:
#     print("palindrom")
# else:
#     print("not polindrom")


# def prime(num):
#     for i in range(2,num-1):
#         if num%i==0:
#             return "not prime"
#         else:
#             return "prime"
# print(prime(6))


# num=input()
# n=len(num)
# k=0
# for i in num:
#     k+=int(i)**n
# if k==int(num):
#     print("armstrong number")
# else:
#     print("not")

# def armstrong(num):
#     k=0
#     n=int(len(num))
#     for i in num:
#        k+=int(i)**n 
#     if k==int(num):
#         print("armstrong")
#     else:
#         print("not")
#         return
# num=input("enter teh number")
# armstrong(num)

# def armstrong(num):
#     n=len(num)
#     aumof_all={i: i**n for i in range(10)}
#     sumo_num=sum(aumof_all[int(k)] for k in num)
#     if sumo_num==int(num):
#         print("arm")
#     else:
#         print("not")
# armstrong('3445')

# arry=[]
# num=input()
# k=num.split()
# print(max(k),"and",min(k))

# arry=[]
# num=input().split()
# for i in num:
#     arry.append(i)
# for i in range(1,len(arry)-1):
#     for j in range(i+1,len(arry)):
#         if arry[i]==arry[j]:
#             print(arry[i],end=" ")
    
        
# arry=[]
# num=input().split()
# for i in num:
#     arry.append(i)    
# print(arry[::-1])

# word1=input()
# word2=input()
# if sorted(word1)==sorted(word2):
#     print("True")
# else:
#     print("false")

# def anagrams(word1,word2):
#     return (sorted(word1.replace(" ","").lower())==sorted(word2.replace(" ","").lower()) )

# word1="listen"
# word2="arunkumar"
# print(anagrams(word1,word2))


def missing_number(arr):
    n=len(arr)+1
    total=n*(n+1)//2
    return total-sum(arr)
num=[5,6,8,9]
print(missing_number(num))