class car_class():

    def __init__(self  ) :
        self.car_model=2016  #by defult
        self.car_color="yellow"    #by defult
        self.number_of_doors= None

    def desc(self):
        print(f"car model is : {self.car_model}")
        print(f"car color is : {self.car_color}")
        print(f"car nod is : {self.number_of_doors}")

    def set_car_model(self, model):
        self.car_model=model

    def set_number_of_doors(self, nod):
        self.number_of_doors= nod









    def set_car_color(self, color) :
        self.car_color=color  

#audi=car_class(model=2017, color="blue" )
audi=car_class()
audi.set_number_of_doors(7)   #b ybassi el nod ll attributes through this method
audi.set_car_model(2020)
audi.set_car_color("blue")
audi.desc()       