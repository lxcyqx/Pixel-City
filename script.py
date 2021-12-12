import maya.cmds as cmds
import math
import random 

random.seed(1234)

boxList = cmds.ls('box*')
if len(boxList) > 0:
    cmds.delete(boxList)

for i in range(0,60):
    for j in range(0,50):
        if not (i%10==0) and not (j%13==0):
            instanceResult = cmds.polyCube(w=1.7, h=3.7, d=1.7, name="box")
            scalingFactor = random.uniform(0.3, 2.1)
            cmds.scale(1, scalingFactor, 1, instanceResult)
            
            cube = instanceResult[0]
 
            
            x = 2*i + random.uniform(-0.1, 0.1)
            y = scalingFactor/2
            z = 2*j + random.uniform(-0.1, 0.1)

            cmds.move(x,y,z, instanceResult)