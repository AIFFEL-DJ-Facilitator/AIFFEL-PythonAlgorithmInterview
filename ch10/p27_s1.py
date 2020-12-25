"""
27. k개 정렬 리스트 병합

[1 -> 4 -> 5,
1 -> 3 -> 4,
2 -> 6
]

1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
"""

import heapq
"""
heapq.heappush(heap, item) : item을 heap에 추가
heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨. 
heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )

heapq가 자동적으로 정렬해주는 속성을 이용한 방법입니다.
"""


def func(self, lists):
    root = result = ListNode(None)
    heap = []

    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i])) # 연결리스트를 heap에 heapq 데이터로 입력하면 lists[i].value기준으로 정렬 됩니다.
    
    while heap: # heap에서 하나씩 꺼내 result를 만들어 줍니다.
        node = heapq.heappop(heap) # 각 node는 각각 연결리스트의 값, 인덱스, 연결리스트 자체가 저장되어 있습니다.
        idx = node[1]
        result.next = node[2] # 맨 위에서 만든 연결리스트 result 다음을 heap에서 불러온 연결리스트로 연결해줍니다. 

        result = result.next

        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next)) # result 뒤에 이어진 부분(아직 result엔 추가되지 않은 부분)은 잘라서 다시 heap에 저장해줍니다.
    
    return root.next

"""
1 -> 4 -> 5,

1 -> 3 -> 4,

2 -> 6

일때,
heap = 
        [(1, 0, (1 -> 4 -> 5),
        (1, 1, (1 -> 3 -> 4),
        (2, 2, (2 -> 6)]

첫 while문이 끝나면,

result = 1 -> 4 -> 5

heap = 
        [(1, 1, (1 -> 3 -> 4),
        (2, 2, (2 -> 6),
        (4, 0, (4 -> 5)]

두 번째 while문이 끝나면,

result = (1 -> )1 -> 3 -> 4

heap =
        [(2, 2, (2 -> 6),
        (3, 1, (3 -> 4),
        (4, 0, (4 -> 5)]

가 됩니다.
"""