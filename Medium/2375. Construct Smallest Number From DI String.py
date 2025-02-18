class Solution:
    def smallestNumber(self, pattern: str) -> str:
        num = []
        result = ""

        for i in range(len(pattern) + 1):
            num.append(str(i + 1))

            if i == len(pattern) or pattern[i] == 'I':
                while num:
                    result += num.pop()

        return result
