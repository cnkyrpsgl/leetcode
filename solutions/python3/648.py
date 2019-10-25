class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        s = set(dict)
        sentence = sentence.split()
        for j, w in enumerate(sentence):
            for i in range(1, len(w)):
                if w[:i] in s: 
                    sentence[j] = w[:i]
                    break
        return " ".join(sentence)                    