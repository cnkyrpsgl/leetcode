class Solution(object):
    def extract_number(self, j, abbr, M):
        num = 0
        while j < M and abbr[j].isdigit():
            num, j = num*10 + int(abbr[j]), j+1
        return num, j
    
    def valid(self, word, abbr):
        i,j,N, M = 0,0,len(word), len(abbr)
        while i < N and j < M:
            if abbr[j].isalpha() and abbr[j] != word[i]:
                return False
            elif abbr[j].isalpha() and abbr[j] == word[i]:
                i,j = i+1,j+1
            elif abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                num, j = self.extract_number(j, abbr, M)
                i = i+num
        return (i==N and j == M)
        
    def process_solution(self, so_far):
        csofar, i, cnt = [], 0, 0
        while i < len(so_far):
            if so_far[i].isalpha():
                csofar.append(so_far[i])
                i, cnt = i+1, cnt+1
            else:
                num = 0
                while i < len(so_far) and so_far[i].isdigit():
                    num, i = num+1, i+1
                cnt = cnt + 1
                csofar.append(str(num))
        return "".join(csofar), cnt
    
    def test(self, abbr, dictionary):
        for wrd in dictionary:
            if self.valid(wrd, abbr):
                return False
        return True
    
    def helper(self, word, so_far, i, dictionary):
        if i == len(word):
            abbr, cnt = self.process_solution(so_far)
            if cnt < self.result_len and self.test(abbr, dictionary):
                self.result, self.result_len = abbr, cnt
            return
        else:
            so_far.append("1")
            self.helper(word, so_far, i+1, dictionary)
            so_far.pop()
            so_far.append(word[i])
            self.helper(word, so_far, i+1, dictionary)
            so_far.pop()

    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        
        # Remove those words which can never be an abbreviation for target.
        # This preprocessing will help us save time.
        filtered_dictionary = []
        for wrd in dictionary:
            if len(wrd) != len(target):
                continue
            filtered_dictionary.append(wrd)
        dictionary = filtered_dictionary
        if len(dictionary) == 0:
            return str(len(target))
            
        self.result_len = len(target)+1
        self.result, so_far, i = target, [], 0
        self.helper(target, so_far, i, dictionary)        
        return self.result