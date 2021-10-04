import datetime
import time

class Mydatetime:
    def __init__(self,s, h = None, m = None, ):
        self.h = h
        self.m = m
        self.s = s

    def timer(self):
        if 1<= self.m <60:
            self.s = self.s + self.m*60
        elif 1<= self.h :
            self.s = self.s + self.h * 3600
        for i in range(self.s):
            time.sleep(1)
            self.s -=1
            print('осталось, сек :', self.s)
        print ('the end')
cc = Mydatetime(23,0,0)
print (cc.timer())
