class car_class():
    
    def __init__(self, model, color) :   #constructor  , initializer
        self.car_model= model
        self.car_color= color

    def desc(self) :                   #functionalities    , methods     # must take self to take the variables from class
        print(f"car model is:{self.car_model}")  
        print(f"car color is :{self.car_color}")           
                       

bus=car_class(model=2014 , color='blue')
audi=car_class(model=2017 , color='green')

bus.desc()
audi.desc()
