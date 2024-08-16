class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class merge_and_sort(object):
    def m_n_s(self,l1,l2):
        head=ListNode()
        temp1=l1
        temp2=l2
        temp3=head

        while(temp1 is not None and temp2 is not None):
            if(temp1.val<=temp2.val):
                temp3.next=temp1
                temp1=temp1.next

            else:
                temp3.next=temp2
                temp2=temp2.next
            
            temp3=temp3.next

        if(temp1 is not None):
            temp3.next=temp1
        
        if(temp2 is not None):
            temp3.next=temp2
        
        head=head.next
        return head
    
l1=[1,2,5,6]


l2=[1,2,5,5,4]

abc=merge_and_sort.m_n_s(l1,l2)
print(abc)