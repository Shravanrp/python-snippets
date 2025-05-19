import time
import sys 

name = input("Enter your name: ").upper()

print("\nRevealing your name...\n")

display = [' '] * len(name)

for i in range(len(name)):
    for c in range(ord('A'), ord(name[i]) + 1):
        display[i] = chr(c)
        sys.stdout.write('\r' + ''.join(display))
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.1)

print("\n\nDone!")
