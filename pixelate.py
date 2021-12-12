import maya.cmds as cmds



# make an array with alle the 'birnen*'
def getSpecificObjectsIntoArray(objectName):
	return cmds.ls(objectName, s = False)

def uvScaler():
	#convert selected object to UV
	cmds.select(cmds.polyListComponentConversion(tuv = True), r = True)
	x = cmds.ls(sl=True, fl=True)
	print x
	#calculate center
	u = 0
	v = 0

	for i in x:
	    print cmds.polyEditUV(i, query = True)
	    u += cmds.polyEditUV(i, query = True)[0]
	    v += cmds.polyEditUV(i, query = True)[1]

	u = u/len(x)
	v = v/len(x)
	print "U: ", u
	print "V: ", v

	#scale UV from center
	cmds.polyEditUV(pivotU=u, pivotV=v, scaleU=0.01, scaleV=0.1)

def mainUVScaler(objectName):
	objectList = getSpecificObjectsIntoArray(objectName)
	print objectList
	for objects in objectList:
		print objects
		cmds.select(objects, r = True)
		uvScaler()

mainUVScaler('box*')