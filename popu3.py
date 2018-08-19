#def testFunc():
#    listA = [1, 2, 3]
#    print 'listA: ', listA
#    return listA

import sys
import nuke
import math

def preSampleHDR():
    #for i in range(1,5):
    #nuke.nodes.Multiply().setName('jhMult1')        
    for vert in range(1,43): # vert = the number of vertices
        populate = nuke.nodes.Multiply(name='ls3_Vert%s' % vert)
        populate.setInput(0, nuke.selectedNode())
        
    # start to generate the hugeList
    hugeList = [] # empty the hugeList first
    
    y = 0.5 
    x = 0.5
    count = 0
    pixelCount = 0
    #ii = 0  # ii is just a number for debugging 
    for v in range(0,64):
        #for y in y_list:    
        if y < 64.0:
            #for x in x_list:
            for u in range(0,128):
                if x < 128.0:
                    #print
                    #print
                    #print 'this is the pixel u= ', u+1, 'and v = ', v+1               
                    #target = nuke.toNode('NoOp_JH')   # point to the node in the Nuke DAG that will be sampled.
                    #valueR = nuke.sample(target, 'red', x, y)    # sample the pixel value of given coordinate
                    #valueG = nuke.sample(target, 'green', x, y)    
                    #valueB = nuke.sample(target, 'blue', x, y)        
                    #avgPV = (valueR + valueG + valueB)/3   # average pixel value of the given coordinate
                    p = [x,y]   # put the x, y coordinate in a tuple for following calcuation               
                    #print 'sampled pixel coord is ', p, '  R= ', valueR, '  G= ', valueG, '  B= ', valueB, '  avg pixel value= ', avgPV
                    #print 'sampled pixel coord is ', p, '  avg pixel value= ', avgPV
                    
                    # huge assignment, assign xy coordinate for each vertex
                    vert_1 = [75.27822,32.00001];  vert_13 = [32.00007,64.00001];    vert_25 = [120.58,21.40];  vert_37 = [43.28,25.66];   vert_49 = [0.0,64.0]
                    vert_2 = [52.72,32.0];  vert_14 = [20.71,51.0];   vert_26 = [7.42,21.40];    vert_38 = [32.0,32.0];     vert_50 = [128.0,64.0]
                    vert_3 = [11.28,32.0];  vert_15 = [20.72,38.33];  vert_27 = [43.29,51.0];    vert_39 = [84.70911,50.99292];    vert_51 = [128.0,52.73]
                    vert_4 = [116.72,32.0]; vert_16 = [20.72,25.66];  vert_28 = [56.58,42.60];   vert_40 = [71.42227,42.59618]
                    vert_5 = [32.0,20.72];  vert_17 = [20.71,13.01];  vert_29 = [63.99998,32.00001];     vert_41 = [84.72,38.34]
                    vert_6 = [32.0,43.28];  vert_18 = [32.0,0.0];     vert_30 = [56.58,21.40];   vert_42 = [71.42,21.40]
                    vert_7 = [96.0,43.28];  vert_19 = [107.29,13.01]; vert_31 = [43.29,13.0];    vert_43 = [10.35,64.0]
                    vert_8 = [96.0,20.72];  vert_20 = [107.27,25.66]; vert_32 = [84.71,13.0];    vert_44 = [32.0,64.0]
                    vert_9 = [0.0,11.26];   vert_21 = [107.27,38.33]; vert_33 = [84.72,25.66];   vert_45 = [53.65,64.0]
                    vert_10 =[64.0,11.26];  vert_22 = [120.58,42.60]; vert_34 = [96.00,32.00];   vert_46 = [74.36,64.0]
                    vert_11 =[64.0,52.73];  vert_23 = [7.42,42.60];   vert_35 = [107.2907,50.99292];   vert_47 = [96.0,64.0]
                    vert_12 =[0.0,52.73];   vert_24 = [0.0,32.0];     vert_36 = [43.28,38.33];   vert_48 = [117.65,64.0]
                                            
                    # huge assignment, each triangle is declared as a list with the vertex numbering as the odd index and the vertex coordinates as the even index
                    tri_1 = ['vertex010', vert_10, 'vertex030', vert_30, 'vertex042', vert_42]
                    tri_2 = ['vertex029', vert_29, 'vertex028', vert_28, 'vertex040', vert_40]
                    tri_3 = ['vertex007', vert_7, 'vertex041', vert_41, 'vertex034', vert_34]
                    tri_4 = ['vertex007', vert_7, 'vertex039', vert_39, 'vertex041', vert_41]
                    tri_5 = ['vertex033', vert_33, 'vertex042', vert_42, 'vertex032', vert_32]
                    tri_6 = ['vertex002', vert_2, 'vertex036', vert_36, 'vertex037', vert_37]
                    tri_7 = ['vertex010', vert_10, 'vertex030', vert_30, 'vertex031', vert_31]
                    tri_8 = ['vertex011', vert_11, 'vertex027', vert_27, 'vertex028', vert_28]
                    tri_9 = ['vertex024', vert_24, 'vertex025', vert_25, 'vertex026', vert_26]
                    tri_10 = ['vertex012', vert_12, 'vertex022', vert_22, 'vertex023', vert_23]
                    tri_11 = ['vertex038', vert_38, 'vertex016', vert_16, 'vertex005', vert_5]
                    tri_12 = ['vertex005', vert_5, 'vertex016', vert_16, 'vertex017', vert_17]
                    tri_13 = ['vertex006', vert_6, 'vertex014', vert_14, 'vertex015', vert_15]
                    tri_14 = ['vertex021', vert_21, 'vertex007', vert_7, 'vertex034', vert_34]
                    tri_15 = ['vertex035', vert_35, 'vertex007', vert_7, 'vertex021', vert_21]
                    tri_16 = ['vertex020', vert_20, 'vertex008', vert_8, 'vertex019', vert_19]
                    tri_17 = ['vertex031', vert_31, 'vertex017', vert_17, 'vertex018', vert_18]
                    #tri_18 = ['vertex013', vert_13, 'vertex027', vert_27, 'vertex011', vert_11]
                    tri_18 = ['vertex045', vert_45, 'vertex027', vert_27, 'vertex011', vert_11]
                    tri_19 = ['vertex039', vert_39, 'vertex007', vert_7, 'vertex035', vert_35]
                    tri_20 = ['vertex032', vert_32, 'vertex018', vert_18, 'vertex019', vert_19]
                    #tri_21 = ['vertex012', vert_12, 'vertex014', vert_14, 'vertex013', vert_13]
                    tri_21 = ['vertex012', vert_12, 'vertex014', vert_14, 'vertex043', vert_43]
                    tri_22 = ['vertex012', vert_12, 'vertex023', vert_23, 'vertex014', vert_14]
                    tri_23 = ['vertex015', vert_15, 'vertex003', vert_3, 'vertex016', vert_16]
                    tri_24 = ['vertex016', vert_16, 'vertex026', vert_26, 'vertex017', vert_17]
                    tri_25 = ['vertex017', vert_17, 'vertex009', vert_9, 'vertex018', vert_18]
                    tri_26 = ['vertex009', vert_9, 'vertex019', vert_19, 'vertex018', vert_18]
                    tri_27 = ['vertex025', vert_25, 'vertex019', vert_19, 'vertex009', vert_9]
                    tri_28 = ['vertex021', vert_21, 'vertex020', vert_20, 'vertex004', vert_4]
                    tri_29 = ['vertex022', vert_22, 'vertex021', vert_21, 'vertex004', vert_4]
                    tri_30 = ['vertex023', vert_23, 'vertex024', vert_24, 'vertex003', vert_3]
                    tri_31 = ['vertex022', vert_22, 'vertex004', vert_4, 'vertex024', vert_24]
                    tri_32 = ['vertex004', vert_4, 'vertex025', vert_25, 'vertex024', vert_24]
                    tri_33 = ['vertex025', vert_25, 'vertex009', vert_9, 'vertex026', vert_26]
                    tri_34 = ['vertex023', vert_23, 'vertex003', vert_3, 'vertex015', vert_15]
                    tri_35 = ['vertex027', vert_27, 'vertex014', vert_14, 'vertex006', vert_6]
                    tri_36 = ['vertex028', vert_28, 'vertex036', vert_36, 'vertex002', vert_2]
                    tri_37 = ['vertex028', vert_28, 'vertex002', vert_2, 'vertex029', vert_29]
                    tri_38 = ['vertex002', vert_2, 'vertex030', vert_30, 'vertex029', vert_29]
                    tri_39 = ['vertex002', vert_2, 'vertex037', vert_37, 'vertex030', vert_30]
                    tri_40 = ['vertex005', vert_5, 'vertex017', vert_17, 'vertex031', vert_31]
                    tri_41 = ['vertex004', vert_4, 'vertex020', vert_20, 'vertex025', vert_25]
                    tri_42 = ['vertex008', vert_8, 'vertex032', vert_32, 'vertex019', vert_19]
                    tri_43 = ['vertex033', vert_33, 'vertex032', vert_32, 'vertex008', vert_8]
                    tri_44 = ['vertex034', vert_34, 'vertex033', vert_33, 'vertex008', vert_8]
                    tri_45 = ['vertex034', vert_34, 'vertex008', vert_8, 'vertex020', vert_20]
                    tri_46 = ['vertex035', vert_35, 'vertex021', vert_21, 'vertex022', vert_22]
                    #tri_47 = ['vertex013', vert_13, 'vertex035', vert_35, 'vertex012', vert_12]
                    tri_47 = ['vertex048', vert_48, 'vertex035', vert_35, 'vertex012', vert_12]
                    #tri_48 = ['vertex013', vert_13, 'vertex014', vert_14, 'vertex027', vert_27]
                    tri_48 = ['vertex044', vert_44, 'vertex014', vert_14, 'vertex027', vert_27]
                    tri_49 = ['vertex027', vert_27, 'vertex006', vert_6, 'vertex036', vert_36]
                    tri_50 = ['vertex038', vert_38, 'vertex005', vert_5, 'vertex037', vert_37]
                    tri_51 = ['vertex036', vert_36, 'vertex038', vert_38, 'vertex037', vert_37]
                    tri_52 = ['vertex006', vert_6, 'vertex015', vert_15, 'vertex038', vert_38]
                    tri_53 = ['vertex014', vert_14, 'vertex023', vert_23, 'vertex015', vert_15]
                    tri_54 = ['vertex015', vert_15, 'vertex016', vert_16, 'vertex038', vert_38]
                    tri_55 = ['vertex003', vert_3, 'vertex026', vert_26, 'vertex016', vert_16]
                    tri_56 = ['vertex026', vert_26, 'vertex009', vert_9, 'vertex017', vert_17]
                    tri_57 = ['vertex003', vert_3, 'vertex024', vert_24, 'vertex026', vert_26]
                    tri_58 = ['vertex022', vert_22, 'vertex024', vert_24, 'vertex023', vert_23]
                    tri_59 = ['vertex035', vert_35, 'vertex022', vert_22, 'vertex012', vert_12]
                    #tri_60 = ['vertex013', vert_13, 'vertex011', vert_11, 'vertex039', vert_39]
                    tri_60 = ['vertex046', vert_46, 'vertex011', vert_11, 'vertex039', vert_39]
                    #tri_61 = ['vertex013', vert_13, 'vertex039', vert_39, 'vertex035', vert_35]
                    tri_61 = ['vertex047', vert_47, 'vertex039', vert_39, 'vertex035', vert_35]
                    tri_62 = ['vertex011', vert_11, 'vertex040', vert_40, 'vertex039', vert_39]
                    tri_63 = ['vertex040', vert_40, 'vertex001', vert_1, 'vertex041', vert_41]
                    tri_64 = ['vertex041', vert_41, 'vertex033', vert_33, 'vertex034', vert_34]
                    tri_65 = ['vertex039', vert_39, 'vertex040', vert_40, 'vertex041', vert_41]
                    tri_66 = ['vertex041', vert_41, 'vertex001', vert_1, 'vertex033', vert_33]
                    tri_67 = ['vertex001', vert_1, 'vertex042', vert_42, 'vertex033', vert_33]
                    tri_68 = ['vertex042', vert_42, 'vertex010', vert_10, 'vertex032', vert_32]
                    tri_69 = ['vertex010', vert_10, 'vertex018', vert_18, 'vertex032', vert_32]
                    tri_70 = ['vertex010', vert_10, 'vertex031', vert_31, 'vertex018', vert_18]
                    tri_71 = ['vertex029', vert_29, 'vertex030', vert_30, 'vertex042', vert_42]
                    tri_72 = ['vertex029', vert_29, 'vertex042', vert_42, 'vertex001', vert_1]
                    tri_73 = ['vertex040', vert_40, 'vertex029', vert_29, 'vertex001', vert_1]
                    tri_74 = ['vertex011', vert_11, 'vertex028', vert_28, 'vertex040', vert_40]
                    tri_75 = ['vertex027', vert_27, 'vertex036', vert_36, 'vertex028', vert_28]
                    tri_76 = ['vertex006', vert_6, 'vertex038', vert_38, 'vertex036', vert_36]
                    tri_77 = ['vertex037', vert_37, 'vertex005', vert_5, 'vertex031', vert_31]
                    tri_78 = ['vertex037', vert_37, 'vertex031', vert_31, 'vertex030', vert_30]
                    tri_79 = ['vertex021', vert_21, 'vertex034', vert_34, 'vertex020', vert_20]
                    tri_80 = ['vertex020', vert_20, 'vertex019', vert_19, 'vertex025', vert_25]
                    # extra psuedo vertices to solve the sampling issue for the pole
                    tri_81 = ['vertex043', vert_43, 'vertex049', vert_49, 'vertex012', vert_12]
                    tri_82 = ['vertex044', vert_44, 'vertex043', vert_43, 'vertex014', vert_14]
                    tri_83 = ['vertex045', vert_45, 'vertex044', vert_44, 'vertex027', vert_27]
                    tri_84 = ['vertex046', vert_46, 'vertex045', vert_45, 'vertex011', vert_11]
                    tri_85 = ['vertex047', vert_47, 'vertex046', vert_46, 'vertex039', vert_39]
                    tri_86 = ['vertex048', vert_48, 'vertex047', vert_47, 'vertex035', vert_35]
                    tri_87 = ['vertex050', vert_50, 'vertex048', vert_48, 'vertex051', vert_51]
                    
                    #print 'tri_1= ', tri_1
                    tri_grp = [tri_1, tri_2, tri_3, tri_4, tri_5, tri_6, tri_7, tri_8, tri_9, tri_10, tri_11, tri_12,
                               tri_13, tri_14, tri_15, tri_16, tri_17, tri_18, tri_19, tri_20, tri_21, tri_22, tri_23,
                               tri_24, tri_25, tri_26, tri_27, tri_28, tri_29, tri_30, tri_31, tri_32, tri_33, tri_34,
                               tri_35, tri_36, tri_37, tri_38, tri_39, tri_40, tri_41, tri_42, tri_43, tri_44, tri_45,
                               tri_46, tri_47, tri_48, tri_49, tri_50, tri_51, tri_52, tri_53, tri_54, tri_55, tri_56,
                               tri_57, tri_58, tri_59, tri_60, tri_61, tri_62, tri_63, tri_64, tri_65, tri_66, tri_67,
                               tri_68, tri_69, tri_70, tri_71, tri_72, tri_73, tri_74, tri_75, tri_76, tri_77, tri_78,
                               tri_79, tri_80, tri_81, tri_82, tri_83, tri_84, tri_85, tri_86, tri_87]
                    #print 'tri_grp[0]= ', tri_grp[0]
                    
                    
                    
                    
                    for i in range(87): # the number in the range() will be the total number of triangles
                        vert_coord = tri_grp[i] # it returns ex. vert_coord = ['vertex005', vert_5, 'vertex034', vert_34, 'vertex035', vert_35]
                                            
                        j = i + 1 #just for displaying the correct corresponding number of triangle during debugging
                   
                        # the three vertices of the queried triangle will be temparaily substituded as vertex A(ta), B(tb), C(tc).
                        ta = vert_coord[1] # it returns coordinates of vertex A. ex. a list stores vert_5's xy coordinates
                        tb = vert_coord[3]
                        tc = vert_coord[5]                            
                        
                        #debug                       
                        #if j == 32:                            
                        #        print
                        #        #print 'this is the pixel u= ', u+1, 'and v = ', v+1
                        #        print 'this is the pixel ', '(',p,')', 'inside the %d triangle' % j
                        #        #print 'this is the %d triangle' % j
                        #        print 'vertices x coord = ', ta[0], tb[0], tc[0]
                        
                        # address the issue of tringles whose area across the seam of the lat-long map
                        if j == 9: # this if statement section is dedicated to solve triangle number 22
                            if x <= 64.0:                                                    
                                tb = [vert_coord[3][0]-128.0, vert_coord[3][1]]
                                #p = [x,y]
                                #print 'pixels in LEFT portion','triangle %d' % j, 'x= ', p[0], 'y= ', p[1], 'ta[0]= ', ta[0]                                                    
                            if x > 64.0:                        
                                ta = [vert_coord[1][0]+128.0, vert_coord[1][1]]                        
                                tc = [vert_coord[5][0]+128.0, vert_coord[5][1]]
                                #print 'pixels in RIGHT portion','triangle %d' % j, 'x= ', p[0], 'y= ', p[1], 'ta[0]= ', ta[0]                                       
                        
                        if j == 10: 
                            if x <= 64.0:                            
                                tb = [vert_coord[3][0]-128.0, vert_coord[3][1]]
                            if x > 64.0:
                                ta = [vert_coord[1][0]+128.0, vert_coord[1][1]]                        
                                tc = [vert_coord[5][0]+128.0, vert_coord[5][1]]
                        
                        if j == 26: # south pole triangle
                            ta = [vert_coord[1][0]+128.0, vert_coord[1][1]]  
                            tc = [0.5*(vert_coord[1][0]+128.0+vert_coord[3][0]), vert_coord[5][1]]
                            
                        if j == 27:
                            tc = [vert_coord[5][0]+128.0, vert_coord[5][1]]
                        
                        if j == 31:
                            tc = [vert_coord[5][0]+128.0, vert_coord[5][1]]
                            #print 'tc is ', tc
                            
                        if j == 32:
                            tc = [vert_coord[5][0]+128.0, vert_coord[5][1]]
                                
                        if j == 33:
                            if x <= 64.0:   
                                ta = [vert_coord[1][0]-128.0, vert_coord[1][1]]   
                            if x > 64.0:                                                      
                                tb = [vert_coord[3][0]+128.0, vert_coord[3][1]]
                                tc = [vert_coord[5][0]+128.0, vert_coord[5][1]]
                        
                        if j == 47: # north pole triangle
                            tc = [vert_coord[5][0]+128.0, vert_coord[5][1]]
                            ta = [0.5*(vert_coord[3][0]+vert_coord[5][0]+128.0), vert_coord[1][1]]
                                              
                        if j == 58:
                            if x <= 64.0:   
                                ta = [vert_coord[1][0]-128.0, vert_coord[1][1]]
                            if x > 64.0:                                                      
                                tb = [vert_coord[3][0]+128.0, vert_coord[3][1]]
                                tc = [vert_coord[5][0]+128.0, vert_coord[5][1]]    
                                
                        if j == 59:
                            tc = [vert_coord[5][0]+128.0, vert_coord[5][1]]
                                                                    
                        # math equation based on John Vince book p.207
                        DET = ta[0]*tb[1]+tc[0]*ta[1]+tb[0]*tc[1]-tc[0]*tb[1]-tb[0]*ta[1]-ta[0]*tc[1]                                     
                        r_coeff = (p[0]*tb[1]+tc[0]*p[1]+tb[0]*tc[1]-tc[0]*tb[1]-tb[0]*p[1]-p[0]*tc[1])/DET            
                        s_coeff = (ta[0]*p[1]+tc[0]*ta[1]+p[0]*tc[1]-tc[0]*p[1]-p[0]*ta[1]-ta[0]*tc[1])/DET
                        t_coeff = (ta[0]*tb[1]+p[0]*ta[1]+tb[0]*p[1]-p[0]*tb[1]-tb[0]*ta[1]-ta[0]*p[1])/DET
                        total_coeff = r_coeff + s_coeff + t_coeff                                                        
                        
                        # debug
                        #if u == 64 and v == 32:
                        #    if total_coeff < 1.0001 and 0.0 <= r_coeff <=1.0001 and 0.0 <= s_coeff <= 1.0001 and 0.0 <= t_coeff <= 1.0001:
                        #        print
                        #        print 'good'
                        #        print 'this is the pixel ', '(',p,')'
                        #        #print 'vertices x coord = ', ta[0], tb[0], tc[0]
                        #        print 'this is the %d triangle' % j
                        #        print 'total_coeff: ', total_coeff
                        #        print 'DET: ', DET
                        #        print 'r_coeff: ', r_coeff
                        #        print 's_coeff: ', s_coeff
                        #        print 't_coeff: ', t_coeff
                        #        
                        #if u == 64 and v == 31:
                        #    if total_coeff < 1.0001 and 0.0 <= r_coeff <=1.0001 and 0.0 <= s_coeff <= 1.0001 and 0.0 <= t_coeff <= 1.0001:
                        #        print 'good'
                        #        print 'this is the pixel ', '(',p,')'
                        #        #print 'vertices x coord = ', ta[0], tb[0], tc[0]
                        #        print 'this is the %d triangle' % j
                        #        #print 'total_coeff: ', total_coeff
                        #        print 'DET: ', DET
                        #        print 'r_coeff: ', r_coeff
                        #        print 's_coeff: ', s_coeff
                        #        print 't_coeff: ', t_coeff
                        #
                        #if u == 64 and v == 33:
                        #    if total_coeff < 1.0001 and 0.0 <= r_coeff <=1.0001 and 0.0 <= s_coeff <= 1.0001 and 0.0 <= t_coeff <= 1.0001:
                        #        print
                        #        print 'good'
                        #        print 'this is the pixel ', '(',p,')'
                        #        #print 'vertices x coord = ', ta[0], tb[0], tc[0]
                        #        print 'this is the %d triangle' % j
                        #        #print 'total_coeff: ', total_coeff
                        #        print 'DET: ', DET
                        #        print 'r_coeff: ', r_coeff
                        #        print 's_coeff: ', s_coeff
                        #        print 't_coeff: ', t_coeff
                                            
                        #################################################
                        ## if the sampled pixel is inside the triangle ##
                        #################################################
                        if total_coeff < 1.0001 and 0 <= r_coeff <1.0001 and 0 <= s_coeff < 1.0001 and 0 <= t_coeff < 1.0001:
                        #if total_coeff > 0.0: #for finding problematic triangles
                            #print
                            #print
                            #print 'this is the %d triangle' %j
                            #print 'the sampled point is inside the triangle'                        
                            def distance(p1, p2): #define a function to calculate the distance between two points
                                return math.hypot(p1[0]-p2[0], p1[1]-p2[1])
                            side_ab = distance(ta, tb)
                            side_bc = distance(tb, tc)
                            side_ca = distance(tc, ta)
                            s = 0.5 * ( side_ab + side_bc + side_ca)
                            triArea = math.sqrt(s * (s - side_ab) * (s - side_bc) * (s - side_ca)) #area of the triangle
                            #print 'triArea= ', triArea
                                                                            
                            side_pb = distance(p, tb)
                            side_bc = distance(tb, tc)
                            side_cp = distance(tc, p)
                            sa = 0.5 * ( side_pb + side_bc + side_cp)
                            if (sa-side_pb)<0.00001 or (sa-side_bc)<0.00001 or (sa-side_cp)<0.00001:
                                intTriArea_a = 0
                            else:    
                                intTriArea_a = math.sqrt(sa * (sa - side_pb) * (sa - side_bc) * (sa - side_cp)) #area of the 1st internal triangle PBC
                            #intTriArea_a = math.sqrt(sa * (sa - side_pb) * (sa - side_bc) * (sa - side_cp)) #area of the 1st internal triangle PBC
                            baryCoeff_a = intTriArea_a/triArea
                            #print 'intTraArea_a= ',intTriArea_a
                    
                            side_pc = distance(p, tc)
                            side_ca = distance(tc, ta)
                            side_ap = distance(ta, p)
                            sb = 0.5 * ( side_pc + side_ca + side_ap)                
                            if (sb-side_pc)<0.00001 or (sb-side_ca)<0.00001 or (sb-side_ap)<0.00001:
                                intTriArea_b = 0
                            else:    
                                intTriArea_b = math.sqrt(sb * (sb - side_pc) * (sb - side_ca) * (sb - side_ap)) #area of the 1st internal triangle PCA
                            baryCoeff_b = intTriArea_b/triArea                
                            #print 'intTraArea_b= ',intTriArea_b, 'side_pc= ', side_pc, 'side_ca= ', side_ca, 'side_ap= ', side_ap, 'sb= ', sb
                    
                            side_pa = distance(p, ta)
                            side_ab = distance(ta, tb)
                            side_bp = distance(tb, p)
                            sc = 0.5 * ( side_pa + side_ab + side_bp)
                            if (sc-side_pa)<0.00001 or (sc-side_ab)<0.00001 or (sc-side_bp)<0.00001:
                                intTriArea_c = 0
                            else:    
                                intTriArea_c = math.sqrt(sc * (sc - side_pa) * (sc - side_ab) * (sc - side_bp)) #area of the 1st internal triangle PAB
                            #intTriArea_c = math.sqrt(sc * (sc - side_pa) * (sc - side_ab) * (sc - side_bp)) #area of the 1st internal triangle PAB
                            baryCoeff_c = intTriArea_c/triArea
                            #print 'intTraArea_a= ',intTriArea_a, 'intTraArea_b= ',intTriArea_b, 'intTraArea_c= ',intTriArea_c
                            
                            sum_bary_coeff = baryCoeff_a + baryCoeff_b + baryCoeff_c
                            #print 'baryCoeff_a = ',baryCoeff_a, 'baryCoeff_b = ',baryCoeff_b, 'baryCoeff_c = ',baryCoeff_c, 'sum_bary_coeff = ', sum_bary_coeff
                            
                            #debug
                            #if triArea > 170.0:
                            #    print
                            #    print 'triangle across boundries'
                            #    print 'this is the pixel u= ', u+1, 'and v = ', v+1
                            #    print 'this is the %d triangle' % j
                            #    print side_ab, side_bc, side_ca
                            #    print 'triArea= ', triArea
                            #    break
                            
                            #debug
                            #print 'triangle', j, 'area is ', triArea
    
                            #debug                       
                            #if u == 64 and v == 30:
                            #    print
                            #    #print 'this is the pixel u= ', u+1, 'and v = ', v+1
                            #    print 'this is the pixel ', '(',p,')', 'inside the %d triangle' % j
                            #    print 'vertices x coord = ', ta[0], tb[0], tc[0]
                            #    print 'side_ab= ',side_ab, side_bc, side_ca
                            #    print 'triArea= ', triArea
                            #    print 'intTriArea_a= ', intTriArea_a
                            #    print 'intTriArea_b= ', intTriArea_b
                            #    print 'intTriArea_c= ', intTriArea_c
                            #    print 'sum_bary_coeff= ', sum_bary_coeff
                            
                            # put the result into a huge list which store the information of which pixels are within which triangle and the value
                            # of barycentric weights
                            
                            newListEntry = [vert_coord[0], baryCoeff_a, vert_coord[2], baryCoeff_b, vert_coord[4], baryCoeff_c]
                            #if u == 64 and v == 29:
                            #    print 'newListEntry for pixel (64,29) is ', newListEntry, ' in triangle %d' % j
                            #if u == 64 and v == 30:
                            #    print 'newListEntry for pixel (64,30) is ', newListEntry, ' in triangle %d' % j
                            #if u == 64 and v == 31:
                            #    print 'newListEntry for pixel (64,31) is ', newListEntry, ' in triangle %d' % j
                            #if u == 64 and v == 32:
                            #    print 'newListEntry for pixel (64,32) is ', newListEntry, ' in triangle %d' % j
                            #if u == 64 and v == 33:
                            #    print 'newListEntry for pixel (64,33) is ', newListEntry, ' in triangle %d' % j
                            #if u == 17 and v == 5:
                            #    print 'newListEntry for pixel', '(',p , ') is ', newListEntry, ' in triangle %d' % j
                            
                            hugeList.append(newListEntry) # use this method to concatenate newListEntry into the hugeList as a "List", not individual value
                            
                            count = 1 # to distinguish the situation where a pixel is within any triangle or not
                            
                            #if u == 64 and v == 6:
                            #    print 'count = ', count
                            #    print hugeList[0]
                            #    print hugeList[0][2]                             
                            #    print 'hugeList is ', hugeList
                                       
                            if sum_bary_coeff > 1.01:
                                print 'sum_bary_coeff= ',sum_bary_coeff, 'something is wrong'
                                print
                                
                            pixelCount += 1
                            #print
                            #print '(u,v) = ', u, v
                            #print 'pixel in tri, pixelCount = ', pixelCount
                            
                            break 
                        else:
                            #print 'the sampled point is outside the triangle'
                            count = 0
                            
                if count == 0: # the sampled pixel is not in any triangle
                    newListEntry = ['NA1', 0, 'NA2', 0, 'NA3', 0]
                    hugeList.append(newListEntry)
                    
                    pixelCount += 1
                    #print
                    #print '(u,v) = ', u, v
                    #print 'pixel has no home, pixelCount = ', pixelCount
                                
                x = x + 1.0
                #print 'x= ', x
            else: 
                x = 0.5
            y = y + 1.0                        
        
    print len(hugeList)
    print 'pixelCount = ', pixelCount
    return hugeList

#baryWeightsList = preSampleHDR()