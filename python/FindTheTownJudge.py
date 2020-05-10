'''
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2

Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1

Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
 

Note:

1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N
'''

'''
Input: N = 2, trust = [[1,2]]
Output: 2
'''

#Solution 1
def findJudge1( N, trust):
    
    if(len(trust) == 1):
        return trust[0][1]

    peopleDict = dict()

    for i in trust:
        #print(i[0])
        if i[0] not in peopleDict:
            peopleDict[i[0]] = [i[1]]
        else:
            #print(peopleDict[i[0]])
            peopleDict[i[0]].append(i[1])
            #temp.append([i[1]])

    print("peopleDict: ",peopleDict)

    count = 0
    for i in range(1, N+1):
        #print("i: ", i)
        if i not in peopleDict:
            print("i: ", i)
            for j in peopleDict:
                if i in peopleDict[j]:
                    count = count + 1
        print("Count: ", count)
        if count == N-1:
            return i

    return -1

#Solution 2
def findJudge2(self, N: int, trust: List[List[int]]) -> int:
        society_level = [0 for i in range(N)]
        suspicion_level = [0 for i in range(N)]

        for el in trust:
            society_level[el[1] - 1] += 1
            suspicion_level[el[0] - 1] += 1

        for i in range(N):
            if society_level[i] == N - 1:
                if suspicion_level[i] == 0:
                    return i + 1

        return -1

N = 3
trust = [[1,3],[2,3]]
print(findJudge(N, trust))
