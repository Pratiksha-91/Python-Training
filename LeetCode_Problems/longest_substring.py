from collections import Counter
inputString = "abcabcbb"

substrings = []
n = len(inputString)

for i in range(n):
    for j in range(i+1,n+1):
        substrings.append(inputString[i:j])

print(substrings)

element_count = Counter(substrings)
print(element_count)
# print("Longest substring is = " + max(element_count))