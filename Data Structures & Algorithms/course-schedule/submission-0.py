class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}
        
        queue = deque()
        remaining_courses = numCourses
        for prereq in prerequisites:
            a, b = prereq
            adjacency[b].append(a)
            indegree[a] += 1
        for c, prereqs in indegree.items():
            if prereqs == 0:
                queue.append(c)
        
        while queue:
            print("checking")
            course = queue.popleft()
            print(course)
            remaining_courses -= 1
            if remaining_courses == 0:
                return True
            for next_class in adjacency[course]:
                indegree[next_class] -= 1
                if indegree[next_class] == 0:
                    queue.append(next_class)

        return False