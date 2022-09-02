n,k = map(int, input('n, k 입력 : ').split())
a = list(map(int, input('list1원소 입력 : ').split()))
b = list(map(int, input('list2원소 입력 : ').split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i],b[i] = b[i],a[i]
    else:
        break


print(sum(a))
