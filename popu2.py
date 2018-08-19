#!/usr/bin/env python
def popu2():
    import sys
    import nuke
    import math
    
    #for i in range(1,5):
        #nuke.nodes.Multiply().setName('jhMult1')
    for i in range(1,7): # i = the number of vertices
        populate = nuke.nodes.Multiply(name='jhMult%s' % i)
        populate.setInput(0, nuke.selectedNode()) 
