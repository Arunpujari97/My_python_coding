##for i in range(5):
##    print(end='\n')
##    for j in range(5):
##        print("*",end='')
#n=int(input("enter the number of rows")
#for i in range(n):
#   for j in range():
#        print("*",end=' ')

##n=int(input())
##if (n%2!=0)or(n%2==0 and n in range(6,20)):
##    print("weird")
##    
##elif n%2==0 and n>20 or n in range(2,5):
##    print("not weird")



##############################################maximum file version########
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


##sortings programs and searching"

##array=input("enter the elements").split()
##key=int(input("enter the value to search"))
##found=False
##for index,i in enumerate(array):
##    if key==int(i):
##        print("the element is found",i," at position",index)
##        found=True
##        break
##if not found:
##    print("the element not found")

################################################## same same but diffrent

##key=int(input())
##n=int(input())
##arr=input().split()
##arr=[int(x) for x in arr]
##i=0
##found=False
##while i<n:
##    if arr[i]==key:
##        print("element found")
##        found=True
##    i+=1
##if not found:
##    print("element not found")


####################################not working
##n=int(input())
##arr=input().split()
##arr=[int(x) for x in arr]
##list1=[]
##i=0
##j=i+1
##while i<=n:
##    if arr[i]<=arr[j]:
##        list1.append(arr[i])
##        i+=1
##    else:
##        j+=1        
##print(list1)

# def is_monotonic(array):
#     n = len(array)
#     if n <= 1:  # Handle empty and single-element arrays
#         return True
    
#     # Convert all elements to integers
#     array = [int(x) for x in array]
    
#     # Determine the nature of monotonicity based on the first and last elements
#     if array[0] < array[-1]:  # Check for monotone increasing
#         for k in range(n - 1):
#             if array[k] > array[k + 1]:
#                 return False

#     elif array[0] > array[-1]:  # Check for monotone decreasing
#         for k in range(n - 1):
#             if array[k] < array[k + 1]:
#                 return False

#     else:  # All elements might be the same
#         for k in range(n - 1):
#             if array[k] != array[k + 1]:
#                 return False

#     return True

# # Example usage
# array1 = input("Enter array elements separated by spaces: ").split()
# print(is_monotonic(array1))
       
        
arr=[]
elements=input("enter the elements").split()
for i in elements:
    arr.append(int(i))
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            i+=1

print(arr)











    
