#Ship 
from mcpi.minecraft import Minecraft
from mcpi import*

mc = Minecraft.create()
air = 0
stone = 1
iron = 42
dirt = 3
gold = 41
wood = 5
leaf = 18
door = 64
stonebrick = 98

x, y, z = mc.player.getTilePos()                                                  
x, y, z = mc.player.getPos()  

#circlesize 27
def init():
	mc = Minecraft.create("192.168.3.5", 4711)
	x, y, z = mc.player.getPos()
	return mc
def makedeck():
	mc = init()
	x, y, z = mc.player.getPos()
	#mc.setBlocks(x,y-13,z,x,y,z, wood)
	mc.setBlocks(x+13,y,z-25,x,y,z+25, wood)
	mc.setBlocks(x-13,y,z-25,x,y,z+25, wood)#circle cross
	#mc.setBlocks(x+3,y+13,z,x-3,y+13,z, stonebrick) #up
	mc.setBlocks(x+4,y-13,z-25,x-4,y-13,z+25, wood) #down
	mc.setBlocks(x+13,y+3,z-25,x+13,y-3,z+25, wood) #right
	mc.setBlocks(x-13,y+3,z-25,x-13,y-3,z+25, wood) #left

	mc.setBlocks(x+12,y-6,z-25,x+12,y-3,z+25, wood) #6 #lower left
	mc.setBlocks(x+11,y-8,z-25,x+11,y-6,z+25, wood) #8
	mc.setBlocks(x+10,y-9,z-25,x+10,y-7,z+25, wood) #9 
	mc.setBlocks(x+9,y-10,z-25,x+9,y-8,z+25, wood) #10
	mc.setBlocks(x+8,y-11,z-25,x+8,y-10,z+25, wood) #11
	mc.setBlocks(x+7,y-12,z-25,x+7,y-11,z+25, wood) #12
	mc.setBlocks(x+6,y-13,z-25,x+6,y-11,z+25, wood) #13
	mc.setBlocks(x+5,y-13,z-25,x+5,y-12,z+25, wood) #13


	mc.setBlocks(x-12,y-6,z-25,x-12,y-3,z+25, wood) #6 #lower right
	mc.setBlocks(x-11,y-8,z-25,x-11,y-6,z+25, wood) #8
	mc.setBlocks(x-10,y-9,z-25,x-10,y-7,z+25, wood) #9
	mc.setBlocks(x-9,y-10,z-25,x-9,y-8,z+25, wood) #10
	mc.setBlocks(x-8,y-11,z-25,x-8,y-10,z+25, wood) #11
	mc.setBlocks(x-7,y-12,z-25,x-7,y-11,z+25, wood) #12
	mc.setBlocks(x-6,y-13,z-25,x-6,y-11,z+25, wood) #13
	mc.setBlocks(x-5,y-13,z-25,x-5,y-12,z+25, wood) #13
makedeck()
#def makenose():
