class Link:
    def __init__(self,value):
        self.value: int = value
        self.next: Link = None


l1 = Link(3)
l2 = Link(9)
l3 = Link(7)
l4 = Link(11)
this_is_my_variable_that_stores_a_data_type_of_a_link_in_a_linked_list_that_I_use_to_store_the_fifth_link_in_my_linked_list_as_a_way_to_make_a_more_efficient_list = Link(12)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = this_is_my_variable_that_stores_a_data_type_of_a_link_in_a_linked_list_that_I_use_to_store_the_fifth_link_in_my_linked_list_as_a_way_to_make_a_more_efficient_list
# Write a function that writes the whole chain given the first link.
def print_chain(link):
    print(link.value, end=" -> ")
    if link.next == None: return
    print_chain(link.next)

print_chain(l1)
print()
def reverse_list(head, previous = None):
    if head.next == None:
        head.next = previous
        return
    reverse_list(head.next, head)
    head.next = previous

def reverse_list(head):
    p = None
    c = head
    n = head.next if head else None

    while n != None:
        c.next = p
        p = c
        c = n
        n = n.next
    return c

reverse_list(l1)
print_chain(this_is_my_variable_that_stores_a_data_type_of_a_link_in_a_linked_list_that_I_use_to_store_the_fifth_link_in_my_linked_list_as_a_way_to_make_a_more_efficient_list)