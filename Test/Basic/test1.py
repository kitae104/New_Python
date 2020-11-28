import os
import sys

for i in range(1, 11):

    if i == 5:
        print(exit)
        #break
        os._exit(0)
        #exit(0)
        #quit(0)
        #sys.exit(0)

    print(i)


for i in range(10):

    # If the value of i becomes
    # 5 then the program is forced
    # to exit
    if i == 5:
        # prints the exit message
        print(exit)
        exit()
    print(i)