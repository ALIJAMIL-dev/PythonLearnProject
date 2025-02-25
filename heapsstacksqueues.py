import heapq

class TaskQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self, priority, task):
        heapq.heappush(priority, task)  # ❌ Wrong arguments!

    def get_task(self):
        return heapq.heappop(self.tasks)  # ❌ Might cause an error!

queue = TaskQueue()
queue.add_task(2, "Do homework")
queue.add_task(1, "Write Python code")

print(queue.get_task())  # Expected Output: "Write Python code" (Priority 1 task first)
