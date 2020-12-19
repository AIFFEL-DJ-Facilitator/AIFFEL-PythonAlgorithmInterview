def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    root = head = ListNode(0) # head와 root는 같은 구조로 형성되지만 최종적으로 head를 리턴하면 마지막으로 지정된 head를 반환합니다.
    # 즉, head가 head.next = ListNode(val)를 통해 3 -> 2 -> 1로 형성이 되었다고 하더라도 head = head.next로 불러와진 후 리턴되기 때문에 최종적으로 head는 1 -> None을 리턴합니다.
    # 때문에 리턴에 사용할 root를 형성해줍니다.
    # 이전에는 왜 이렇게 안 했을까요? 

    carry = 0
    while l1 or l2 or carry: # l1과 l2가 모두 None이라도 Carry(올림 값)이 남아있으면 다음 자릿수에 더해줘야해서 다음 항이 살아있습니다.
        sum = 0
        # 두 입력값의 합 계산
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next # l1과 l1에서 하나씩 불러와 합해주고 next를 통해 둘 다 텅 빌 때까지 다음 스텝으로 갑니다.

        # 몫(자리올림수)과 나머지(값) 계산
        carry, val = divmod(sum + carry, 10) # 두 수의 합에서 1의 자리수는 val로, 10의 자리수는 carry에 지정해줍니다.
                                             # 불러와지는 carry는 이전의 합이 10을 넘었을때 1을 받아오게 됩니다.
        head.next = ListNode(val) # 계산된 1의 자리수는 head에 저장됩니다.
        head = head.next

    return root.next # next가 붙은 이유는 처음에 root와 head를 생성시 0 -> None으로 만들어졌기 때문입니다.

