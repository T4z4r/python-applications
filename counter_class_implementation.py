class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1    

    def get_count(self):
        return self.count

    def reset(self):
        self.count = 0
        
counter = Counter()
counter.increment()
counter.increment()
print(f"Current count: {counter.get_count()}")
counter.decrement()
print(f"Current count after decrement: {counter.get_count()}")
counter.reset()
print(f"Count after reset: {counter.get_count()}")