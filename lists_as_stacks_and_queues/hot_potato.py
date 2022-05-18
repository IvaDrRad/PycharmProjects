from collections import deque

kids_names = deque(input().split())
toss = int(input())

while len(kids_names) > 1:
    kids_names.rotate(-toss)
    to_pop = kids_names.pop()
    print(f"Removed {to_pop}")

print(f"Last is {kids_names[0]}")

