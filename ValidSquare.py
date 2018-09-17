# https://leetcode.com/problems/valid-square/description/
import itertools
class ValidSquare(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        pointPairs = itertools.combinations([p1,p2,p3,p4],2)
        # (x1-x2)^2 + (y1-y2)^2
        distances = [(c1[0]-c2[0])**2 +(c1[1]-c2[1])**2 for c1, c2 in pointPairs]
        grouped = {}
        for k,v in itertools.groupby(distances):
            if(k in grouped): grouped[k] = grouped[k] + sum(1 for _ in v)
            else: grouped[k] = sum(1 for _ in v)

        if len(grouped) == 2 and 4 in grouped.values(): return True
        else: return False

# These commands will be executed when "python filename.py" is run from a shell
vs = ValidSquare()
print(vs.validSquare([1,1],[2,1],[1,2],[2,2]))


