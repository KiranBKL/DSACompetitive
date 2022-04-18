class Player:
    def __init__(self,Name,Runs,A):
       self.Name=Name
       self.Runs=Runs
       self.Avg=A
       self.next=None
    def printplayers(self):
        print(self.Name,"\t\t",self.Runs,"\t\t",self.Avg)