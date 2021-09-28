import random 

class GVDie:  
   def __init__(self):      
      self.my_value = random.randint(1, 6)
      self.rand = random.Random()

   def roll(self):
       self.my_value = self.rand.randint(1, 6)  
      
   def set_seed(self, seed):
       self.rand.seed(seed)
   
   def compare_to(self, other):
       return self.my_value - d.my_value
       