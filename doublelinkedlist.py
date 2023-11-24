#solution as a singly linked list

class ListNode:
    def __init__(self , val , next_node=None) -> None:
        self.val = val
        self.next = next_node

class MyLinkedList:
    def __init__(self) -> None:
        self.head = ListNode(-1)
        self.tail = self.head
        

    def get(self, index : int ) -> int:
        curr = curr.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1
    
      
    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        # set the next pointer to the new aquired node
        # inserting the new_node before current head node
        new_node.next = self.head.next
        # updates the head.next pointer to the newly acquired node
        # ie new_node == new head
        self.head.next = new_node

        #if we did not have any value then  the new_node also becomes the tail
        if not new_node.next:
            self.tail = new_node


    def addAtTail(self, val: int) -> None:
        # set the value next to the tail where the pinter is at
        self.tail.next = ListNode(val)
        # move the pointer to the new added tail
        self.tail = self.tail.next

    def addAtIndex(self, index:int, val: int) -> None:
        i = 0
        curr = self.head

        while i < index and curr:
            i += 1
            curr = curr.next

            if curr and curr.next:
                curr.next = ListNode(val)
                curr.next = curr.next.next
                # hwo abou the tail
            return "Out of bound / -1 "

    def deleteAtIndex(self, index : int , val : int) -> None:
        i = 0
        curr = self.head

        while i < index  and curr :
             i += 1
             curr = curr.next

             if curr and curr.next:
                 if curr.next == self.tail:
                     self.tail = curr
                 curr.next = curr.next.next
        return "out of bound"  
                      
                 

            

        



        




        

    

    
    









        


        