"""Given a non-empty list of integers, every element appears twice except for one.
Find that single one."""

numbers = [1, 1, 2, 2, 3, 3, 4, 5, 5]
count = {}
for i in numbers:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

for key, value in count.items():
    if value == 1:
        print(key)
