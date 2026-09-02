from collections import deque as queue
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        neighbours = defaultdict(list)
        wordList.append(beginWord)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbours[pattern].append(word)
        visited = set()
        q = queue()
        q.append(beginWord)
        res = 1
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return res
                else:
                    for j in range(len(node)):
                        pattern = node[:j] + "*" + node[j+1:]
                        for neigh in neighbours[pattern]:
                            if neigh not in visited:
                                visited.add(neigh)
                                q.append(neigh)

            res += 1
        return 0

