# This program reverses a string
txt = input("Enter any string to reverse: \n")[::-1]
# print(len(txt))
x = length = len(txt) - 1
arr = []
while(x>=0):
    print(x)
    sz = length - x
    arr.append(txt[x])
    x = x-1
print(arr)
print(txt)
