class ListNode:
    def __init__(self , value) -> None:
        self.value = value
        self.prev = None
        self.next = None

        

class MyLinkedList:

    def __init__(self) -> None:
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
         

    def get(self, index: int) -> int:
        curr = self.left.next
        i = 0

        while i < index and curr:
            i += 1
            curr = curr.next
            
        



    def addAtHead(self, index : int) -> None:
        pass
  
    def addAtTail(self, index : int) -> None:
        pass

    def addAtIndex(self, index : int) -> None:
        pass

    
    def deleteAtindex(self, index : int) -> None:
        pass