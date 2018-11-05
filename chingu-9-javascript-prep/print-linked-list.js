function printLinkedList(head) {
    if (head == null) {
        return;
    }
    let node = head;
    while (true) {
        console.log(node.data);
        if (node.next !== null) {
            node = node.next;
        } else {
            break;
        }
    }
}