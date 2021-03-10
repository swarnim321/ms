def delete_node(head, key):
    prev = None
    current = head
    while current!=None:
        if current.data == key:
            if current == head:
                head = current.next
                current = head
            else:
                prev.next = current.next
                current  = current.next
        else:
            prev= current
            current = current.next
    if current ==None:
        return head
    return head



