arr=[1,2,3,4,5]

def insert(arr,index,successor):
    for index in range(index,len(arr)):
        arr[index],successor=successor,arr[index]

        arr.append(successor)

print("Array before insertion:",arr)
insert(arr,3,4)
print("Array after insertion:",arr)