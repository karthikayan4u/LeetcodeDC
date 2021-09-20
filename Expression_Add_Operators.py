class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        l = len(num)
        def backtrack(index, prev, cur, val, expression):
            if index == l:
                if val == target and cur == 0:
                    result.append(''.join(expression[1:]))
                return
            cur = cur * 10 + int(num[index])
            
            if cur > 0:
                backtrack(index+1, prev, cur, val, expression)
                
            expression.append('+')
            expression.append(str(cur))
            backtrack(index+1, cur, 0, val + cur, expression)
            expression.pop()
            expression.pop()
            
            if expression:
                expression.append('-')
                expression.append(str(cur))
                backtrack(index+1, -cur, 0, val - cur, expression)
                expression.pop()
                expression.pop()
                
                expression.append('*')
                expression.append(str(cur))
                backtrack(index+1, cur * prev, 0, val - prev + (cur * prev), expression)
                expression.pop()
                expression.pop()
        backtrack(0, 0, 0, 0, [])
        return result
            
