class MyCalenderTwo():
    def __init__(self):
        self.list=[]
        self.dou_list=[]
    def book(self,start,end):
        cover_flag=0
        for s,e in self.list:
            if max(s,start)<min(e,end):
                cover_flag=1
                break
        if cover_flag==0:
            self.list.append((start,end))
            return True
        else:
            for dou_s,dou_e in self.dou_list:
                if max(dou_s,start)<min(dou_e,end):
                    return False
            self.dou_list.append((max(s,start),min(e,end)))
            self.list.append((start,end))
            return True
test=MyCalenderTwo()
print(test.book(10,20))
print(test.book(50,60))
print(test.book(10,40))
print(test.book(5,15))
print(test.book(5,10))
print(test.book(25,55))


