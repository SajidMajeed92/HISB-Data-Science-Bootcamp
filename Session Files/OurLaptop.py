class Laptop():
    # Constructor
    def __init__(self,color,ram,storage,processor,model,make,generation):
        self.color       = color
        self.ram         = ram
        self.storage     = storage
        self.processor   = processor
        self.model       = model
        self.make        = make 
        self.generation  = generation
    def specification (self):
        print(f'''
        =========================================
                   Laptop Specification
        =========================================
        color      :      {self.color}
        Ram        :      {self.ram}
        Storage    :      {self.storage}
        Processor  :      {self.processor}
        Model      :      {self.model}
        Make       :      {self.make}
        Generation :      {self.generation}
       =========================================
       =========================================

        ''')
    def get_color(self):
        print(f"The color of Laptop is {self.color}")
        
    def set_color(self,newcolor):
        colors = ["Black","Silver" ,"Blue" , "White"]
        if newcolor in colors:
            self.color = newcolor
        else: 
            print("Color not Available")
                  
    def get_make(self):
        print(f"This  Laptop Manufactured by {self.make}")
        
    def set_make(self,new_make):
        makes = ["HP","Lenovo" ,"Dell"]
        if new_make in makes:
            self.make = new_make
        else: 
            print("Manufacturer not Available")