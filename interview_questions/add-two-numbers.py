"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# function to add nodes to a SLL
def add(val):
    new_node = ListNode(val=val)
    return new_node


# convert a string to a SLL
def string_to_sll(text, head=None):
    # reverse the text
    text = text[::-1]
    head = add(int(text[0]))
    current = head
    for i in range(len(text) - 1):
        current.next = add(text[i + 1])
        current = current.next
    return head


# print sll
def print_sll(head: ListNode):
    current = head
    while current is not None:
        print(current.val)
        current = current.next


def sll_to_string(head: ListNode):
    current = head
    ret_str = ""
    while current is not None:
        ret_str += str(current.val)
        current = current.next
    return ret_str[::-1]


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> \
            Optional[ListNode]:
        int1 = int(sll_to_string(l1))
        int2 = int(sll_to_string(l2))
        sol_int = int1 + int2
        sol_str = str(sol_int)
        return string_to_sll(sol_str)


num_1_sll = string_to_sll("942")
num_2_sll = string_to_sll("9465")

t1 = Solution()
print_sll(t1.addTwoNumbers(num_1_sll, num_2_sll))
