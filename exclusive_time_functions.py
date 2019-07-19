class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stk, start = [], None
        for log in logs:
            jid, kw, ts = log.split(':')
            jid, ts = int(jid), int(ts)
            if kw == 'start':
                if stk:
                    ans[stk[-1]] += (ts - start)
                stk.append(jid)
                start = ts
            else:
                ans[stk.pop()] += (ts - start + 1)
                start = ts + 1
        return ans
