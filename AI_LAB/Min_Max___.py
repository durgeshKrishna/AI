import math

def Min_Max(cd, node, maxt, src, td):
    if cd == td:
        return src[node]
    
    left = Min_Max(cd + 1, node * 2, not maxt, src, td)
    right = Min_Max(cd + 1, node * 2 + 1, not maxt, src, td)

    if left is None:
        return right
    if right is None:
        return left
    
    return max(left, right) if maxt else min(left, right)

src = list(map(int, input("leaf nodes: ").split()))

n = len(src)
next_2 = 2 ** math.ceil(math.log2(n))

src.extend([None] * (next_2 - n))
td = math.ceil(math.log2(len(src)))

print(src,"\nTotal Depth:",td)
cd = 0
node = 0
maxt = True
answer = Min_Max(cd, node, maxt, src, td)
print("Optimal Val: ", answer)