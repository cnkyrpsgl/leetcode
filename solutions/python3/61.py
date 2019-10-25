class Solution:
    def rotateRight(self, head, k):
        arr, count = [head], 0
        root = last = head
        while last and last.next and count < k:
            last, count = last.next, count+1
            arr.append(last)
        if k != count: 
            k = k % (count+1)
            last = arr[k]
        if k == 0 or not last: 
            return head
        curr = root
        while last.next:
            last, curr = last.next, curr.next
        last.next, curr.next, start = root, None, curr.next
        return start