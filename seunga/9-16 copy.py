import sys

# 재귀 깊이 제한을 늘립니다 (필요에 따라 조절)
sys.setrecursionlimit(10**6)

def quickSort(A, p:int, r:int):
   if p < r:
       q = partition(A, p, r)    # 분할
       quickSort(A, p, q-1)    # 왼쪽 부분 리스트 정렬
       quickSort(A, q+1, r)    # 오른쪽 부분 리스트 정렬

def partition(A, p:int, r:int) -> int:
   x = A[r]               # x: 기준 원소
   i = p-1               # i: 1구역의 끝 지점
   for j in range(p, r):   # j: 3구역의 시작 지점
      if A[j] < x:
         i += 1
         A[i], A[j] = A[j], A[i]  # 교환
   A[i+1], A[r] = A[r], A[i+1]      # 기준 원소와 2구역 첫 원소 교환
   return i+1

def heapSort(A):
   buildHeap(A)
   for last in range(len(A)-1, 0, -1):
      A[last], A[0] = A[0], A[last]
      percolateDown(A, 0, last-1)

def buildHeap(A): # 리스트 A[0...len(A)-1]을 힙으로 만든다
   for i in range((len(A)-2) // 2, -1, -1):
      percolateDown(A, i, len(A)-1)

# A[k]를 루트로 하는 서브 트리가 A[k...end] 범위 내에서 힙 특성을 만족하도록 수선
# 주어진 조건: A[k]의 두 자식을 루트로 하는 서브 트리는 힙 특성을 만족함
def percolateDown(A, k:int, end:int):
   child = 2*k+1    # 왼자식
   right = 2*k+2    # 오른자식
   if child <= end:
         if right <= end and A[child] < A[right]:
               child = right
         # child: A[2k+1]와 A[2k+2] 중에 큰 원소의 인덱스
         if A[k] < A[child]:
            A[k], A[child] = A[child], A[k]
            percolateDown(A, child, end)

import time
import random
import numpy as np
import matplotlib.pyplot as plt

def prepare(n:int) ->list:
    A= []
    for i in range(n):
        A.append((int)(1000*random.random()))
    return A

def copy(A:list):
    B = []
    for i in range(len(A)):
        B.append(A[i])
    return B

x_values = np.array([])
y_values = np.array([])

x_values = np.arange(1,100000,1000) 

for N in x_values:
    A = prepare(N)
    B=copy(A)
    
    # start = time.time()
    # heapSort(B)
    # curr = time.time() - start   
    # print(N,"힙 정렬 소요 시간", curr) 
    
    # start = time.time()
    # quickSort(B,0,N-1)
    # curr = time.time() - start
    # print(N,"첫 번째 퀵 정렬 소요시간",curr)
    
    start = time.time()
    quickSort(B,0,N-1)
    start = time.time()
    quickSort(B,0,N-1)
    curr = time.time() - start
    print(N,"두 번째 퀵 정렬 소요시간", curr)
    
    y_values = np.append(y_values, float(curr))
    
 
x_values = x_values.reshape(-1, 1)
y_values = y_values.reshape(-1, 1)
x_min = np.min(x_values)
x_max = np.max(x_values)
K = int(input("K값을 입력 :"))

uk = []
for i in range(K):
    uk.append(x_min + (x_max - x_min) * i / (K - 1))

sigma = (x_max - x_min) / (K - 1)
print(sigma)
print(uk)

basic_func = []
gauss = np.zeros((len(x_values), 0))

for i in range(K):
    basic_func = np.exp(-1/2 * ((x_values - uk[i]) / sigma) ** 2)
    gauss = np.column_stack((gauss, basic_func))

ones_matrix = np.ones((len(x_values), 1))
gauss = np.column_stack((gauss, ones_matrix))
#print(gauss)

XT = np.transpose(gauss)
XTX = XT @ gauss
IXTX = np.linalg.inv(XTX)
IXTXXT = IXTX @ XT
w = IXTXXT @ y_values
print(w)

x_range = np.linspace(min(x_values), max(x_values), 100) 
y_range = np.zeros((100, 1))
for i in range(K):
    y_range += w[i][0] * np.exp(-1/2 * ((x_range - uk[i]) / sigma) ** 2)

y_range += w[K][0]

plt.figure(figsize=(10, 6))  
plt.scatter(x_values, y_values, c='blue', marker='o', label='Data Point')  
plt.plot(x_range, y_range, color='red', label='Predicted Line')  
plt.xlabel('N')
plt.ylabel('소요 시간') 
plt.title('힙 정렬 소요 시간')  
plt.legend(loc='upper left')  
plt.grid(True)

plt.show()
    # B=copy(A)
    
    # start = time.time()
    # quickSort(B,0,N-1)
    # curr = time.time() - start
    # print("첫 번째 퀵 정렬 소요시간",curr) 
    
    # start = time.time()
    # quickSort(B,0,N-1)
    # curr = time.time() - start
    # print("두 번째 퀵 정렬 소요시간", curr)