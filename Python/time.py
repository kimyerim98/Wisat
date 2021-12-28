
import time
current = time.ctime()
cur = current.split(' ')
cur = cur[3]
cur = cur.split(":")
print("현재 시각은", cur[0],"시", cur[1], "분 입니다.")