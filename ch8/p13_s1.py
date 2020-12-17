"""
# 13 펠린드롬 연결 리스트
연결리스트가 팰린드롬 구조인지 판별하라.

연결리스트는 분할되어 저장되었기 때문에 1개씩 불러와야하는 데이터입니다.
[링크](https://ko.wikipedia.org/wiki/%EC%97%B0%EA%B2%B0_%EB%A6%AC%EC%8A%A4%ED%8A%B8)
"""

def func(head):
    """
    1, 2번의 풀이는 collection함수를 사용하여 데이터 처리를 용이하게 한 것을 제외하면 완전히 동일한 풀이입니다.
    """

    q = [] # linked data를 이곳에 저장한 후 알고리즘을 실행합니다.

    if not head:
        return True # 입력값이 없으면 참으로 판별합니다.
    
    node = head # node 는 현재 입력된 linked data입니다.

    while node is not None: # linked data를 저희에게 익숙한 list data로 변환하는 알고리즘입니다.
        q.append(node.val) # 현재 불러온 linked data의 값을 q에 저장합니다.
        node = node.next # 다음 linked 자료를 불러옵니다. 다음 값이 없으면 node에 None값이 할당되므로 while문이 종료됩니다.
    
    while len(q) > 1: # 저장된 q가 0 혹은 1개가 남으면 종료됩니다.
        if q.pop(0) != q.pop() # 첫번째와 마지막 요소를 pop 함수로 잘라내서 비교합니다.
            return False # 중간에 서로 다르른 요소가 불러와진다면 False를 리턴합니다.
    
    return True # 두번째 while문이 끝나면 True를 리턴합니다.