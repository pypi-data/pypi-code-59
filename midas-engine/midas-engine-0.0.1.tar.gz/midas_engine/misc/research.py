list = [1,2,3,4]

for i in range(len(list)-1,-1,-1):
    print(list[i], type(list[i]))
    list[i] = str(list[i])
    print(list[i], type(list[i]))

print(list[-1])