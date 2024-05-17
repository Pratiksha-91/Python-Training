l1 = [3,4,8]
l2 = [5,6,4]

l2.reverse()

result = [i+j for i,j in zip(l1,l2)]
result.reverse()
print(result)

