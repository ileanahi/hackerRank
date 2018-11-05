function insertNodeAtTail(head, data) {
    if (head == null) {
        head = new SinglyLinkedListNode();
        head.data = data;
    } else {
        let node = head;
        while (node.next != null) {
            node = node.next;
        }
        node.next = new SinglyLinkedListNode();
        node.next.data = data;
    }
    return head;

}