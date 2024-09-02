class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next


class solution(ListNode):
    def remove_nth_node(self,head,n):
        #creating a dummy
        dummy=ListNode

        #defining left and right pointer for linked list
        left=dummy

        #since we cant write right=right+2 to shift the node, we need to write below code to shift right by 2
        right=head
        
        while n>0 and right:
            right=right.next
            n=n-1

        while right:
            left=left.next
            right=right.next
        
        left.next=left.next.next

        return dummy.next