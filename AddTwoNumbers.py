# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def get_data(self):
        return self.val
    
    def get_next(self):
        return self.next
    
    def set_next(self,new_next):
        self.next = self.new_next
    
    def insert(self,val):
        new_next = ListNode(val)
        new_next.set_next(self.val)
        self.val = new_next
    
    def print_Linked_List(self):
        node = self
        while node != None:
            print node.val
            node = node.next
    
    def create_int_array_linked(self):
        node = self
        linkintoString = []
        while node!= None:
            linkintoString.append(node.val)
            node = node.next
        print list(reversed(linkintoString))
        return list(reversed(linkintoString))




class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_list = l1.create_int_array_linked()
        l2_list = l2.create_int_array_linked()
        
        #[x + y for x, y in zip(first, second)]
        summed_list = [x + y for x, y in zip(l1_list, l2_list)]
        return list(reversed(summed_list))
        #return sum_of_two_list

        

def main():
    # first linked list
    node = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node.next = node2
    node2.next = node3 
    # second linked list
    list1 = ListNode(2)
    list2 = ListNode(6)
    list3 = ListNode(8)
    list1.next = list2
    list2.next = list3
    
    summation_list = Solution()
    summed_list = summation_list.addTwoNumbers(node,list1)
    print (summed_list)

    # pointing back to linked list
    

if __name__ == "__main__":
    main() 