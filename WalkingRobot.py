class WalkingRobot(object):
    def robots(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        obs = frozenset([(v[0], v[1]) for v in obstacles])
        current =(0, 0)
        dir = (0,1) # facing north.
        max_dist = 0
        for cmd in commands:
            if cmd == -2:
                if dir == (0,1): dir = (-1,0)
                elif dir == (-1,0): dir = (0,-1)
                elif dir == (0,-1): dir = (1,0)
                elif dir == (1,0): dir = (0,1)
            elif cmd == -1:
                if dir == (0,1): dir = (1,0)
                elif dir == (1,0): dir = (0,-1)
                elif dir == (0,-1): dir = (-1,0)
                elif dir == (-1,0): dir = (0,1)
            else:
                for i in range(0, cmd):
                    next = (current[0] + dir[0], current[1] + dir[1])
                    # if next is in obstacle.. do nothing .. else current = next
                    if(next not in obs): current = next
                max_dist = max(max_dist, current[0]**2 + current[1]**2)
        return max_dist

# default
wr = WalkingRobot()
print(wr.robots([4,-1,3], []))
print(wr.robots([4,-1,4,-2,4], [[2,4]]))