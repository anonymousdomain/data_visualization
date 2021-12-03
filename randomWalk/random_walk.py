from random import choice

class RandomWalk:
    
    def __init__(self,num_points=5000):
        self.num_points=num_points
        
        self.x_values=[0]
        self.y_values=[0]
        
    def fill_walk(self):
       while len(self.x_values)<self.num_points:
           
            x_step=self.get_xstep()
          
            y_step=self.get_ystep()
            if x_step==0 and y_step==0:
                continue
            
            #calculate the new postion
            self.new_postion()
            
    def get_xstep(self):
        
        x_direction=choice([1,-1])
        x_distance=choice([0,1,2,3,4,5])
    
        return x_direction*x_distance
    def get_ystep(self):
        y_direction=choice([1,-1])
        y_distance=choice([1,2,3,4,5])
        
        return y_direction*y_distance
    def new_postion(self):
        x=self.x_values[-1]+self.get_xstep()
        y=self.y_values[-1]+self.get_ystep()
            
        self.x_values.append(x)
        self.y_values.append(y)