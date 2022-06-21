from collections import deque
class Solution:
    def asteroidCollision(self, asteroids):
        sign = True
        if asteroids[0] < 0:
            sign = False
        deque = deque()
        for asteroid in asteroids:
            if asteroid > 0 and sign:
                deque.append(asteroid)
            elif asteroid < 0 and sign:
                while len(deque) != 0:
                    cur = deque.pop()
                    if asteroid * -1 > cur:
                        continue
                    elif asteroid * -1 == cur:
                        break
                    else:
                        deque.append(cur)
            elif asteroid > 0 and not sign:
                while len(deque) != 0:
                    cur = deque.pop()
                    if asteroid > cur * -1:
                        continue
                    elif asteroid == cur * -1:
                        break
                    else:
                        deque.append(cur)
            elif asteroid < 0 and not sign:
                deque.append(asteroid)
        return list(deque)