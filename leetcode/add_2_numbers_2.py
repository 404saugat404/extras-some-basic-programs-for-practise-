

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sum_num(self,a,b):
        head=ListNode(0)
        root=head
        carry=0

        while a or b:
            v1=a.val if a else 0
            v2=b.val if b else 0

            sum=v1+v2+carry

            value=sum%10
            head.next=ListNode(value)
            head=head.next
            carry=sum//10


            if a:
                a.next=a
            
            if b:
                b.next=b

        if carry:
            head.next=ListNode(carry)

        return root.next


