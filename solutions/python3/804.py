class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dic=set()
        letters=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            code=[]
            for letter in word: code.append(letters[ord(letter)-ord("a")])
            code= "".join(code)
            if not code in dic: dic.add(code)
        return len(dic)