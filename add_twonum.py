l1=[0]
l2=[0]
l1.reverse()
l2.reverse()
l1 = int(''.join(map(str, l1)))
l2= int(''.join(map(str, l2)))
output=l1+l2
a = list(map(int, str(output)))
a.reverse()
print (a)

class Solution:
    def addTwoNumbers(self, l1:list, l2: list) -> list:
        l1.reverse()
        l2.reverse()
        l1 = int(''.join(map(str, l1)))
        l2= int(''.join(map(str, l2)))
        output=l1+l2
        output=list(map(int, str(output)))
        output.reverse()
        return output



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1.val
        l2.val
        l1.reverse()
        l2.reverse()
        l1 = int(''.join(map(str, l1)))
        l2= int(''.join(map(str, l2)))
        output=l1+l2
        output=list(map(int, str(output)))
        output.reverse()
        return output