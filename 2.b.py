def frequency(string):
    dict={}
    for char in string:
        if(char in dict):
            dict.update({char: dict.get(char) + 1})
        else:
            dict[char] = 1

    return dict

resp = frequency("Hello world")
print(resp)

# Testing removing a key
resp.pop('d')
print(resp) # pair with dict removed