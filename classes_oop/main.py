from coordinates import  cartisian , cylind


point1= cartisian(x=1 , y=2, z=3)
print(point1.spherical)
#print(point1.cylindrical)


#point2= spherical(roh=10 , phai=120 , theta=60)
#print(point2.cartisian)
#print(point2.clyndeical)


point3=cylind(r=10 , theta=120 , z=2)
print(point3.cartesian)
print(point3.spherical)

