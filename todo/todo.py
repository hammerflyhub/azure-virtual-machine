# import the time module
import time


print("想上厕所吗？1:想 0：不想")
x=input()
if x==1:
  print("去上厕所")

t=5

while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
print("时间到")
