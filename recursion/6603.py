from itertools import combinations

result = []
nums = list(map(int, input().split()))

while nums[0] != 0:
    coms = list(combinations(nums[1:], 6))
    for com in coms:
        temp = " ".join(map(str, sorted(com)))
        result.append(temp) 
    nums = list(map(int, input().split()))
    result.append("")

for i in result:
    print(i)
    

    