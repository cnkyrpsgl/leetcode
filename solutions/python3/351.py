class Solution:
    def numberOfPatterns(self, m, n):
        q, pattern = [[c] for c in range(1, 10)], 0
        while q:
            new = []
            for arr in q:
                if m <= len(arr) <= n:
                    pattern += 1
                if len(arr) < n:
                    last = arr[-1]
                    for c in range(1, 10):
                        if c not in arr:
                            if last in (1, 4, 7) and c == last + 2:
                                if last + 1 in arr:
                                    new.append(arr + [c])
                            elif last in (3, 6, 9) and c == last - 2:
                                if last - 1 in arr:
                                    new.append(arr + [c])
                            elif last in (1, 2, 3) and c == last + 6:
                                if last + 3 in arr:
                                    new.append(arr + [c])
                            elif last in (7, 8, 9) and c == last - 6:
                                if last - 3 in arr:
                                    new.append(arr + [c])
                            elif last == 1 and c == 9:
                                if 5 in arr:
                                    new.append(arr + [9])
                            elif last == 9 and c == 1:
                                if 5 in arr:
                                    new.append(arr + [1])
                            elif last == 3 and c == 7:
                                if 5 in arr:
                                    new.append(arr + [7])
                            elif last == 7 and c == 3:
                                if 5 in arr:
                                    new.append(arr + [3])
                            else:
                                new.append(arr + [c])
            q = new
        return pattern