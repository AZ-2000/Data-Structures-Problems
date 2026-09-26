class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        candidates = set()
        if target in triplets:
            return True
        else:
            for a,b,c in triplets:
                if a <= target[0] and b <= target[1] and c <= target[2]:
                    candidates.add((a,b,c))
            curr = [0] * 3
            for a, b, c in candidates:
                curr[0] = max(a, curr[0])
                curr[1] = max(b, curr[1])
                curr[2] = max(c, curr[2])
                if curr == target:
                    return True
            if curr == target:
                return True
            else:
                return False

