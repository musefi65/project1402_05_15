class  karmand:
    def __init__(self,n,f,a,adrs) :
        self.name=n
        self.family=f
        self.age=a
        self.address=adrs
    def chap(self):
        print(10*"*")
        print(self.name,self.family,self.address)

k1=karmand ("alireza","ahmadi",20,"shahrkord")
k1.chap()


