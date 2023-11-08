class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [(-(x ** 2 + y ** 2), x, y) for x, y in points]

        heapq.heapify(distance)

        while len(distance) > k:
            heapq.heappop(distance)

        return [(x, y) for _, x, y in distance]
