'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
Check if these points make a straight line in the XY plane.

Example 1:

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
'''

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if 2 == len(coordinates):
            return True
        
        #d=(x−x1)(y2−y1)−(y−y1)(x2−x1)
        i = 0
        print(len(coordinates))
        while i < len(coordinates)-1:
            print(i)
            if((len(coordinates)-1) - i) > 2:
                a = (coordinates[i][0]-coordinates[i+1][0])*(coordinates[i+2][1]-coordinates[i+1][1])
                b = (coordinates[i][1]-coordinates[i+1][1])*(coordinates[i+2][0]-coordinates[i+1][0])
                d = (a)-(b)
                if 0 != d:
                    return False
            else:
                a = (coordinates[i-1][0]-coordinates[i][0])*(coordinates[i+1][1]-coordinates[i][1])
                b = (coordinates[i-1][1]-coordinates[i][1])*(coordinates[i+1][0]-coordinates[i][0])
                d = (a)-(b)
                if 0 != d:
                    return False
            
            i = i + 2
        return True
