# merge sort

def merge_sort(list):
    if(len(list) <= 1):
        return list
    leftHalf = list[:(len(list)//2)]
    rightHalf = list[(len(list)//2): ]

    # print(leftHalf, rightHalf)

    resp1 = merge_sort(leftHalf)
    resp2 = merge_sort(rightHalf)
    return merge(resp1, resp2)

def merge(leftHalf, rightHalf):
    merged = []
    i = j = 0

    while(i < len(leftHalf) and j < len(rightHalf)):
        if (leftHalf[i] < rightHalf[j]):
            merged.append(leftHalf[i])
            i += 1
        else:
            merged.append(rightHalf[j])
            j += 1

    merged.extend(leftHalf[i: ])
    merged.extend(rightHalf[j: ])

    return merged


print(merge_sort([5,4,3,2,1]))


