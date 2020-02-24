import time
import sys
sys.path.append('C:/Users/nchib/DS5/Data-Structures/doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
start_time = time.time()

f = open('C:/Users/nchib/DS5/Sprint-Challenge--Data-Structures-Python/names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('C:/Users/nchib/DS5/Sprint-Challenge--Data-Structures-Python/names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names_f = names_1 + names_2
names_f.sort()

dll = DoublyLinkedList()
for name_f in names_f:
    dll.add_to_tail(name_f)

def findDuplicates(self,head):
        duplicates = []  # Return the list of duplicates in this data structure
        p1 = head
        p2 = head.next
        while p2 is not None:
            # increment both pointers UNTIL they are
            while p2 is not None and p1.value != p2.value:
                p1 = p1.next
                p2 = p2.next
            while p2 is not None and p1.value == p2.value:
                duplicates.append(p1.value)
                # incrememnt p2
                p1 = p1.next
                p2 = p2.next
                
        return duplicates

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#SOLUTION WITH LINKED LIST
duplicates = findDuplicates(dll, dll.head)

#SOLUTION WITH LIST COMPREHENSION
# duplicates =  [x for x in names_1 if x in names_2]

#SOLUTION WITH PYTHON SETS
# def intersection(lst1, lst2): 
#     return list(set(lst1) & set(lst2))

# duplicates = intersection(names_1,names_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
