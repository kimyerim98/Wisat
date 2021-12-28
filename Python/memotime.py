#텍스트에 메모되는 시간 재기
import time

memo = '''
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라만세
'''
t1 = time.time()

print("현재 시각: ",t1)

with open('time.txt','w')as f:
   f.write(memo)
t2 = time.time()
print("경과 시간 :",t2-t1,"\n")

t1 = time.time()
print("현재 시각 :",t1)
with open('time.txt','r')as f:
    print(f.read())
t2 = time.time()
print("경과 시간 :", t2-t1)
