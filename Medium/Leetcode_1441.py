class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        result= []
        index_target = 0

        for i in range(1, n + 1):
            if index_target == len(target):
                break
            result.append('push')

            if i == target[index_target]:
                index_target += 1

            else:
                result.append('pop')
        return result

         
         