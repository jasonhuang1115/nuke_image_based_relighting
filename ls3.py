#!/usr/bin/env python
def ls3(): # just to wrap the code into this fuction so it can be called in Nuke
    import sys 
    import nuke
    import math
    
    y_list = (0.5, 1.5)  # a large tuple holds the y coordinate of the sample point of each pixel on the 128x64 lat-long map
    x_list = (0.5, 1.5, 2.5, 3.5)  # a large tuple holds the x coordinate of the sample point of each pixel on the 128x64 lat-long map
    
    # give final result, the pixel value on each vertex, an initial value
    pixelValueVertex001_r = 0.0; pixelValueVertex001_g = 0.0; pixelValueVertex001_b = 0.0        
    pixelValueVertex002_r = 0.0; pixelValueVertex002_g = 0.0; pixelValueVertex002_b = 0.0    
    pixelValueVertex003_r = 0.0; pixelValueVertex003_g = 0.0; pixelValueVertex003_b = 0.0        
    pixelValueVertex004_r = 0.0; pixelValueVertex004_g = 0.0; pixelValueVertex004_b = 0.0        
    pixelValueVertex005_r = 0.0; pixelValueVertex005_g = 0.0; pixelValueVertex005_b = 0.0        
    pixelValueVertex006_r = 0.0; pixelValueVertex006_g = 0.0; pixelValueVertex006_b = 0.0
                            
    ii = 0  # ii is just a number for debugging 
    for y in y_list: 
        for x in x_list:        
            print
            print
            print 'this is the ', ii+1, 'sampled pixel!'
            ii += 1
            target = nuke.toNode('Reformat1')   # point to the node in the Nuke DAG that will be sampled, needed to be changed.
            valueR = nuke.sample(target, 'red', x, y)    # sample the pixel value of given coordinate
            valueG = nuke.sample(target, 'green', x, y)    
            valueB = nuke.sample(target, 'blue', x, y)        
            avgPV = (valueR + valueG + valueB)/3   # average pixel value of the given coordinate
            p = (x,y)   # put the x, y coordinate in a tuple for following calcuation
           
            print 'sampled pixel coord is ', p,'R= ', valueR, 'G= ', valueG, 'B= ', valueB, 'avg pixel value= ', avgPV
            
            
            # assign initial pixel value for each vertex
            #p_value = avgPV
            p_value_r = valueR
            p_value_g = valueG
            p_value_b = valueB
            
            # huge assignment, assign xy coordinate for each vertex
            vert_1 = (0.0,0.0)
            vert_2 = (1.0,0.0)
            vert_3 = (4.0,0.0)
            vert_4 = (4.0,2.0)
            vert_5 = (3.0,2.0)
            vert_6 = (0.0,2.0)
            
            # huge assignment, each triangle is declared as a list with the vertex numbering as the odd index and the vertex coordinates as the even index
            tri_1 = ['vertex001', vert_1, 'vertex002', vert_2, 'vertex006', vert_6]
            tri_2 = ['vertex002', vert_2, 'vertex003', vert_3, 'vertex005', vert_5]
            tri_3 = ['vertex005', vert_5, 'vertex004', vert_4, 'vertex003', vert_3]
            tri_4 = ['vertex005', vert_5, 'vertex002', vert_2, 'vertex006', vert_6]
            
            tri_grp = (tri_1, tri_2, tri_3, tri_4)
            
            for i in range(4): # the number in the range() will be the total number of triangles
                vert_coord = tri_grp[i]   
                # the three vertices of the queried triangle will be temparaily substituded as vertex A(ta), B(tb), C(tc).
                ta = vert_coord[1] # coordinates of vertex A
                tb = vert_coord[3]
                tc = vert_coord[5]
                #print tri_grp[i], ta, tb, tc
                #sys.exit(0)
                                
                # math equation based on John Vince book p.207
                DET = ta[0]*tb[1]+tc[0]*ta[1]+tb[0]*tc[1]-tc[0]*tb[1]-tb[0]*ta[1]-ta[0]*tc[1]                                     
                r_coeff = (p[0]*tb[1]+tc[0]*p[1]+tb[0]*tc[1]-tc[0]*tb[1]-tb[0]*p[1]-p[0]*tc[1])/DET            
                s_coeff = (ta[0]*p[1]+tc[0]*ta[1]+p[0]*tc[1]-tc[0]*p[1]-p[0]*ta[1]-ta[0]*tc[1])/DET
                t_coeff = (ta[0]*tb[1]+p[0]*ta[1]+tb[0]*p[1]-p[0]*tb[1]-tb[0]*ta[1]-ta[0]*p[1])/DET
                total_coeff = r_coeff + s_coeff + t_coeff
                
            
                j = i + 1 #just for displaying the correct corresponding number of triangle during debugging
                print 'this is the %d triangle' %j
                print 'total_coeff: ', total_coeff
                print 'DET: ', DET
                print 'r_coeff: ', r_coeff
                print 's_coeff: ', s_coeff
                print 't_coeff: ', t_coeff
            
                if total_coeff <= 1.0 and 0 <= r_coeff <=1.0 and 0 <= s_coeff <= 1.0 and 0 <= t_coeff <= 1.0: # if the sampled inside the triangle
                    print 'the sampled point is inside the triangle'
                    
                    def distance(p1, p2): #define a function to calculate the distance between two points
                        return math.hypot(p1[0]-p2[0], p1[1]-p2[1])
                    side_ab = distance(ta, tb)
                    side_bc = distance(tb, tc)
                    side_ca = distance(tc, ta)
                    s = 0.5 * ( side_ab + side_bc + side_ca)
                    triArea = math.sqrt(s * (s - side_ab) * (s - side_bc) * (s - side_ca)) #area of the triangle
                    print 'triArea= ', triArea
                    
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
                    print 'intTraArea_a= ',intTriArea_a
            
                    side_pc = distance(p, tc)
                    side_ca = distance(tc, ta)
                    side_ap = distance(ta, p)
                    sb = 0.5 * ( side_pc + side_ca + side_ap)                
                    if (sb-side_pc)<0.00001 or (sb-side_ca)<0.00001 or (sb-side_ap)<0.00001:
                        intTriArea_b = 0
                    else:    
                        intTriArea_b = math.sqrt(sb * (sb - side_pc) * (sb - side_ca) * (sb - side_ap)) #area of the 1st internal triangle PCA
                    baryCoeff_b = intTriArea_b/triArea                
                    print 'intTraArea_b= ',intTriArea_b, 'side_pc= ', side_pc, 'side_ca= ', side_ca, 'side_ap= ', side_ap, 'sb= ', sb
            
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
                    print 'intTraArea_c= ',intTriArea_c
                    
                    sum_bary_coeff = baryCoeff_a + baryCoeff_b + baryCoeff_c
                    print 'baryCoeff_a = ',baryCoeff_a, 'baryCoeff_b = ',baryCoeff_b, 'baryCoeff_c = ',baryCoeff_c, 'sum_bary_coeff = ', sum_bary_coeff
                    if sum_bary_coeff > 1.01:
                        print 'sum_bary_coeff= ',sum_bary_coeff, 'something is wrong'
                        print 
                    #pv_at_ta = p_value * baryCoeff_a #pixel value at vertex A
                    #pv_at_tb = p_value * baryCoeff_b #pixel value at vertex B
                    #pv_at_tc = p_value * baryCoeff_c #pixel value at vertex C
                    pv_at_ta_r = p_value_r * baryCoeff_a
                    pv_at_ta_g = p_value_g * baryCoeff_a
                    pv_at_ta_b = p_value_b * baryCoeff_a
                    pv_at_tb_r = p_value_r * baryCoeff_b
                    pv_at_tb_g = p_value_g * baryCoeff_b
                    pv_at_tb_b = p_value_b * baryCoeff_b
                    pv_at_tc_r = p_value_r * baryCoeff_c
                    pv_at_tc_g = p_value_g * baryCoeff_c
                    pv_at_tc_b = p_value_b * baryCoeff_c
            
                    pixelValueATemp = [vert_coord[0],pv_at_ta_r, pv_at_ta_g, pv_at_ta_b]
                    pixelValueBTemp = [vert_coord[2],pv_at_tb_r, pv_at_tb_g, pv_at_tb_b]
                    pixelValueCTemp = [vert_coord[4],pv_at_tc_r, pv_at_tc_g, pv_at_tc_b]
                            
                    print 'pixelValueATemp= ',pixelValueATemp, 'pixelValueBTemp= ',pixelValueBTemp, 'pixelValueCTemp= ',pixelValueCTemp
                    
                    if pixelValueATemp[0] == 'vertex001':
                        #print 'pixelValueVertex001= ',pixelValueVertex001
                        pixelValueVertex001_r = pixelValueVertex001_r + pv_at_ta_r
                        pixelValueVertex001_g = pixelValueVertex001_g + pv_at_ta_g
                        pixelValueVertex001_b = pixelValueVertex001_b + pv_at_ta_b
                    if pixelValueBTemp[0] == 'vertex001':
                        #print 'pixelValueVertex001= ',pixelValueVertex001
                        pixelValueVertex001_r = pixelValueVertex001_r + pv_at_tb_r
                        pixelValueVertex001_g = pixelValueVertex001_g + pv_at_tb_g
                        pixelValueVertex001_b = pixelValueVertex001_b + pv_at_tb_b
                    if pixelValueCTemp[0] == 'vertex001':
                        #print 'pixelValueVertex001= ',pixelValueVertex001
                        pixelValueVertex001_r = pixelValueVertex001_r + pv_at_tc_r
                        pixelValueVertex001_g = pixelValueVertex001_g + pv_at_tc_g
                        pixelValueVertex001_b = pixelValueVertex001_b + pv_at_tc_b
                        
                    if pixelValueATemp[0] == 'vertex002':
                        #print 'pixelValueVertex002= ',pixelValueVertex002                    
                        pixelValueVertex002_r = pixelValueVertex002_r + pv_at_ta_r
                        pixelValueVertex002_g = pixelValueVertex002_g + pv_at_ta_g
                        pixelValueVertex002_b = pixelValueVertex002_b + pv_at_ta_b
                    if pixelValueBTemp[0] == 'vertex002':
                        #print 'pixelValueVertex002= ',pixelValueVertex002                    
                        pixelValueVertex002_r = pixelValueVertex002_r + pv_at_tb_r
                        pixelValueVertex002_g = pixelValueVertex002_g + pv_at_tb_g
                        pixelValueVertex002_b = pixelValueVertex002_b + pv_at_tb_b
                    if pixelValueCTemp[0] == 'vertex002':
                        #print 'pixelValueVertex002= ',pixelValueVertex002                    
                        pixelValueVertex002_r = pixelValueVertex002_r + pv_at_tc_r
                        pixelValueVertex002_g = pixelValueVertex002_g + pv_at_tc_g
                        pixelValueVertex002_b = pixelValueVertex002_b + pv_at_tc_b
                        
                    if pixelValueATemp[0] == 'vertex003':
                        #print 'pixelValueVertex003= ',pixelValueVertex003                    
                        pixelValueVertex003_r = pixelValueVertex003_r + pv_at_ta_r
                        pixelValueVertex003_g = pixelValueVertex003_g + pv_at_ta_g
                        pixelValueVertex003_b = pixelValueVertex003_b + pv_at_ta_b
                    if pixelValueBTemp[0] == 'vertex003':
                        #print 'pixelValueVertex003= ',pixelValueVertex003                    
                        pixelValueVertex003_r = pixelValueVertex003_r + pv_at_tb_r
                        pixelValueVertex003_g = pixelValueVertex003_g + pv_at_tb_g
                        pixelValueVertex003_b = pixelValueVertex003_b + pv_at_tb_b
                    if pixelValueCTemp[0] == 'vertex003':
                        #print 'pixelValueVertex003= ',pixelValueVertex003                    
                        pixelValueVertex003_r = pixelValueVertex003_r + pv_at_tc_r
                        pixelValueVertex003_g = pixelValueVertex003_g + pv_at_tc_g
                        pixelValueVertex003_b = pixelValueVertex003_b + pv_at_tc_b
                    
                    if pixelValueATemp[0] == 'vertex004':
                        #print 'pixelValueVertex004= ',pixelValueVertex004                    
                        pixelValueVertex004_r = pixelValueVertex004_r + pv_at_ta_r
                        pixelValueVertex004_g = pixelValueVertex004_g + pv_at_ta_g
                        pixelValueVertex004_b = pixelValueVertex004_b + pv_at_ta_b
                    if pixelValueBTemp[0] == 'vertex004':
                        #print 'pixelValueVertex004= ',pixelValueVertex004                    
                        pixelValueVertex004_r = pixelValueVertex004_r + pv_at_tb_r
                        pixelValueVertex004_g = pixelValueVertex004_g + pv_at_tb_g
                        pixelValueVertex004_b = pixelValueVertex004_b + pv_at_tb_b
                    if pixelValueCTemp[0] == 'vertex004':
                        #print 'pixelValueVertex004= ',pixelValueVertex004                    
                        pixelValueVertex004_r = pixelValueVertex004_r + pv_at_tc_r
                        pixelValueVertex004_g = pixelValueVertex004_g + pv_at_tc_g
                        pixelValueVertex004_b = pixelValueVertex004_b + pv_at_tc_b
                    
                    if pixelValueATemp[0] == 'vertex005':
                        #print 'pixelValueVertex005= ',pixelValueVertex005                    
                        pixelValueVertex005_r = pixelValueVertex005_r + pv_at_ta_r
                        pixelValueVertex005_g = pixelValueVertex005_g + pv_at_ta_g
                        pixelValueVertex005_b = pixelValueVertex005_b + pv_at_ta_b
                    if pixelValueBTemp[0] == 'vertex005':
                        #print 'pixelValueVertex005= ',pixelValueVertex005                    
                        pixelValueVertex005_r = pixelValueVertex005_r + pv_at_tb_r
                        pixelValueVertex005_g = pixelValueVertex005_g + pv_at_tb_g
                        pixelValueVertex005_b = pixelValueVertex005_b + pv_at_tb_b
                    if pixelValueCTemp[0] == 'vertex005':
                        #print 'pixelValueVertex005= ',pixelValueVertex005                    
                        pixelValueVertex005_r = pixelValueVertex005_r + pv_at_tc_r
                        pixelValueVertex005_g = pixelValueVertex005_g + pv_at_tc_g
                        pixelValueVertex005_b = pixelValueVertex005_b + pv_at_tc_b
                        
                    if pixelValueATemp[0] == 'vertex006':
                        #print 'pixelValueVertex006= ',pixelValueVertex006                    
                        pixelValueVertex006_r = pixelValueVertex006_r + pv_at_ta_r
                        pixelValueVertex006_g = pixelValueVertex006_g + pv_at_ta_g
                        pixelValueVertex006_b = pixelValueVertex006_b + pv_at_ta_b
                    if pixelValueBTemp[0] == 'vertex006':
                        #print 'pixelValueVertex006= ',pixelValueVertex006                    
                        pixelValueVertex006_r = pixelValueVertex006_r + pv_at_tb_r
                        pixelValueVertex006_g = pixelValueVertex006_g + pv_at_tb_g
                        pixelValueVertex006_b = pixelValueVertex006_b + pv_at_tb_b
                    if pixelValueCTemp[0] == 'vertex006':
                        #print 'pixelValueVertex006= ',pixelValueVertex006                    
                        pixelValueVertex006_r = pixelValueVertex006_r + pv_at_tc_r
                        pixelValueVertex006_g = pixelValueVertex006_g + pv_at_tc_g
                        pixelValueVertex006_b = pixelValueVertex006_b + pv_at_tc_b
                    
                    print 'pixel value vertex 001 aum= ',pixelValueVertex001_r, pixelValueVertex001_g, pixelValueVertex001_b
                    print 'pixel value vertex 002 aum= ',pixelValueVertex002_r, pixelValueVertex002_g, pixelValueVertex002_b
                    print 'pixel value vertex 003 aum= ',pixelValueVertex003_r, pixelValueVertex003_g, pixelValueVertex003_b
                    print 'pixel value vertex 004 aum= ',pixelValueVertex004_r, pixelValueVertex004_g, pixelValueVertex004_b
                    print 'pixel value vertex 005 aum= ',pixelValueVertex005_r, pixelValueVertex005_g, pixelValueVertex005_b
                    print 'pixel value vertex 006 aum= ',pixelValueVertex006_r, pixelValueVertex006_g, pixelValueVertex006_b
                else:
                    print 'the sampled point is outside the triangle'
    
    
    print 'pixel value Vertex 001 = ', pixelValueVertex001_r, pixelValueVertex001_g, pixelValueVertex001_b
    print 'pixel value Vertex 002 = ', pixelValueVertex002_r/2, pixelValueVertex002_g/2, pixelValueVertex002_b/2
    print 'pixel value Vertex 003 = ', pixelValueVertex003_r, pixelValueVertex003_g, pixelValueVertex003_b
    print 'pixel value Vertex 004 = ', pixelValueVertex004_r, pixelValueVertex004_g, pixelValueVertex004_b
    print 'pixel value Vertex 005 = ', pixelValueVertex005_r/2, pixelValueVertex005_g/2, pixelValueVertex005_b/2
    print 'pixel value Vertex 006 = ', pixelValueVertex006_r, pixelValueVertex006_g, pixelValueVertex006_b