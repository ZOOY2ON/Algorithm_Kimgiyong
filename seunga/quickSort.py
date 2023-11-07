import time

# def quickSort(A, p, r):
#     if p < r:
#         q = partition(A, p, r)  # 분할
#         quickSort(A, p, q - 1)  # 왼쪽 부분 리스트 정렬
#         quickSort(A, q + 1, r)  # 오른쪽 부분 리스트 정렬

# def partition(A, p, r):
#     x = A[r]  # x: 기준 원소
#     i = p - 1  # i: 1구역의 끝 지점
#     for j in range(p, r):
#         if A[j] < x:
#             i += 1
#             A[i], A[j] = A[j], A[i]  # 교환
#     A[i + 1], A[r] = A[r], A[i + 1]  # 기준 원소와 2구역 첫 원소 교환
#     return i + 1


def quickSort(A, p, r):
    if p < r:
        q1, q2 = partition(A, p, r)  # 분할
        quickSort(A, p, q1 - 1)     # 왼쪽 부분 리스트 정렬
        quickSort(A, q2 + 1, r)     # 오른쪽 부분 리스트 정렬

def partition(A, p, r):
    x = A[r]  # x: 기준 원소
    i = p - 1  # i: 1구역의 끝 지점
    j = p  # j: 현재 검사 중인 원소

    while j <= r - 1:
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]  # 교환
        elif A[j] == x:
            A[r], A[j] = A[j], A[r]  # 동일한 원소를 2구역으로 이동
            r -= 1
            j -= 1
        j += 1

    A[i + 1], A[r] = A[r], A[i + 1]  # 기준 원소와 2구역 첫 원소 교환
    return i + 1, r


from random import *

def prepare(n:int) ->list:
    A=[]
    for i in range(n):
        A.append((int)(1000*random()))
    return A
    
N = 100000

A = prepare(N)
start = time.time()
quickSort(A, 0, len(A) - 1)
end = time.time()
total = end-start
print(f"{total}초")