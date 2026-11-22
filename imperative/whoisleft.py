n = int(input())
arr = list(range(1, n + 1))

def eliminate(arr):
    phase = 0
    while len(arr) > 1:
        if phase == 0:
            arr = remove_even(arr)
        elif phase == 1:
            arr = remove_odd(arr)
        else:
            arr = remove_thirds(arr)

        phase = (phase + 1) % 3

    return arr[0]

def remove_even(arr):
    return [number for pos, number in enumerate(arr, 1)
            if pos % 2 != 0]

def remove_odd(arr):
    return [number for pos, number in enumerate(arr, 1)
            if pos % 2 == 0]

def remove_thirds(arr):
    return [number for pos, number in enumerate(arr, 1)
            if pos % 3 != 0]

print(eliminate(arr))