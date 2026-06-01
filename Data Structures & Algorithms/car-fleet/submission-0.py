class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i],speed[i])for i in range(len(position))]
        fleet=curtime=0
        for dist,speed in sorted(pairs,reverse=True):
            dest = (target-dist)/speed
            if curtime<dest:
                fleet+=1
                curtime=dest
        return fleet