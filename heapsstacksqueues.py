import heapq

class TaskQueue:
    def __init__(self):
        self.tasks = []  # Min-heap to store (priority, task)

    def add_task(self, priority, task):
        heapq.heappush(self.tasks, (priority, task))  # ✅ Push as (priority, task)

    def get_task(self):
        if self.tasks:  # ✅ Check if heap is not empty
            return heapq.heappop(self.tasks)[1]  # ✅ Return only the task
        else:
            return "No tasks left!"

# ✅ Testing the Fixed Code
queue = TaskQueue()
queue.add_task(2, "Do homework")
queue.add_task(1, "Write Python code")  # Lower number = higher priority

print(queue.get_task())  # Output: "Write Python code" (Priority 1 first)
print(queue.get_task())  # Output: "Do homework"
print(queue.get_task())  # Output: "No tasks left!"
