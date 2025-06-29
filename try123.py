# intf=input("enter the world")
# pri=intf.split()
# print(pri)
# maximum=max(pri)
# max2=int(maximum)
# max3=max2+1
# print(max3)


# array=input("enter the elemenst to the array")
# arr=array.split()
# arr1=sorted(arr)
# print(arr1)

    
# word1=input("enter the first name")
# word2=input("enter the second name")
# for alphabet in range(len(word1) and len(word2)):
#        print(alphabet())

# word1=input("enter the word")
# word2=input("enter the word")
# for i in range(word1 and word2):
#    if word1[i]==word2[i]:
#        print(i)
#    else:
#        print("no similer")

##n=int(input("enter the number"))
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print(i,end="")
##    print('\n')
##
##n=int(input())
##for i in range(1,n):
##    print(i*(10**i-1)//9)


##f=int(input())
##n = input()
##for f in range(2,11):
##    m=n.split()
##    m1=list(m)
##    m2=sorted(m1)
##    k1=set(m2)
##    k4=list(k1)
##    k2=max(k1)
##    k3=k1.remove(k2)
##    print(max(k1))

# def is_prime(n):
#   for i  in range(n):
#    if i==1 and i==0:
#        print("not a prime")
#    elif (n%i)==0:
#        print("a prime")
#    else:
#        print("not a prime") 
# is_prime(5)

##n = int(input())  # First input: number of elements
##arr = list(map(int, input().split()))  # Second input: space-separated integers
##
##arr = list(set(arr))  # Convert to set to remove duplicates, then back to list
##arr.sort(reverse=True)  # Sort in descending order
##





##
##list=[]
##n=int(input())
##list.append(n)
##m=int(input())
##list.append(m)
##k=int(input())
##list.insert(1,k)
##print(list)



##print(arr[1])  # The second element is the runner-up
##n=int(input())
##for name,grade in range(n):
##    name=input()
##    grade=input()
##    names=list(name.split())
##    grades=list(grade.split())
##    names_gread=(name,grade)
##    print(names_gread)
##for name in names:
##    dicst=list(name)
##    dicst=dicst.append(grade)
##    dicst1=dicst.append(list(dicst))
##print(dicst1)

##arr=input()
##arr=list(arr.split())
##maximum=max(arr)
##count=0
##for elem in arr:
##    if elem==maximum:
##        print(elem)
##        count +=1
##        print(count)
##        arr1=arr.index(maximum)
##        arr2=arr[arr1+1:]
##        maximum1=max(arr2)
##        for eleme in arr2:
##            if  eleme==maximum1:
##                print(eleme)
##                count+=1
##                if maximum1==arr2[-1]:
##                    print(count)
##                else:
##                   print(count+1)
##                break
##        break
##


#####################################white space
##string=input()
##string2=input()
##print(list(string))
##print(list(string2))
##i=" "
##space=string.count(i)
##space1=string2.count(i)
##print(space)
##print(space1)
##space3=space-space1
##print(space3)



############################################maximum file version########
##import re
##input1=input()
##
##data =input1.split() 
##int_values = []
##
##for item in data:
##    numbers = re.findall(r'\d+', item)
##    for num in numbers:
##        int_values.append(int(num))
##
##print(int_values)

##m=int(input())
##n=input()
##n = [int(item) for item in n.split()]
##k=sorted(n)
##t=list(reversed(k))
##print(t[1:2])


##string=input()
##string=string.split()
##gread=input()
##gread=gread.split()
##gread=sorted(int(item) for item in gread)
##string=sorted(item for item in string)
##print(string[0:2])


##dist={}
##n=int(input())
##for _ in range(n):
##    name=input()
##    score=input()
##    dist[name]=score
##dist=dict(sorted(dist.items(),key=lambda item:item[1]))
##dist1=list(dist.keys())[:2]
##print(sorted(dist1))



#sorting of nested loop according to scores and print two lowest
                                                              #scored names in accending order
##arr=[]
##n=int(input())
##for _ in range(n):
##    name=input()
##    score=float(input())
##    arr.append([name,score])
##scores=[score for score in arr]
##sorted_names=sorted(scores,key=lambda student:student[1])
##prin=sorted_names[1:3]
##sorted_string=[item[0] for item in prin]
##string='\n'.join(sorted(sorted_string))
##print(string)



########prime#######################
##count=0
##for i in range(2,50):
##    for j in range(2,50):
##        if i%j==0:
##            break
##    if i==j:
##        count +=1
##        print(i,count)
                
###################fabinachi###########
##num=int(input())
##n1,n2=1,2
##sum=0
##for i in range(num):
##    n1=n2
##    n2=sum
##    sum=n1+n2
##    print(sum)
##    

############################it print the average of student wher student selected by user####
##names_score=[]
##num=int(input())
##for _ in range(num):
##    name=input()
##    score=input()
##    scores=score.split()
##    names_score.append([name,scores])
####print(names_score)
##name1=input()
##found_list=None
##for sublist in names_score:
##    if name1 in sublist:
##        found_list=sublist
##int_list=found_list[1]
##sublist_sum=sum(int(i) for i in int_list)
##avg=sublist_sum/len(int_list)
##print(avg)
##
############################or##################
##n = int(input())
##student_marks = {}
##for _ in range(n):
##    data = input().split()
##    name = data[0]
##    marks = list(map(float, data[1:]))  # Convert marks to float
##    student_marks[name] = marks
##query_name = input()
##marks = student_marks[query_name]
##average = sum(marks) / len(marks)
##print(f"{average:.2f}")



##list=[]
###n=int(input())
###list.append(n)
###m=int(input())
###list.append(m)
###k=int(input())
###list.insert(1,k)
###print(list)
##list.insert(0,int(input()))
##list.insert(1,int(input()))
##list.insert(0,int(input()))
##list1=list
##list4=list1.remove(int(input()))
##list4.append(int(input()))
##list4.append(int(input()))
##list4.sort()
##list2=list4
##list2.pop()
##list2=list2[::-1]
##list2=list2
##print(list1)
##print(list2)
##print(list3)

##if __name__ == '__main__':
##    # Initialize an empty list
##    my_list = []
##    
##    # Read number of commands
##    N = int(input())
##    
##    # Process each command
##    for _ in range(N):
##        # Read the command and split it into parts
##        command = input().split()
##        
##        # Check the command and apply the corresponding list operation
##        if command[0] == "insert":
##            my_list.insert(int(command[1]), int(command[2]))
##        elif command[0] == "print":
##            print(my_list)
##        elif command[0] == "remove":
##            my_list.remove(int(command[1]))
##        elif command[0] == "append":
##            my_list.append(int(command[1]))
##        elif command[0] == "sort":
##            my_list.sort()
##        elif command[0] == "pop":
##            my_list.pop()
##        elif command[0] == "reverse":
##            my_list.reverse()
##
##

######################################hashing of the tupel#######################
##n=int(input())
##for _ in range(n):
##    my_list=input().split()
##    my_list=tuple(map(int,my_list))
##    hashing=hash(my_list)
##    print(hashing)


##n = int(input())  # Reading the number of elements
##elements = map(int, input().split())  # Reading the space-separated integers and converting them to integers
##t = tuple(elements)  # Creating a tuple from the integers
##print(hash(t)) 


##k=input()
##for s in k:
##    print(s)
##l=s.isupper()
##m=s.islower()
##n=s.isdigit()
##o=s.isalnum()
##p=s.isalpha()
##print(l)

##def swap_case(s):
##    result=s.swapcase()
##    print(result)
##        
##swap_case(input())


##def string(a):
##    a=a.split()
##    b="-".join(a)
##    print(b)
##string(input())

##import re
##main_string=input()
##sub_string=input()
####main_string=re.search(r'\s+',sub_string)
####m=main_string.start()
####print(m)
####n=main_string.end()
####print(n)
##
##m=finditer(sub_string,main_string)
##print(m)

##string=input()
##list1=[]
##for char in string:
##    if char not in list1:
##        list1.append(char)
##
##print(list1)

##string=input()
##list=[]
##while string:
##    for char in string:
##        for char1 in string:
##            if char!=char1:
##                list.append([char,char1])
##        break
##print(list)

##floting_list=input().split()
##for item in floting_list:
##    if '+' '-' not in str(item):
##        if '.' in str(item):
##            print("True")
##    else:
##        print("false")
        

##string=input()
##m=int(input())
##arr=[]
##for char in string:
##    arr.append(char)
##arr.insert(m,'k')
##string2=''.join(arr)
##print(string2)
    
##string=input()
##sub_string=input()
##print(string.count(sub_string))

##def count_overlapping(string, sub_string):
##    count = 0
##    start = 0
##    
##    while True:
##        # Find the substring starting from 'start' index
##        start = string.find(sub_string, start)
##        
##        # If not found, break the loop
##        if start == -1:
##            break
##        
##        # If found, increment count and move to the next character
##        count += 1
##        start += 1  # Move to the next position to allow overlapping
##        
##    return count
##
### Input
##string = input("Enter the main string: ")
##sub_string = input("Enter the substring to count: ")
##
### Output the count of overlapping occurrences
##print("Occurrences:", count_overlapping(string, sub_string))

##class calculator():
##    def __init__(self):
##        self.num1=int(input())
##        self.num2=int(input())
##    def add(self,num3,num4):
##        return num3+num4
##       
##    def sub(self,num3,num4):
##        return num3-num4
##    
##    def mul(self,num3,num4):
##        return num3*num4
##        
##    def call_fun(self):
##        result1=self.add(self.num1,self.num2)
##        result2=self.sub(self.num1,self.num2)
##        result3=self.mul(self.num1,self.num2)
##        return result1,result2,result3
##obj=calculator()
##result1,result2,result3=obj.call_fun()
##print(result1)
##print(result2)
####print(result3)
##n=input().split()
##p=[]
##
##for item in n:
##    p.append(item)
##    
##x=int(p[0])
##y=int(p[1])
##print(x*y)

##list1=input().split()
##count=[]
##for item in list1:
##    count.append(int(item))
##print(sum(count))
##
##num=int(input())
##y=1
##x=1
##while x<num+1:
##    y=y*x
##    x+=1
##print(y)

##string=input()
##string1='aeiouAEIOU'
##count=0
##for char in string:
##    if char in string1:
##        count+=1     
##print(count)







##string = input("Enter a string: ")
##vowels = 'aeiouAEIOU'
##count = 0
##
### Loop through the input string and count all occurrences of vowels
##for char in string:
##    if char in vowels:
##        count += 1
##
##print("Total number of vowels (including repeated ones):", count)

##
##list1=input().split()
##list2=[]
##start=int(list1[0])
####print(start)
##end=int(list1[1])
####print(end)
##diviser=int(list1[2])
####print(diviser)
##for i in range(start,end+1):
##    if i%diviser==0:
##        list2.append(i)
##
##print(list2)
        

##list2=[]
##def find_divisibles(start, end, divisor):
##    for i in range(start,end+1):
##        if i%divisor==0:
##            list2.append(i)
##    return list2
##list1=input().split()
##start1=int(list1[0])
##end1=int(list1[1])
##divisor1=int(list1[2])
##result=find_divisibles(start1,end1,divisor1)
##print(result)


##
##string=input().replace(" ","").lower()
##list1=[]
##for char in string:
##    if char.isalpha():
##        position=ord(char)-ord('a')+1
##        list1.append(position)
##    else:
##        print('not a leter')
##print(list1)


##def alphabet_position(text):
##    # Your list comprehension goes here
##    # Hint: Use ord() to get ASCII value and chr() to convert back to character if needed
##    pass
##list1=[]
##if __name__ == "__main__":
##    input_string = input().strip().lower()
##    for char in input_string:
##        if char.isalpha():
##            result=ord(char)-ord('a')+1
##            list1.append(result)
##print(list1)


##if __name__=='__main__':
##    input_string=input()
##    input_string1=input_string.replace(" ","")
##    for index,char in enumerate(input_string1):
##        if index%2==0:
##            print(char.upper(),end="")
##        else:
##            print(char.lower(),end="")
        
##def string1(text):
##text=input().split()
##integer=int(input())
##list1=[]
##for item in text:
##    if len(item)>=integer:
##        list1.append(item)
##print(list1)
##

##def filter_words(sentence, min_length):
##    # TODO: Implement the function using a Generator expression
##    #sentence = input().split()
##   # min_length = int(input())
##    list1=[]
##    for item in sentence:
##        if len(item)>=min_length:
##            list1.append(item)
##    return list1
##
##think=filter_words(input().split(),int(input()))
##print(think)

##
##def reverse_strings(string_list):
##    for item in string_list:
##        print(item[::-1],end=' ')
##    
##    
##result=reverse_strings(input().split())
##print(result)


##def reverse_strings(string_list):
##    
##    reversed_list = [item[::-1]for item in string_list]
##    return ' '.join(reversed_list) 
##result = reverse_strings(input().split())
##print(result)
##

##inch=2.54
##list1=[]
##def inchtometer(inches):
##    inches=inches.split()
##    for i in inches:
##        inche=float(i)*inch
##        list1.append(str(inche))
##    return ' '.join(list1)
##result=inchtometer(input())
##print(result)

##list1=input().split()
##for i in list1:
##    if i.startswith("-"):
##        list1=i.removeprefix("-")
##        print(list1,end=' ')
##    else:
##        print(i,end=" ")
##        

##stringlist=input().split()
##char=input()
##list1=[]
##for i in stringlist:
##    if char in i:
##        list1.append(i)
##print(list1)


# def string1(string):
#    vowels='aeiouAEIOU'
#    for i in string:
#        for char in vowels:
#            if i.startswith(char):
#                string.remove(i)           
#    return string

# string2=string1(input().split())
# print(string2)
    

# def itere(words):
#    vowels='aeiouAEIOU'
#    result=[word for word in words if word[0] not in vowels]
#    return " ".join(result)
# result1=itere(input().split())
# print(result1)
# itere('arunkumar')
##
##def add(digit):
##    a=0
##    for i in digit:
##        a=a+int(i)
##    return a
##result=add(input())
##print(result)
##def claculate(integer):
##    a=0
##    for i in integer:
##       try:
##            a += float(i) 
##       except ValueError:
##           print(i)
##    return a
##def avg(a,count):
##    if count==0:
##        return 0
##    return a/count
##retunt=input().split()
##result=claculate(retunt)
##retun=avg(result,len(retunt))
##print(f'{retun:.2f}')


##
##mydict={}
##n=int(input())
##addition=0
##for _ in range(n):
##    product=input()
##    price=float(input())
##    mydict[product]=price
##    addition+=price
##discount=float(input())
##discount=(discount)if value else 0
##total=addition

##print(mydict)
##print(addition)

# arr=input().split()
# list1=[]
# for i in arr:
#    list1.append(int(i)*int(i))
# print(sorted(list1))

##class arraycreation:   
##    def creation(self,array):
##        self.n=[]
##        self.n=[]*array
##        print(self.n)
##        print(len(self.n))
##    def appending(self):
##        self.elem=input("enter the element")
##        for self.n in range(len(self.n)):
##            if len(self.n)==0:
##                self.n.append(self.elem)
##                print(self.n)
##            else:
##                print("list is full")
##        
##        
##array1=arraycreation()
##length=int(input())
##array1.creation(length)
##array1.appending()

# array=input().split()
# maximum=max(array)
# for i,index in enumerate(array):
#    if index==maximum:
#        print(i,maximum)

    
# a=input()
# b=input()
# maximum=min(len(a),len(b))
# for i in range(maximum):
#    print(a[i],b[i],end=" ")
# if len(a)>maximum:
#            print(a[maximum:],end=" ")

# elif len(b)>maximum:
#    print(b[maximum:],end=" ")


##
# a = input("Enter first string: ")
# b = input("Enter second string: ")

# # Initialize the result string
# result = ""

# # Interleave characters using zip
# for char_a, char_b in zip(a, b):
#    result += char_a + char_b
# result +=a[len(b):]+b[len(a):]

# print(result)

##input_items=input().split()
##discount=input('discount:')
##if not discount:
##    discount=0
##else:
##    discount=discount
##tax=input('tax:')
##if not tax:
##    tax=10
##else:
##    tax=tax
##tip=input('tip:')
##if not tip:
##    tip=15
##else:
##    tip=tip
##menu_items={}
##total=0
##for item in input_items:
##    name,price=item.split(':')
##    menu_items[name]=float(price)
##    total +=float(price)
##
##discount1=total/100*discount
##total1= total-discount1

##tax1=total1/100*tax
##tip1=total/100*tip
##result=total-discount1+tax1+tip1
##print(result)
##
# def greet(name):
#    return f"Hello,{name}!"

# if __name__ == "__main__":
#    name = input().strip()
#    name1=name.upper()
#    result = greet(name1)
#    print(result)



##
# with open("arun1.txt","r")as file:
#    comtent=file.read()
#    print(comtent)
##
# with open("arun1.txt","w")as file:
#    file.write("Hello,world")
#    print(file)
    
##
# def my_generator():
#    for i in range(3):
#        yield i
# for value in my_generator():
#    print(value)

# import numpy as np
# arr=np.array([1,2,3,4])
# print(arr*2)

# import threading

# def task():
#     print("Thread is running")

# t = threading.Thread(target=task)
# t.start()

# input1=input("enter the first string")
# input2=input("enter the second string")
# arr=[]

# for i,j in zip(input1,input2):
#     arr.append(i)
#     arr.append(j)
# print(arr)

# input1=input("enter the string to reverse")
# print(input1[::-2])

# numbers=input("enter the numbers by using space").split()
# arr=[]
# for i in numbers:
#     arr.append(int(i))
# arr=set(arr)
# arr=sorted(arr)
# arr=arr[::-1]
# print(arr)
# print(arr[1])

# ovels="AEIOUaeiou"
# counter=0
# input1=input("enter the string")
# for i in ovels:
#     for j in input1:
#         if i==j:
#          counter+=1
# print(counter)

# string0=input().split()
# string1=[]
# for i in string0:
#     string1.append(i)
# string2=input()
# count=0
# for word in string1:
#     if word== string2:
#         count +=1
# print(count)


# number_of_student=int(input())
# arr=[]
# for i in range(number_of_student):
#     student=input("name")
#     marks=input("marks")
#     arr.append(int(marks))
# sum=sum(arr)
# avg=sum/len(arr)
# print(avg)


# list=["arun","kumar","praveen","oreng","eye"]
# ovels="AEIOUaeiou"
# word1=[]
# for word in list:
#     if word[0] not in ovels:
#         word1.append(word)
# print(word1)

# start=int(input("start "))
# end=int(input("end "))
# divisor=int(input("divisor"))

# for i in range(start,end+1):
#     if i %divisor==0:
#         print(i)
            
# sentence=input("enter the sentence").split()
# for word in sentence:
#     print(word[::-1],end=" ")

# print("1.addition, 2. substraction, 3. multipliaction, 4.division")
# input1=int(input("first"))
# input2=int(input("second"))
# input3=int(input("opration"))
# if input3==1:
#     print(input1+input2)
# elif input3==2:
#     print(input1-input2)
# elif input3==3:
#     print(input1*input2)
# elif input3==4:
#     print(input1/input2)
# else:
#     print("invalid syntax")

# input1=input("list").split()
# list1=[]
# for  char in input1:
#     list1.append(int(char))
# print(list1)
# n=len(list1)
    
# count_of_even=0
# count_of_odd=0
# for i in list1:
#     if i%2==0:
#         count_of_even +=1
#     else:
#         count_of_odd +=1
# print(count_of_even)
# print(count_of_odd)

# for i in range(n-1):
#     for j in range(i+1,n):
#         if list1[i]>=list1[j]:
#             list1[i],list1[j]=list1[j],list1[i]
#         else:
#             i+=1
# list1=set(list1)
# list1=list(list1)
# print(list1[-2])

# input1=int(input("enter the number"))
# for i in range(input1):
#     if i%3==0 and i%5==0:
#         print(i)

# input1=input("list").split()
# list1=[]
# for char in input1:
#     list1.append(int(char))
# n=len(list1)
# list2=[]

# for i in range(n):
#     if list1[i] not in list2:
#         list2.append(list1[i])

# print(list2)


# string=input("string")
# if string==string[::-1]:
#     print("pallindrom")
# else:
#     print("not")

# sentence=input("enter the sentence").split()
# list1=[]
# for word in sentence:
#     list1.append(word)
# print(max(list1,key=len))

# n=int(input("enter the number"))
# for i in range(n+1):
#     if i%5==0 and i%3==0:
#         print("fizzi buzzi")
#     elif i%5==0:
#         print("fizzi")
#     elif i%3==0:
#         print("Buzzi")
#     else:
#         print(i)

# n=int(input("enter the number"))
# for i in range(2,n):
#     for j in range(2,i):
#         if i%j==0:
#             print("not prime")
#             break
#     else:
#         print(i)
        
# numbers=input("enter the  with the space").split()
# list1=[]
# for i in numbers:
#     list1.append(int(i))
# n=len(list1)
# n=int(input("enter the number"))
# rotationoflist=list1[n:]+list1[:n]
# print(rotationoflist)


# k=int(input("enter the number"))
# for i in range(n):
#     for j in range(i+1,n):
#         if list1[i]+list1[j]==k:
#             print(list1[i],list1[j])

# def arun():
#     n=len(arra)
#     seen=set()
#     for i in range(n):
#         if arra[i] not in seen:
#             count=arra.count(arra[i])
#             print(arra[i],":",count) 
#             seen.add(arra[i])
# arra=[]
# numbers=input("enter the numbers").split()
# for i in numbers:
#     arra.append(int(i))   

# arun()

# def arun(input1,input2):
#     if sorted(input1)==sorted(input2):
#         print("annagrame")
#     else:
#         print("not")

# arun("arun","nura")

# def arun():
#     for char in arr:
#       if char not in arr1:
#          arr1.append(char)
#     string=''.join(arr1)
#     print(string)
            

# input1=input("string")
# arr=[]
# arr1=[]
# for char in input1:
#     arr.append(char)
# arun()

# def arun():
#     for i in arr1:
#         if i not in arr2:
#             arr2.append(i)
#         else:
#             arr3.add(i)
#     print(arr3)

# input1=input("enter the string")
# arr1=[]
# arr2=[]
# arr3=set()
# for char in input1:
#     arr1.append(char)
# arun()

# def arun(sentence):
#     for i in sentence:
#         arr.append(i)
#     print(max(arr,key=len))
# arr=[]
# sentence=input("enter the sentence").split()
# arun(sentence)

# def arun(n):
#     for i in range(n):
#         for j in range(n):
#             if i>=j:
#                 print(j,end=" " )
#         print()


# n=int(input("enter the number"))
# arun(n)

# def arun(n):
#     for i in range(2,n):
#         for j in range(2,i):
#             if i%j==0:
#                break
#         else:
#             print(i) 
# arun(10)

# def fabinacci(n):
#     if n<0:
#         print("enter the valid number")
#     elif n==0:
#         return 0
#     elif n==1 or n==2:
#         return 1
#     else:
#         return fabinacci(n-1)+fabinacci(n-2)
# n=int(input())
# for i in range(n):
#     print(fabinacci(i),end=" ")   

# def arun(string):
#     i=0
#     j=0
#     for word in string:
#         i+=1
#         for char in word:
#             j+=1
#     print("word",i, "charecter",j)
# string=input("enter the sentence").split()
# arun(string)


# def arun(s1,s2):
#     if len(s1)!=len(s2):
#         return False
#     map1={}
#     map2={}
#     for c1,c2 in zip(s1,s2):
#         if c1 in map1:
#             if map1[c1]!=c2:
#                 return False
#         else:
#             map1[c1]=c2
#         if c2 in map2:
#             if map2[c2]!=c1:
#                 return False
#         else:
#             map2[c2]=c1
#     return True
# s1=input("enter the string")
# s2=input("enter the string")
# if arun(s1,s2):
#     print("string have same pattran")
# else:
#     print("not")

# def substring(arr):
#     n=len(arr)
#     for i in range(n+2):
#         if arr[0]==arr[n+1]:
#             arr.remove(arr[i])
#     print(arr)
# s1=input("enter the string")
# arr=[]
# for char in s1:
#     arr.append(char)
# substring(arr)

# def substring(s1):
#     start=0
#     end=len(s1)-1
#     while start<end and s1[start]==s1[end]:
#             if (end - start + 1) <= 3:
#                 break
#             start+=1
#             end-=1
#     result=s1[start:end+1]
#     print(result)
        
# s2=input("enter the string")
# s1=[]
# for char in s2:
#     s1.append(char)
# substring(s1)

# def armstrong(n):
#     sum=len(n)
#     total=0
#     for char in n:
#         total+=int(char)**sum
#     if total==int(n):
#         print("armstrong")
#     else:
#         print("not armstrong")
# armstrong("370")

# class bank_account:
#     def __init__(self):
#         self.account_number=None
#         self.account_holder=None
#         self.account_balence=0.0
#     def open_account(self):
#         self.account_number=input("enter the account number")
#         self.account_holder=input("enter the name of the account holder")
#     def deposite(self):
#         self.ammount=float(input("enter the ammount to deposite"))
#         self.account_balence+=self.ammount
#     def withdraw(self):
#         self.ammount_to_withdraw=float(input("enther the ammount to withdraw"))
#         if self.ammount_to_withdraw<=self.account_balence:
#             self.account_balence-=self.ammount_to_withdraw
#         else:
#             print("the ammount you enterd exceeds the current ballenc ammount =",self.account_balence)
#     def view_balence(self):
#         print("your balence is =",self.account_balence)
# account=bank_account()
# while True: 
#     print('''wellcome to the bank
#           1.open account
#           2.Deposite the ammount
#           3.withdraw thw ammount
#           4.view the balence
#           5.Exit''')
#     choice=int(input("enter your choice"))
#     if choice==1:
#         account.open_account()
#     elif choice==2:
#         account.deposite()
#     elif choice==3:
#         account.withdraw()
#     elif choice==4:
#         account.view_balence()
#     elif choice==5:
#         print("sure want to exit")
#         break
#     else:
#         print("invalid input")


# class book_management:
#     def __init__(self):
#         self.library={}
#     def add_book(self):
#         self.book_name=input("enter the book name to add")
#         self.book_author=input("enter the name who wrote the book")
#         self.library[self.book_name]=self.book_author

#     def remove_book(self):
#         self.book_name=input("enter the name of thge bbok to remove")
#         if self.book_name in self.library:
#             del self.library[self.book_name]
#         else:
#             print("sorry entered book name not in library")
#     def search_book(self):
#         self.book_name=input("enter the name of the book to search")
#         if self.book_name in self.library:
#             print("yes your searched book in the library")
#         else:
#             print("sorry your searched book is not in the library")
#     def track_avilability(self):
#         if not self.library:
#             print("there is no book")
#         else:
#             for name,author in self.library.items():
#                 print(f"{self.book_name} : {self.book_author}")
# book=book_management()
# while True:
#     print("""welcome to library management system
#           1.if you wana add book to library
#           2.if you wana remove book from the library
#           3.if you wana search the book in the library
#           4.if you wana see all avilable book
#           5.exit""")
#     choice=int(input("enter your choice"))
#     if choice==1:
#         book.add_book()
#     elif choice==2:
#         book.remove_book()
#     elif choice==3:
#         book.search_book()
#     elif choice==4:
#         book.track_avilability()
#     elif choice==5:
#         break
#     else:
#         print("invalid input")


# class employeeclass:
#     def __init__(self):
#         self.employee={}
#     def add_employee(self):
#         self.emp_Id=int(input("enter the employee id"))
#         self.emp_name=input("enter the name of the employee")
#         self.emp_age=input("enter the employee age")
#         self.emp_department=input("enter the department of the employee")
#         self.salary=float(input("enter the salary of the employee"))
#         self.employee[self.emp_Id]=[self.emp_name,self.emp_age,self.emp_department,self.salary]

#     def view_employee_details(self):
#         if not self.employee:
#             print("their is know employee added yet")
#         else:
#             print("the employee details are")
#             for emp_id,data in self.employee.items():
#                 print(f"{emp_id} = Name: {data[0]}, Age: {data[1]}, Dept: {data[2]}, Salary: {data[3]}")
    
#     def delete_employee(self):
#         self.emp_Id=int(input("enter the emploee id tom delete"))
#         if self.emp_Id in self.employee:
#             del self.employee[self.emp_Id]
#         else:
#             print("ther is no such employee")

# class manager_work(employeeclass):
#     def __init__(self):
#         super().__init__()
#         self.bonus=float(input("enter the bonus ammount"))
#         self.tax=float(input("enter the percent of tax to apply "))
    
#     def tax_report(self):
#         emp_id = int(input("Enter the employee ID to generate tax report: "))
#         if emp_id in self.employee:
#             emp_data = self.employee[emp_id]
#             salary = emp_data[3]  # salary is the 4th element
#             total_salary = salary + self.bonus
#             reduced = total_salary * (self.tax / 100)
#             net_salary = total_salary - reduced
#             print("After bonus and tax deduction, net salary is:", net_salary)
#         else:
#             print("Employee not found.")


# manager=manager_work()
# while True:
#     print("""welcome to employee manage ment system
#           1.Add employee
#           2.view employee details
#           3.delete employee
#           4.get tax_report
#           5.exite""")
#     choice=int(input("enter your choice"))
#     if choice==1:
#         manager.add_employee()
#     elif choice==2:
#         manager.view_employee_details()
#     elif choice==3:
#         manager.delete_employee()
#     elif choice==4:
#         manager.tax_report()
#     elif choice==5:
#         break
#     else:
#         print("invalid input")
    
# import math 
# class shape:
#     def __init__(self):
#         self.arr=[]
#         self.sides=list(map(float,input("eneter the sides to create shapes").split()))
#         self.length=len(self.sides)

# class circle(shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         print(f"the area of the circl is{math.pi*self.radius**2:.2f}")
#     def parameter(self):
#         print(f"the parameter of the circle is{2*math.pi*self.radius:.2f}")
# class squre(shape):
#     def __init__(self,hight,width):
#         self.hight=hight
#         self.width=width
#     def area(self):
#         print(f"the area of the squre is {self.hight*self.width}")
#     def parameter(self):
#         print(f"the parameter of the squre if {2*(self.hight+self.width):.2f}")

# shape1=shape()


# if shape1.length==1:
#         circle1=circle(shape1.sides[0])
#         circle1.area()
#         circle1.parameter()
# elif shape1.length==2:
#         squre1.squre(shape1.sides[0],shape1.sides[1])
#         squre1.area()
#         squre1.perimeter()
# else:
#         print("to much side and you have to enter one or two sides ")

# class collag:
#     collage={}
#     print("welcome to sir M Visveswaraya institute of tecnology")

# class student(collag):
#     def __init__(self):
#         self.n=int(input("enter the number of student"))
#     def student(self):
#         for i in range(self.n):
#             name=input("enter the name of the student")
#             Roll_number=input("enter the roll number of the student")
#             maths=int(input("enter the marks for the maths"))
#             science=int(input("enter the marks for the science"))
#             social_science=int(input("enter the marks for the social science"))
#             self.collage[Roll_number]={"name":name,"maths":maths,"scienc":science,"social":social_science}

#     def calculate(self):
#         for roll,data in self.collage.items():
#             total=data["maths"]+data["scienc"]+data["social"]
#             average=total/3
#             percentage=(total/300)*100
#             grade=self.grade(percentage)
#             print(f"Roll no : {roll}, total : {total},Average : {average}, grade : {grade}")
#     def grade(self,percentage):
#         if percentage>=90:
#             return "A+"
#         elif percentage>=80 and percentage<90:
#             return "A"
#         elif percentage>=70 and percentage<80:
#             return "B+"
#         else:
#             return "B"

# student1=student()
# student1.student()
# student1.calculate()

import os
file=open('C:/Users/My PC/OneDrive/Desktop/try_projects/arun1.txt','r')
file.read()


# file=open("C:/Users/My PC/OneDrive/Desktop/try_projects/arun1.txt",'w')
# file.write("arun kumar k h is the good boy")