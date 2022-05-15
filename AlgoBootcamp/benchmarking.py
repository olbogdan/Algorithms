import time
from collections import deque


array = [1, 2, 3, 4]
que = deque()
que.append("a")
que.append("b")
# for i in array:
#     que.appendleft(i)
array.reverse()
que.extendleft(array)
print(que)


first_stamp = int(round(time.time() * 1000))


second_stamp = int(round(time.time() * 1000))
time_taken = second_stamp - first_stamp
time_taken_seconds = round(time_taken / 1000)
print(f'{time_taken_seconds} seconds or {time_taken} milliseconds')
