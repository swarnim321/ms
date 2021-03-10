def nthFromEnd(head , n):
    slow = head
    fast =head
    count =0
    if head == None:
        return
    while (count < n):
        fast = fast.next
        count+=1
    while (slow !=None):
        fast = fast.next
        slow=slow.next
    return slow.data

