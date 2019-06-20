// using LinkedList to implement stack with 4 basic operations:
//    1. Push(item)
//    2. Pop()
//    3. Peek()
//    4. isEmpty()
public class stackClassUsingLinkedList {
    Node top;
    stackClassUsingLinkedList() {
        this.top = null;
    }
    private class Node {
        int data; // data
        Node link; // the rest of stack.
    }
    // Insert in the beginning.
    public void push(int newElement) {
        // create new node temp and allocate memory
        Node temp = new Node();

        if (temp == null) System.out.print("\nHeap Overflow");
        temp.data = newElement;
        temp.link = null;
        // add to the top of the list.
        top = temp;
    }
    // Pop the elements.
    public void pop() {
        // check for stack underflow
        if (top == null) {
            System.out.print("\nStack Underflow");
            return;
        }

        // update the top pointer to point to the next node
        top = (top).link;

    }
    // Return top element in a stack
    public int peek() {
        // check for empty stack
        if (!isEmpty()) {
            return top.data;
        }
        else {
            System.out.println("Stack is empty");
            return -1;
        }
    }
    // Check if the stack is empty or not
    public boolean isEmpty() {
        return top == null;
    }

    // threeStackinOneArray

}
