
n = int(input())
arr = list(range(1, n + 1))
phase = 0

while len(arr) > 1:
    arr2 = []
    for i in range(len(arr)):
        curr = i + 1

        if phase == 0:
            if curr % 2 != 0:
                arr2.append(arr[i])

        elif phase == 1:
            if curr % 2 == 0:
                arr2.append(arr[i])

        elif phase == 2:
            if curr % 3 != 0:
                arr2.append(arr[i])

    arr=arr2

    phase+=1

    if phase == 3:
        phase = 0

print(arr[0])
