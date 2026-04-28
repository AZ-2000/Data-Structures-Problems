# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        curr_2 = l2
        carry = 0
        head = None

        while curr and curr_2:
            if curr.val+curr_2.val+carry < 10:
                new_node = ListNode(curr.val+curr_2.val+carry)
                if not head:
                    head = new_node
                else:
                    old_node.next = new_node
                carry = 0
                old_node = new_node
            else:
                new_node = ListNode((curr.val+curr_2.val+carry)%10)
                carry = (curr.val+curr_2.val+carry)//10
                if not head:
                    head = new_node
                else:
                    old_node.next = new_node
                old_node = new_node
            curr = curr.next
            curr_2 = curr_2.next

        if curr:
            if carry == 0:
                while curr:
                    new_node = ListNode(curr.val)
                    old_node.next = new_node
                    old_node = new_node
                    curr = curr.next
            else:
                while curr:
                    if curr.val + carry >= 10:
                        new_node = ListNode((curr.val+carry)%10)
                        carry = (curr.val+carry)//10
                        if not head:
                            head = new_node
                        else:
                            old_node.next = new_node
                        old_node = new_node
                    else:
                        new_node = ListNode(curr.val+carry)
                        carry = 0
                        if not head:
                            head = new_node
                        else:
                            old_node.next = new_node
                        old_node = new_node
                    curr = curr.next
                    

        elif curr_2:
            if carry == 0:
                print("here",curr_2.val,carry)
                while curr_2:
                    new_node = ListNode(curr_2.val)
                    old_node.next = new_node
                    old_node = new_node
                    curr_2 = curr_2.next
            else:
                while curr_2:
                    if curr_2.val + carry >= 10:
                        new_node = ListNode((curr_2.val+carry)%10)
                        carry = (curr_2.val+carry)//10
                        if not head:
                            head = new_node
                        else:
                            old_node.next = new_node
                        old_node = new_node
                    else:
                        new_node = ListNode(curr_2.val+carry)
                        carry = 0
                        if not head:
                            head = new_node
                        else:
                            old_node.next = new_node
                        old_node = new_node
                    
                    curr_2 = curr_2.next
        if carry != 0:
            print(carry)
            new_node = ListNode(carry)
            old_node.next = new_node
            
        return head


        


        