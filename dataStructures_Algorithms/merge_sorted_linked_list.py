def mergeLists(head1, head2):
    main = temp = node()
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    while head1 is not None or head2 is not None:
        if head1.data <head2.data:
            current = head1.data
            head1 =head1.next
        if head2.data < head1.data:
            current = head2.data
            head2=head2.next
        temp.next = current
        temp = temp.next
    return if __name__ == '__main__':



[[][] ]