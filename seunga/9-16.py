import time
from random import *
from heapSort import *
from seunga.DS_2022134021_SSA import *

def prepare(n: int) -> list:
    A = []
    for i in range(n):
        A.append((int)(1000 * random()))
    return A

def copy(A: list) -> list:
    B = []
    for i in range(len(A)):
        B.append(A[i])
    return B

N = 100000

A = prepare(N)
B = copy(A)
# print(A)

# heapSort 실행 시간 측정
start_time = time.time()
heapSort(B)
end_time = time.time()
heapSort_time = (end_time - start_time) 
# local_time = time.localtime()
# heaptime = local_time.tm_sec
print(f"Heap Sort 소요 시간: {(heapSort_time)} 초")

# print(f"Heap 정렬: {(B)}")
B = copy(A)

# quickSort 실행 시간 측정)
start_time = time.time()
quickSort(B, 0, N-1)
end_time = time.time()
quickSort_time = (end_time - start_time) 
# local_time = time.localtime()
# quick1_time = local_time.tm_sec
print(f"Quick Sort 소요 시간: {(quickSort_time)} 초")
# print(f"Quick 정렬: {(B)}")
# B = copy(B)

# quickSort 실행 시간 측정 (두 번째 호출)
start2_time = time.time()
quickSort(B, 0, N-1)
end2_time = time.time()
quickSort2_time = (end2_time - start2_time) 
print(f"Quick Sort (두 번째 호출) 소요 시간: {(quickSort2_time)} 초")
# print(f"Quick 정렬: {(B)}")
