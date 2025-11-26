class Node:
    #Node Creation
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    #Initailizing a Linked List
    def __init__(self):
        self.head=None
    
    def inser_at_end(self,data):
        #add Element at end of Linked List
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            last=self.head
            while last.next:
                last=last.next
            last.next=newnode
        return self.head
    #add Element at the beginning of the Linked List
    def insert_at_begin(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
        return self.head
    #insert Element at a given position
    def insert_at_postion(self,position,data):
        newnode=Node(data)
        if position == 1:
            newnode.next=self.head
            self.head=newnode
            return 
        temp=self.head
        pos=1
        while temp is not None and pos<position-1:
            temp=temp.next
            pos+=1
        if temp is None:
            print("Position out of bounds")
            return
        newnode.next=temp.next
        temp.next=newnode
        return self.head
#delete Element at the beginning of the Linked List
    def linked_list_deletebeginning(self):
        if self.head is None:
            print("List is Empty.")
            return
        temp=self.head
        temp=temp.next
        self.head=temp
        return self.head
#delete Element at end of the Linked List
    def linked_list_deleteend(self):
        if self.head is None:
            print("List is Empty")
            return
        if self.head.next is None:
            self.head=None
            return
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None
        return self.head
#delete Element at a given position
    def linked_list_deleteatpos(self,position):
        if self.head is None:
            print("it is Empty")
            return
        if position==1:
            self.head=self.head.next
        temp=self.head
        pos=1
        while temp is not None and pos<position-1 :
            temp=temp.next
            pos+=1
        temp.next=temp.next.next
        return self.head

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")


link=LinkedList()
link.inser_at_end(10)
link.inser_at_end(20)
link.inser_at_end(30)
link.inser_at_end(40)
link.insert_at_begin(1)
link.insert_at_postion(3,15)
# link.display()
# link.linked_list_deletebeginning()
# link.display()
# link.linked_list_deleteend()
# link.display()
link.inser_at_end(90)
link.inser_at_end(80)
link.display()
link.linked_list_deleteatpos(2)
# link.linked_list_deleteatpos(1)
link.display()
