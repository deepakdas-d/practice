head=[1,2,3,4,5]
class Node:
    #Node Creation
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
########################################################
    def linked_list(self,arr):
        self.head=Node(arr[0])
        temp=self.head
        for i in range(1,len(arr)):
            temp.next=Node(arr[i])
            temp=temp.next
        return self.head
#########################################################
    def reverse(self):
        temp=self.head
        prev=None
        while temp is not None:
            nxt=temp.next
            temp.next=prev
            prev=temp
            temp=nxt
        self.head=prev
        return self.head
#########################################################
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

l=LinkedList()
l.linked_list(head)
l.display()
l.reverse()
l.display()

