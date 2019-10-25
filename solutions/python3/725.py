class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        n = 0
        node = root
        while node:
            n += 1
            node = node.next
        count = n // k
        residual = n % k

        i = 0
        ret = [[] for _ in range(k)]
        prev = root
        while prev and k > 0:
            node = prev
            leftover = count
            ret[i] = node
            i += 1
            while node and leftover > 1:
                node = node.next
                leftover -= 1
            if node and count != 0 and residual:
                node = node.next
                residual -= 1
            prev = node.next if node else None
            if node:
                node.next = None
            k -= 1
        return ret
