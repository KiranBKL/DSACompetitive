from PlayerList import PlayerList
file = open("Players.txt", "r")
pl=PlayerList()
for each in file:
    name,score,avg=each.split()
    pl.add(name,score,avg)
pl.Traversal()
pl.delete("Zaheer")
pl.Traversal()


