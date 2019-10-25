class Solution:
    def prisonAfterNDays(self, cells, N):
        day, state, cur = 0, {}, "".join(map(str, cells))
        while cur not in state:
            state[cur] = day
            state[day] = cur
            if day == N:
                return list(map(int, cur))
            day += 1
            cur = "0" + "".join(cur[i - 1] == cur[i + 1] and "1" or "0" for i in range(1, len(cur) - 1)) + "0"
        return list(map(int, state[state[cur] + (N - state[cur]) % (day - state[cur])]))