# daemon threads
import threading
import time

def timer():
  print('\n')
  count = 0
  while True:
    time.sleep(1)
    count += 1
    print(f"You are logged in {count} seconds.")

x = threading.Thread(target=timer)
x.setDaemon(True)
x.start()

print(x.isDaemon())

ans = input("Do you want to exit? (y/n): ")
print(threading.enumerate())
