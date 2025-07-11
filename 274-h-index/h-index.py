class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = 0
        citations.sort()
        l = len(citations)
        for i in range(len(citations)):
            if len(citations) - i <= citations[i]:
                h_index = len(citations) - i
                break
        return h_index