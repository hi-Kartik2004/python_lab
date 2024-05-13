# Create dict with count of each element?
#  dict = {“123”:2, “234”:1, “345”:2, “abc”:3, xyz:1}

def checker(list, ele):
    for el in list:
        if(ele == el):
            return True
    
    return False

def frequency(list):
    dict = {}
    for ele in list:
        if(checker(dict.keys(), ele)):
            dict[ele] += 1
        else:
            dict[ele] = 1
    return dict

list = ["123", "123", "234", "345", "abc", "xyz"]
print(frequency(list))