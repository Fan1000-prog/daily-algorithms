class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        result = [0] * n
        prev_time = 0

        for log in logs:
            id, typ, timeStamp = log.split(":")
            id , timeStamp = int(id), int(timeStamp)
            if typ == 'start':
                if stack:
                    result[stack[-1]] += timeStamp - prev_time
                stack.append(id)
                prev_time = timeStamp

            else:
                finished_id = stack.pop()
                result[finished_id] += timeStamp - prev_time + 1

                prev_time = timeStamp + 1
                
        return result