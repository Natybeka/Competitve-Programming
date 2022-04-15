from turtle import right
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    summation = ListNode()
    sumDigit = summation
    left = l1
    right = l2
    carry = 0
    while left or right:
        leftValue = left.val if left else 0
        rightValue = right.val if right else 0
        digitSum = leftValue + rightValue + carry

        carry = 0 if digitSum > 10 else digitSum // 10
        sumDigit.val = digitSum % 10
        left = left.next if left else None
        right = right.next if right else None
        if left or right:
            sumDigit.next = ListNode(carry)
            sumDigit = sumDigit.next
    if carry > 0:
        sumDigit.next = ListNode(carry)
    return summation
