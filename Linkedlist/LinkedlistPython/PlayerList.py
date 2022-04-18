from Player import Player
class PlayerList:
    def __init__(self):
        self.start=None
        self.end=None
        self.temp=None
    def add(self,Name,runs,Avg):
        player=Player(Name,runs,Avg)
        if(self.start==None and self.end==None):
            self.start=player
            self.end=player
        else:
            self.end.next=player
            self.end=player
    def Traversal(self):
        current=self.start
        print("Player|\t\tRuns|\t\tAvg|")
        while current is not None:
            current.printplayers()
            current=current.next
    def search(self,str):
        current=self.start
        while current is not None:
            if current.Name==str:
                print("Player Found")
                current.printplayers()
                break
            current=current.next
        if current is None:
            print("Player not found")
    def delete(self,str):
        current=self.start
        if(current.Name==str):
            self.start=current.next
        else:
            while(current.next.next is not None):
                if(current.next.Name==str):
                    current.next=current.next.next
                current=current.next
        if(current.next.Name==str):
            self.end=current
            self.end.next=None



