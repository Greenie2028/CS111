def sort(list_a,list_b):
    a = 0
    b = 0
    a_max = len(list_a) - 1
    b_max = len(list_b) - 1
    sorted_list = []
    while a <= a_max and b <= b_max:
        if list_a[a] < list_b[b]:
            sorted_list.append(list_a[a])
            a += 1
        else:
            sorted_list.append(list_b[b])
            b += 1
    if a_max >= a:
        sorted_list += list_a[a:]
    if b_max >= b:
        sorted_list += list_b[b:]
    return sorted_list


if __name__ == "__main__":
    list_a = [0,1,2,4,6,9]
    list_b = [2,3,5,7]
    print(sort(list_a,list_b))