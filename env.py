import numpy as np
import pandas as pd 
import random 
import time 

class City(object):
    num = 0  # 클래스변수 선언 
    def __init__(self,ranges=(100,200), x=None, y=None):
        self.x = x
        self.y = y
        self.ranges = ranges 

        if x is not None : 
            self.x = x 
        else : 
            self.x = random.randint(*self.ranges)

        if y is not None : 
            self.y = y 
        else : 
            self.y = random.randint(*self.ranges)

        self.position = [self.x,self.y] 
        self.id = City.num
        City.num+=1 

        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y 

    def get_position(self):
        return self.position

    def get_distance(self, city):
        if city is isinstance(city,City):
            diffrence_x = self.get_x()-city.get_x()
            diffrence_y = self.get_y()-city.get_y()
            distance = np.sqrt(diffrence_x**2 + diffrence_y**2)
    def __repr__(self):
        return f"id:{self.id}, x:{self.get_x()}, y:{self.get_y()}"

class env(object):
    def __init__(self, city_num=10, ranges =[100,200], destination_id=2 ):
        self.city_num = city_num
        self.destination_id = 2 
        self.clty_lst = [City(ranges) for i in range(city_num)] # random inititalization 
        self.state  =  None     # Agent visited place
        self.done = False 
        self.get_adj_matrix(city_num)

    def get_adj_matrix(self,n):
        adj_matrix = np.random.random((n,n)) # initialize random matrix 0~1
        adj_matrix = adj[np.where(adj>=0.5)] = 1
        adj_matrix = adj[np.where(adj<0.5)] = 0 
        self.adjacency_matrix = adj_matrix #it stands for possible path to each node 

    def set_destination(self, city_index=None):
        if city_index is not None : 
            destination_id = city_index
        else : destination_id = city_index 

    
    def is_done(self):
        if state[-1] == destination_id :
            self.done = True 
        else :
            self.done = False 
        
        
    def move_from_to(slef, action):
        pass
    

if __name__ == '__main__':
    Ulsan = City(x=20,y=30)
    print(Ulsan.get_x())
    print(Ulsan.get_y())
    print(Ulsan.get_position())
    print(Ulsan)

    Ulsan2 = City(x=21,y=30)
    print(Ulsan2.get_x())
    print(Ulsan2.get_y())
    print(Ulsan2.get_position())
    print(Ulsan2)

    Ulsan3 = City(ranges=[100,200])
    print(Ulsan3.get_x())
    print(Ulsan3.get_y())
    print(Ulsan3.get_position())
    print(Ulsan3)



