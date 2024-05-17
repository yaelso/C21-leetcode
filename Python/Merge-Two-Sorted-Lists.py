class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

def print_linked_list(head):
    current = head
    res = []

    while current:
        res.append(current.val)
        current = current.next

    print(res)


list1 = create_linked_list([1,2,4])
list2 = create_linked_list([1,3,4])


def mergeTwoLists(list1, list2):
    curr = dummy = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next

        curr = curr.next

    curr.next = list1 if list1 else list2

    return dummy.next

# Alternative Solution 1:

def mergeTwoListsAlt2(list1, list2):
    if not list1 or not list2:
        return list1 or list2

    if list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2
