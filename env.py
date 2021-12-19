
import numpy as np
import matplotlib.pyplot as plt 
import random 

class random_generator(object):
    def __init__(self,num=20, range_=(0,100), start_point=0):
        self.points = np.random.randint(*range_,size=(num,2))
        #self.destination = np.random.randint(0,num)
        self.start_point = start_point

    def visualize(self):
        plt.figure(figsize=(5,5))
        plt.scatter(self.points[:,0],self.points[:,1], color='red')
        plt.scatter(self.points[self.start_point][0], self.points[self.start_point][1], marker='*', color='Blue', label='start',s=200)
        #plt.scatter(self.points[self.destination][0], self.points[self.destination][1], marker='*', color='orange', label='destination',s=200)
        plt.grid()
        plt.title("generated points (random)")
        plt.legend()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()
        
    def get_points(self):
        return self.points


def distance_matric(from_, to_):
    return np.sqrt((from_[0]-to_[0])**2 +(from_[1]-to_[1])**2)


class env(object):
    def __init__(self, points_obj):
        self.points_obj = points_obj
        self.points = self.points_obj.get_points()
        self.current_position = self.points_obj.start_point
        self.state = np.zeros(len(self.points_obj.points)) # initailize with 0 , [0,0...] ,
        self.state[self.current_position]=1

        self.next_state = self.state
        self.history = [self.current_position] 
       

    def is_done(self): 
        done_mask = False 
        if sum(self.state) == len(self.points_obj.points): # 다 돌았다. :
            done_mask = True 

        return done_mask

    def reward(self, action):
        distance = distance_matric(from_ =self.points[self.current_position], to_= self.points[action])
        return distance 

    def transition(self, action): 
        reward = self.reward(action)      
        self.current_position = action  
        self.state[self.current_position]=1 
        self.history.append(self.current_position)
        return [self.state, reward,self.is_done()] 

    def visualize(self):
        plt.figure(figsize=(5,5))
        plt.scatter(self.points_obj.points[:,0],self.points_obj.points[:,1], color='red')
        plt.scatter(self.points_obj.points[self.points_obj.start_point][0],
         self.points_obj.points[self.points_obj.start_point][1], marker='*', color='Blue', label='start',s=200)

        for i in range(len(self.history)-1):
            plt.plot(self.points_obj.points[self.history[i]], 
            self.points_obj.points[self.history[i+1]])
        
        #plt.scatter(self.points[self.destination][0], self.points[self.destination][1], marker='*', color='orange', label='destination',s=200)
        plt.grid()
        plt.title("generated points (random)")
        plt.legend()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()












