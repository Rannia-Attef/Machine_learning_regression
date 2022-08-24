import math


class cartisian():
    def __init__(self, x, y ,z) :
        self.cartesian= (x,y,z)
        self.spherical=None
        self.cylindrical=None

    def cart2sph(self):
        x,y,z= self.cartesian
        roh= math.sqrt(x*x + y*y +z*z)
        theta=math.atan(y/x) *180/math.pi
        phai=math.atan(math.sqrt(x*x + y*y)/z) *180/math.pi
        self.spherical=(roh, theta, phai)

    #defcart2cylin(self) :
        #x,y,z=self.cartesian
       # r=
        #theta=
        #z=
       # self.cylindrical=(r,theta,z)




class cylind():
    def __init__(self,r,theta,z):
        self.cartesian==None
        self.spherical=None
        self.cylindrical=(r,theta,z)

    def cylin2cart(self):
        r,theta,z=self.cylindrical
        x=r*math.cos(math.radians(theta))
        y=r*math.sin(math.radians(theta))
        self.cartesian=(x,y,z)

    def cylin2spher(self):
        r,theta,z=self.cylindrical
        ro=math.sqrt(r*r + z*z)
        phai=math.atan(r/z)
        self.spherical=(ro,theta,phai)        





#class spherical():
    


#class cylnderical():

    


