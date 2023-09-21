array = [
       46,      82,      21,      58,      22,      54,      71,     215,      99,     227, 
       73,      24,      17,      44,     244,      78,      25,      66,      47,       3, 
       87,      33,     312,     242,      42,      61,     348,     346,      98,      92, 
       83,     100,      94,      40,       5,     458,     364,      26,      64,      35, 
       90,     489,      72,     504,      88,      97,     226,     218,     186,      68, 
]

def sort_bubble(arr):
  print('-' * 60)
  print(f'before: {arr}')

  count = len(arr)
  for a in range(count - 1):
    for b in range(count - 1 - a):
      if arr[b] > arr[b + 1]:  # 현재 원소가 다음 원소보다 큰 경우
        arr[b], arr[b + 1] = arr[b + 1], arr[b]  # 위치를 변경

  print(f'after : {arr}')


def sort_select(arr):
    print('-' * 60)
    print(f'before: {arr}')

    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    print(f'after : {arr}')


def sort_insert(arr):
    print('-' * 60)
    print(f'before: {arr}')

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    print(f'after : {arr}')


def sort_shell(arr):
    print('-' * 60)
    print(f'before: {arr}')
    n = len(arr)
    gap = n // 2  # 초기 갭 설정

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # 갭을 줄여나감

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

