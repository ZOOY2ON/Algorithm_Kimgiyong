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
	child = 2*k+1	 # 왼자식
	right = 2*k+2	 # 오른자식
	if child <= end:
			if right <= end and A[child] < A[right]:
					child = right
			# child: A[2k+1]와 A[2k+2] 중에 큰 원소의 인덱스
			if A[k] < A[child]:
				A[k], A[child] = A[child], A[k]
				percolateDown(A, child, end)

# 코드 9-7