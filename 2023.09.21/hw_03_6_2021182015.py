array = [
       46,      82,      21,      58,      22,      54,      71,     215,      99,     227, 
       73,      24,      17,      44,     244,      78,      25,      66,      47,       3, 
       87,      33,     312,     242,      42,      61,     348,     346,      98,      92, 
       83,     100,      94,      40,       5,     458,     364,      26,      64,      35, 
       90,     489,      72,     504,      88,      97,     226,     218,     186,      68, 
]

def sort_bubble(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    print('-' * 60)
    print(f'before: {arr}')
    print(f'after : {arr}')


def sort_select(arr):
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    print('-' * 60)
    print(f'before: {arr}')
    print(f'after : {arr}')


def sort_insert(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    print('-' * 60)
    print(f'before: {arr}')
    print(f'after : {arr}')


def sort_shell(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    
    print('-' * 60)
    print(f'before: {arr}')
    print(f'after : {arr}')


def main():
  print('\n[ Bubble Sort ]\n')
  sort_bubble(array[:])
  print('\n[ Insert Sort ]\n')
  sort_insert(array[:])
  print('\n[ Select Sort ]\n')
  sort_select(array[:])
  print('\n[ Shell Sort ]\n')
  sort_shell(array[:])

if __name__ == '__main__':
  main()

