from itertools import permutations

s1 = input().strip()
s2 = input().strip()
final = input().strip()

a = set(s1) | set(s2) | set(final)

if len(a) > 10:
    print("No")

else:
    for i in permutations(range(10), len(a)):

        d = dict(zip(a, i))
        
        p = ''.join(str(d[i]) for i in s1)
        q = ''.join(str(d[i]) for i in s2)
        s = ''.join(str(d[i]) for i in final)

        if int(s) == int(p) + int(q):
            print(d)
            print('YES')
            break
    else:
        print("No solution")