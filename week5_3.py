def zigzag_merge(list1, list2):
    merged = []
    len1, len2 = len(list1), len(list2)
    min_len = min(len1, len2)

    for i in range(min_len):
            merged.append(list1[i])
            merged.append(list2[i])


    if len1 > len2:
        merged.extend (list1[min_len:])
    else:
         merged.extend (list2[min_len:])

    return merged


list_a = [1, 2, 3]
list_b = ['A', 'B', 'C']
print (zigzag_merge(list_a, list_b))

list_c = [1, 2]
list_d = ['A', 'B', 'C', 'D']
print (zigzag_merge(list_c, list_d))

list_e = [1, 2, 3, 4, 5]
list_f = ['A']
print (zigzag_merge(list_e, list_f))
    
