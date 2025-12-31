class Pet :
    def __init__(self,name,p_type,price):
        self.name = name
        self.p_type = p_type
        self.price = price
        
    def display(self):
        print("pet name : ",self.name)
        print("Pet Type:", self.p_type)
        print("Pet Price:", self.price)
p=Pet("tom","Dog",20000)
p.display()