# Develop a program that accept the list and iterates over a list of
# numbers first and prints the numbers in the list whose square is
# divisible by 8

def divisibleBy8(list):
    ans = []
    for ele in list:
        if(ele % 8 == 0):
            ans.append(ele)
    return ans

inputList = []

n = int(input("Enter the size of the arr: "))
for i in range(n):
    inputList.append(int(input("Enter the val: ")))

print(divisibleBy8(inputList))