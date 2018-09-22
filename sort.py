# several sort function 1.fast_sort 2.merge_sort 3...

# fast-sort
def fast_sort(List):
    if len(List) <= 1:
        return List
    label = List[0]
    i = 1
    j = len(List)-1
    while i <= j:
        if List[i]<=label:
            i += 1
        if List[j] >label:
            j -= 1
        if i<j:
            temp = List[i]
            List[i] = List[j]
            List[j] = temp
    A = List[1:min(i,j) + 1]
    B = List[max(j,i):]
    A_sorted = fast_sort(A)
    B_sorted = fast_sort(B)
    List_sorted = []
    List_sorted.extend(A_sorted)
    List_sorted.append(label)
    List_sorted.extend(B_sorted)
    return List_sorted


# merge sort with recurrise
def merge_sort(List):
    if len(List) <= 1:
        return List
    Left = List[:round(len(List)/2)]
    Right = List[round(len(List)/2):]
    Left_sorted = merge_sort(Left)
    Right_sorted = merge_sort(Right)
    List_sorted =[]
    i = 0
    j = 0
    while i<len(Left_sorted) and j<len(Right_sorted):
        if Left_sorted[i] <= Right_sorted[j]:
            List_sorted.append(Left_sorted[i])
            i +=1
        else:
            List_sorted.append(Right_sorted[j])
            j +=1
    List_sorted.extend(Left_sorted[i:])
    List_sorted.extend(Right_sorted[j:])
    return List_sorted




