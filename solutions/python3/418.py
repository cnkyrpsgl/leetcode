class Solution:
    def wordsTyping(self, sentence, rows, cols):
        left, count, sm, ptr, wordLen = [0] * len(sentence), 0, 0, 0, len(sentence[0])
        for i, w in enumerate(sentence):
            while sm + wordLen <= cols:
                sm += wordLen
                ptr += 1
                wordLen = len(sentence[ptr % len(sentence)]) + 1
            left[i] = ptr - i
            sm -= len(w) + 1
        for r in range(rows):
            count += left[count % len(sentence)]
        return count // len(sentence)