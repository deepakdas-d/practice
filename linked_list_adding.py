l2 = [5,6,4]
l1 = [9,9,9,9,9,9,9]
class ListNode:
         def __init__(self, val, next=None):
            self.val = val
            self.next = next

class Problem:
      def list_to_linkedlist(self,arr):
            self.head=ListNode(arr[0])
            temp=self.head
            for i in range(1,len(arr)):
                  temp.next=ListNode(arr[i])
                  temp=temp.next
            return self.head 
############################################################################## 
      def addtwonum(self,l1,l2):
            l=ListNode(self)
            current=l
            carry=0
            while l1 or l2 or carry:
                  x=l1.val if l1 else 0
                  y=l2.val if l2 else 0
                  total=x+y+carry
                  carry=total//10
                  digit=total%10
                  current.next=ListNode(digit)
                  current=current.next
                  if l1: l1=l1.next
                  if l2: l2=l2.next
            return l.next

############################################################################## 
      def print_list(self,head):
            temp=head
            while temp:
                  print(temp.val,end="->")
                  temp=temp.next
            print("None")
############################################################################## 

p = Problem()

list1 = p.list_to_linkedlist(l1)
p.print_list(list1)

list2 = p.list_to_linkedlist(l2)
p.print_list(list2)

res = p.addtwonum(list1, list2)
p.print_list(res)
