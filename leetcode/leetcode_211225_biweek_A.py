class Solution(object):
    def mostWordsFound(self, sentences):
        result = 0
        for s in sentences:
            word_count = len(s.split(" "))
            if result < word_count:
                result = word_count
        return result
        """
        :type sentences: List[str]
        :rtype: int
        """
