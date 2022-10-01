class Solution(object):
    def leastInterval(self, tasks, N):
        length = len(tasks)
        task_counts = collections.Counter(tasks)
        task_values = task_counts.values()
        Maximum = max(task_values)
        MaximumCount = task_values.count(Maximum)
        result = max(length, (Maximum - 1) * (N + 1) + MaximumCount)
        return result
        