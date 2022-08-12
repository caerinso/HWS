mystr = 'algorithm'
#1. 파이썬 내장 기능
print(mystr[::-1])
arr = list(mystr)
print(arr)

#for
mystr = 'algorithm'
arr = list(mystr)
for i in range(len(arr)//2):
    arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
print(arr)









