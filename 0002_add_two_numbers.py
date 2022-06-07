class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
class Solution:
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        tmp = ListNode(0)
        res = tmp
        flag = 0
        while l1 or l2:
            tmpsum = 0
            if l1:
                tmp = l1.val
                l1 = l1.next
            if l2:
                tmp += l2.val
                l2 = l2.next
            tmpres = (tmpsum + flag) % 10
            flag = (tmpsum + flag) / 10
            res.next = ListNode(tmpres)
            res = res.next
        if flag:
            res.next = ListNode(1)

        res = tmp.next
        del tmp
        return res
'''


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        head = res
        step = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            result = x + y + step
            step = result // 10

            head.next = ListNode(result % 10)
            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if step == 1:
            head.next = ListNode(1)

        return res.next

