import random

class car_class():
    
    def __init__(self, model, color, nod) :   
        self.car_model= model
        self.car_color= color
        self.num_of_doors=nod

    def desc(self) :                  
        print(f"car model is:{self.car_model}")  
        print(f"car color is :{self.car_color}")  
        print(f"num of doors is:{self.num_of_doors}")  
               
                       
class audi_car(car_class):
    def __init__(self, model, color, nod ):
        super().__init__(model, color, nod)
        self.audi_model=None
        self.__serial_num=random.randint(1,10)    # set __ to make this atribute private Encapsulation
    
    def set_audi_model(self,model1):
        self.audi_model=model1

    def get_serial_num(self) :
        print(self.__serial_num )  


#audi1=car_class(model=2017 , color='green', nod=4)
audi2=audi_car(model=2019, color='red' ,nod=7)

#audi1.desc()
audi2.desc()

#audi1.set_audi_model('RR'); print(audi1.audi_model)       error audi1 is car class that hasn't audi model method
audi2.set_audi_model('fff'); print(audi2.audi_model)
audi2.get_serial_num()
#print(audi2.__serial_num)      error not defined out the class because it's private









#child class takes anything from parent class except encapsulations