from vpython import *

r=vector(-10,0,0)
vel=vector(10,10,0)
grav = 10
acel= vector(0,-grav,0)
dt=1/50
t=0

wall=box(pos=vector(0,-1,0),color=color.yellow,length=30,height=.1,width=25)
cañon=cylinder(pos=vector(-10,0,0),axis=vector(1,1,0),color=color.green,length=3,radius=.5)
limon=sphere(pos=vector(-10,0,0),color=color.red,radius=.40)
limon2=sphere(pos=vector(-4,5,0),color=color.red,radius=.40)
limon3=sphere(pos=vector(2,9,0),color=color.red,radius=.40)
limon4=sphere(pos=vector(8,5,0),color=color.red,radius=.40)
limon5=sphere(pos=vector(12,0,0),color=color.red,radius=.40)
trayectoria=curve(color=color.magenta,axis=vector(vel))
velocidad_total=arrow(color=color.purple,pos=limon.pos,axis=(vel/3))
velocidadx=arrow(color=color.orange,pos=limon.pos,axis=vector(vel.x/3.,0,0))
velocidady=arrow(color=color.orange,pos=limon.pos,axis=vector(0,vel.y/3.,0))
velocidad_total=arrow(color=color.purple,pos=limon2.pos,axis=(vel/6))
velocidadx=arrow(color=color.orange,pos=limon2.pos,axis=vector(vel.x/6.,0,0))
velocidady=arrow(color=color.orange,pos=limon2.pos,axis=vector(0,vel.y/6.,0))
velocidad_total=arrow(color=color.purple,pos=limon3.pos,axis=(vel/6))
velocidadx=arrow(color=color.orange,pos=limon3.pos,axis=vector(vel.x/6.,0,0))
velocidady=arrow(color=color.orange,pos=limon3.pos,axis=vector(0,vel.y/6.,0))
velocidad_total=arrow(color=color.purple,pos=limon4.pos,axis=(vel/6))
velocidadx=arrow(color=color.orange,pos=limon4.pos,axis=vector(vel.x/6.,0,0))
velocidady=arrow(color=color.orange,pos=limon4.pos,axis=vector(0,vel.y/6.,0))
velocidad_total=arrow(color=color.purple,pos=limon5.pos,axis=(vel/6))
velocidadx=arrow(color=color.orange,pos=limon5.pos,axis=vector(vel.x/6.,0,0))
velocidady=arrow(color=color.orange,pos=limon5.pos,axis=vector(0,vel.y/6.,0))









