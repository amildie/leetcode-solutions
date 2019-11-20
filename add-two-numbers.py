# https://leetcode.com/problems/add-two-numbers/

class Solution:
    def __init__(self):
        self.head = None
        self.res = self.head
        self.acc = 0

    def addNode(self, n: ListNode):
        # Iterate through the list, add at the end - O(n)
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = n
        else:
            self.head = n
            self.res = self.head
            
    def addNodeToRes(self, val1, val2):
        # Calculate value for the new node and update accumulator
        newVal = val1 + val2 + self.acc
        if newVal > 9:
            self.acc = 1
            newVal -= 10
        else:
            self.acc = 0
       
        self.addNode(ListNode(newVal))

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Iterate simultaneously through both lists  - O(max(len(l1),len(l2)))
        i1 = l1
        i2 = l2
        while i1 != None and i2 != None:
            self.addNodeToRes(i1.val, i2.val)
            i1 = i1.next
            i2 = i2.next

        # Iterate through the remainder of the longest list (if it exists)
        i3 = i2 if i1 == None else i1
        while i3:
            self.addNodeToRes(0, i3.val)
            i3 = i3.next
        
        # Add the accumulator (if it exists)
        if self.acc == 1:
            self.addNodeToRes(0, 0)
        
        return self.res
