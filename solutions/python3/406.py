class Solution:
    def reconstructQueue(self, people):
        arr = [0] * len(people)
        people.sort()
        for h, k in people:
            cnt = 0
            for i in range(len(arr)):
                if not arr[i] or arr[i][0] == h:
                    cnt += 1
                    if cnt == k + 1:
                        arr[i] = [h, k]
        return arr