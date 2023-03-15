import random
import json

# プレイヤー
class player:
    # 位置
    def __init__(self,pos):
        self.pos = pos
    # マスに動く
    def move(self):
        sum = 0
        dice = Dice()
        dice_list = dice.roll(1)
        for dice in dice_list:
            sum += dice


class Node:
    def __init__(self,id,kind,adj):
        self.id = id
        self.kind = kind
        self.adj = adj
        
    def __repr__(self):
        return f"<Node {self.id}: kind={self.kind}, adj={self.adj}>"

        


        


# class City:
    
# class Node:
#     def node_distance(self,destination,distance):
#         self.destination = destination
#         self.distance = distance

        

class Dice:
    def roll(self,num):
        dice_list = []
        for i in range(num):
            rand = random.randrange(1,7)
            dice_list.append(rand)
        return dice_list


def distance(a, b):
    if a in dist and b in dist[a]:
        return dist[a][b]
    if b in dist and a in dist[b]:
        return dist[b][a]
    raise KeyError(f"Distance not found between {a} and {b}.")



from bs4 import BeautifulSoup as bs

if __name__ == "__main__":
    with open("distance.json", "r") as f:
        dist = json.load(f)
        print(dist)
        print(f"{distance('tokyo','nagoya') = }")
        print(f"{distance('nagoya','tokyo') = }")
        # print(f"{distance('shiga','tokyo') = }")
    with open("nodes.xml", "r") as f:
        content = f.read()
        
    soup = bs(content,"lxml")
    xnode_list = soup.find_all("node")
    node_list = []
    for node in xnode_list:
        id = int(node.id.text)
        kind = node.kind.text
        adj = list(map(lambda x: int(x.text),node.find_all("adj")))
        node_list.append(Node(id,kind,adj))
    print(node_list)
        
