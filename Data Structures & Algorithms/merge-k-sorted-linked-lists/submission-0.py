# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #empty list handling
        if not lists:
            return 

        flag = True

        for l in lists:
            if l != []:
                flag = False

        if flag:
            return

        #not empty list handling

        # lists = sorted(lists, key = len, reverse = True)

        #first, rewrite the merge two sorted lists code
        
        for i in range(len(lists)-1):
            l_1 = lists[0]
            head_1 = lists[0]
            curr_1 = head_1
            l_2 = lists[i+1]
            head_2 = lists[i+1]
            curr_2 = head_2
            dummy = ListNode(0)
            real_head = dummy
            while curr_1 and curr_2:
                if curr_1.val < curr_2.val:
                    dummy.next = curr_1
                    curr_1 = curr_1.next
                else:
                    dummy.next = curr_2
                    curr_2 = curr_2.next
                dummy = dummy.next
            if curr_1:
                dummy.next = curr_1
            else:
                dummy.next = curr_2
            lists[0] = real_head.next
        return lists[0]


        





