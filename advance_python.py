2#Arrays is divided into two ways static and dynamic
#static array are only store same type data and dynamic store many type of data in the array
#homogenious and heterogenious are different homogenious store only same type of data and
# heterogenious store diffrent type of data


#arry support fallowing methods
#creation
#append
#index
#len
#insert
#clear
#pop
#find
#delete (this can be done by using world)

# let's start the coding
#creation
# import ctypes # this is used for use of array using c
# class ListCreation:
#     def __init__(self):
#         self.size = 1
#         self.n = 0
#         self.A = self.__make_array(self.size)
#
#     def __make_array(self, capacity):
#         # Creating the array (static, referential) with size capacity
#         return (capacity * ctypes.py_object)()
#
#     def __len__(self):
#         # Return the number of elements in the array
#         return self.n
# # append the item at last
#     def append_item(self, item):
#         if self.n == self.size: # this check whether the array has enough space or not
#             self.__resize(self.size * 2) #it doubl the size of array if array is enough to store data
#         self.A[self.n] = item
#         self.n += 1
# #resize function to resize array
#     def __resize(self, new_capacity):
#         B = self.__make_array(new_capacity)
#         # Copy all elements from A to B
#         for i in range(self.n):
#             B[i] = self.A[i] #this assign the values from one array to another
#         self.A = B
#         self.size = new_capacity
#
#     def indexing(self, item):
#         # Find the index of the item
#         for i in range(self.n):
#             if self.A[i] == item:
#                 return i
#         return "element not found"
#     def __str__(self):
#         self.result=''
#         for i in range(self.n):
#             self.result +=str(self.A[i])+","
#         return '['+self.result[:-1]+']'
#     def pop(self):
#         if self.n==0:
#             return 'empty'
#         self.n=self.n-1
#     def clear(self):
#         self.n=0
#         self.size=1
#     def find(self,item):
#         if self.n==0:
#             return 'there is no element'
#         else:
#             for i in range(self.n):
#                 if self.A[i]==item:
#                     return "founded element is" ,item, "at" ,i
#     def insert(self,item,index):
#         if self.size==self.n:
#             self.__resize(self.size*2)
#         for i in range(self.n,index,-1):
#             self.A[i]=self.A[i-1]
#         self.A[index]=item
#         self.n =self.n+1
#     def delete(self,position):
#         if position<self.n:
#             for i in range(position,self.n-1):
#                 self.A[i]=self.A[i+1]
#             self.n -=1
#         else:
#             return 'out of index'
#     def remove(self,item):
#         for i in range(self.n):
#             if self.A[i]==item:
#                 self.delete(i)
#                 return "item is found and removed item is",self.A[i],"at",i
#         return "item is not found"





#linked_list
#linked_list support fallowing functions
# node
# create linkedlist
# len
# insert from head
# traverse/print
# insert from tail(append)
# insert in middle(after)
# clear
# delete from head
# dalete from value
# delete from index
# search by index
# search by value
#
# class Node:
#     def __init__(self,value):
#         self.next=None
#         self.data=value
# class linked_list:
#     def __init__(self):
#         self.head=None
#         self.n=0
#
#     def __len__(self):
#         return self.n
#     def insert_at_head(self,value):
#         new_node=Node(value)
#         new_node.next=self.head
#         self.head=new_node
#         self.n=self.n+1
#     def __str__(self):
#         curr=self.head
#         result=''
#         while curr!=None:
#             result=result+str(curr.data)+'->'
#             curr=curr.next
#         return result[:-2]
#
#     def insert_at_tail(self,value):
#         new_node=Node(value)
#         if self.head==None:
#             self.head=new_node
#             self.n=self.n+1
#             return
#         curr = self.head
#         while curr.next!=None:
#             curr=curr.next
#         curr.next=new_node
#         self.n = self.n+1
#     def insert_at_mid(self,after,value):
#         new_node=Node(value)
#         curr=self.head
#         while curr!=None:
#             if curr.data==after:
#                 new_node.next=curr.next
#                 break
#             curr=curr.next
#         if curr!=None:
#             new_node.next=curr.next
#             curr.next=new_node
#         else:
#             return "item not in the list"
#     def clear(self):
#         self.head=None
#         self.n=0
#     def delete_from_head(self):
#         if self.head==None:
#             return "Empty linked list"
#         curr=self.head
#         self.head=curr.next
#         self.n=self.n-1
#     def delete_by_tail(self):
#         if self.head == None:
#             return "empty list"
#         curr=self.head
#         if curr.next == None:
#             return self.delete_from_head()
#         while curr.next.next!=None:
#             curr=curr.next
#         curr.next=None
#         self.n=self.n-1
#
#     def delete_by_value(self,value):
#         curr=self.head
#         if curr.data==value:
#             self.head=curr.next # insted of this we can call the self.delete_head() function
#             self.n = self.n - 1
#         while curr.next!=None:
#             if curr.next.data==value:
#                 break
#             curr=curr.next
#         if curr.next==None:
#             return "item not found"
#         else:
#             curr.next = curr.next.next
#             self.n = self.n - 1
#     def search_by_value(self,value):
#         curr=self.head
#         index=0
#         while curr!=None:
#             if curr.data==value:
#                 return index
#             curr=curr.next
#             index += 1
#         return "not found"
#     def search_by_index(self,index):
#         new_index=0
#         curr=self.head
#         while curr!=None:
#             if new_index==index:
#                 return curr.data
#             curr=curr.next
#             new_index=new_index+1
#         return "item not found"
#     def delete_by_index(self,index):
#         if index<0 or index>=self.n:
#             return "Index out of index"
#         if index==0:
#             return self.delete_from_head()
#         curr=self.head
#         new_index=0
#         while new_index<index-1:
#             curr = curr.next
#             new_index = new_index + 1
#         if curr!=None and curr.next!=None:
#             curr.next = curr.next.next
#             self.n-=1
#
#
# l=linked_list()
# l.insert_at_head(1)
# l.insert_at_head(2)
# l.insert_at_head(3)
# l.insert_at_head(4)
# print(l)
# print(l.delete_by_index(2))

# stack
#it is just like linked list but the but insertion and pop is appened at head only
# the supported methods are
# push
# pop
# is_empty
# peek


# creation_of_stack
# class node:
#     def __init__(self,value):
#         self.data=value
#         self.next=None
# class stack:
#     def __init__(self):
#         self.top=None
#     def is_empty(self):
#         return self.top==None
#     def push(self,value):
#         new_node=node(value)
#         new_node.next=self.top
#         self.top=new_node
#     def traverse(self):
#         temp=self.top
#         while temp!=None:
#             print(temp.data)
#             temp=temp.next
#     def peek(self):
#         if self.top==None:
#             return "stack is empty"
#         else:
#             return self.top.data
#     def pop(self):
#         if(self.is_empty):
#             return "the stack is empty"
#         else:
#             self.top=self.top.next
# s=stack()
# s.push(4)
# s.push(3)
# s.push(2)
# s.push(7)
# s.push(8)
# s.push(9)
# s.traverse()


# Queue



# it support the fallowing function
# enqueue
# dequeue
# traverse
# size
# is_empty

# class Node:
#     def __init__(self,value):
#         self.data=value
#         self.next=None
# class Queue:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def enqueue(self,value):
#         new_node=Node(value)
#         if self.tail==None:
#             self.head=new_node
#             self.tail=self.head
#         else:
#             self.tail.next=new_node
#             self.tail=new_node
#     def dequeue(self):
#         if self.head==None:
#             return 'empty'
#         self.head=self.head.next
#     def travers(self):
#         if self.head==None:
#             return 'empty'
#         temp=self.head
#         while temp!=None:
#             print(temp.data)
#             temp=temp.next
#
# s=Queue()
# s.enqueue(4)
# s.enqueue(6)
# s.enqueue(5)
# s.enqueue(7)
# s.enqueue(9)
# s.enqueue(8)
# s.dequeue()
# s.travers()

# hashing
#hashing is same as array of same elements but it store based on the index value (index values are calculated by element devided by array size)
# if the element is string it will be calculated by converting the string into hashing value using hash function like hash('arun')
#hashing requires mire space
# if the two elements mapping the same index thet it will sovle by using two methods like below
#adjusunt placing and linking
#adjusent means if elements mapping the same index store the first element in the index and next elements in to the next index  like wise
#linkeing means store the linked list as one element to the array
#this will reduce space


# def __init__(self,size):
#     self.size = size
#     self.array=[None]*size
# def hash_value(self,value):
#     return abs(hash(value))*self.size
# def put(self,value):
#     hash_value=self.hash_value(value)
#     if self.array[hash_value]==None:
#         self.array[hash_value]=value
#     else:
#         self.new_hash=self.rehash(hash_value)
#         while self.array[hash_value]!=None:
#             new_hash=self.rehash(new_hash)
# def rehash(self,old_hash):
#     return (old_hash+1) % self.size


              
class node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
class Tree:
    def creat_tree(self,data):
        return node(data)
    def insert_to_tree(self,Node,data):
        if Node is None:
            return self.creat_tree(data)
        if data<Node.data:
            Node.left=self.insert_to_tree(Node.left,data)
        else:
            Node.right=self.insert_to_tree(Node.right,data)
        return Node


tree=Tree()
root=tree.creat_tree(5)
tree.insert_to_tree(5,[2,5,2,6,7,8,4,9])

print(root.data)



