# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        l = 0
        ret = []
        while cur:
            l+=1
            cur = cur.next
        
        cur = start = head
        cur_len = 0
        extra_parts = l % k
        while cur:
            cur_len += 1
            if (cur_len == l//k and extra_parts < 1) or (cur_len == l//k + 1):
                extra_parts -= 1
                temp = cur.next #next part's head
                cur.next = None
                ret.append(start)
                cur = start = temp
                cur_len = 0
            else:
                cur = cur.next
        return ret + [cur for _ in range(k-len(ret))]
    
    
    Time: O(N)
    Space: O(1)
