import time
import uuid

class Animal:
  def __init__(self, name, type):
    self.id = time.strftime("%d%m%M%S") #id it by time bc time will always be unique/
    #self.id = self(id) #get id from memory address so next time code is ran, id can be different than last execution
    #self.id = uuid()
    self.name = name
    self.type = type
    self.arrived = time.strftime("%d/%m/%Y")
    self.adopted = None #bc they won't be adopted right after they arrived
  def setAdopted(self):
    self.adopted = time.strftime("%d/%m/%Y")
  def __str__(self):
    result_str = f"{self.name}[{self.type}]"
    result_str += f"\narrived{self.arrived}"
    result_str += f"\nadopted:{self.adopted}"
    return result_str
    
def main():
  fido = Animal("fido", "cat")
  fido.setAdopted()
  
main()

#https://replit.com/@Steven_AA/Ch-7-Exercise-Animal-Shelter#main.py