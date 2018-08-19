#def testFunc():
#    listA = [1, 2, 3]
#    print 'listA: ', listA
#    return listA

import sys
import nuke
import math

def preSampleHDR():
    # create 162 multiple node and name them accordingly
    # for vert in range(1,163): # vert = the number of vertices
    #    populate = nuke.nodes.Multiply(name='ls3_Vert%s' % vert)
    #    populate.setInput(0, nuke.selectedNode())
        
    hugeList = [] # the list contains vertices name and barycentric weights of each vertex
    
    y = 0.5 
    x = 0.5
    count = 0
    pixelCount = 0
    
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
                    vert_1 = [32.00007,32.00001];        vert_43 = [43.26807321,20.71623998]; vert_85 = [86.55459573,44.8054174];  vert_127 = [32.00007483,0]
                    vert_2 = [33.63806399,36.91646175];  vert_44 = [50.70254706,21.33333777]; vert_86 = [79.40907076,47.28894441]; vert_128 = [117.3586233,10.74890402]
                    vert_3 = [27.78891844,35.02615533];  vert_45 = [47.62818001,15.71294652]; vert_87 = [118.5545209,32.00000666]; vert_129 = [107.2697902,6.134704607]   
                    vert_4 = [28.88006231,40.94246662];  vert_46 = [39.83795633,37.42157091]; vert_88 = [116.9293641,36.91646175]; vert_130 = [53.35877298,10.74890402]
                    vert_5 = [22.56432309,38.39964397];  vert_47 = [43.26807321,43.28377334]; vert_89 = [113.3694152,32.00000666]; vert_131 = [56.05027343,16.54329258]
                    vert_6 = [22.55474539,44.8054174];   vert_48 = [47.62818001,48.28706679]; vert_90 = [110.715269,37.42157091];  vert_132 = [57.68736829,23.05754669]
                    vert_7 = [16.77091587,41.349502];    vert_49 = [46.71541868,37.42157091]; vert_91 = [107.2781424,32.00000666]; vert_133 = [58.77462521,28.97385798]
                    vert_8 = [15.40922041,47.28894441];  vert_50 = [50.70254706,42.66667554]; vert_92 = [103.8378067,37.42157091]; vert_134 = [63.99965354,12.80059165]
                    vert_9 = [11.26814804,43.28377334];  vert_51 = [52.92951374,36.91646175]; vert_93 = [101.1684497,32.00000666]; vert_135 = [63.99974819,19.19459592]
                    vert_10 = [35.83228279,42.66667554]; vert_52 = [75.26799838,20.71623998]; vert_94 = [114.7023974,42.66667554]; vert_136 = [63.99978579,25.60036935]
                    vert_11 = [30.5114255,47.45672074];  vert_53 = [79.40907076,16.71106891]; vert_95 = [107.2679235,43.28377334]; vert_137 = [71.13602275,16.71106891]
                    vert_12 = [22.55474539,51.19942166]; vert_54 = [80.77076622,22.65051132]; vert_96 = [111.6280303,48.28706679]; vert_138 = [69.77866679,22.65051132]
                    vert_13 = [38.93311627,48.28706679]; vert_55 = [86.55459573,19.19459592]; vert_97 = [111.6280303,15.71294652]; vert_139 = [58.77462521,35.02615533]
                    vert_14 = [33.21606598,53.2511093];  vert_56 = [86.56417344,25.60036935]; vert_98 = [107.2679235,20.71623998]; vert_140 = [57.68736829,40.94246662]
                    vert_15 = [43.26875682,52.73622503]; vert_57 = [92.87991265,23.05754669]; vert_99 = [103.8378067,26.57844241]; vert_141 = [56.05027343,47.45672074]
                    vert_16 = [27.78891844,28.97385798]; vert_58 = [91.78876878,28.97385798]; vert_100 = [114.7023974,21.33333777];vert_142 = [53.41907018,53.2511093]
                    vert_17 = [22.55474539,32.00000666]; vert_59 = [97.63791433,27.08355156]; vert_101 = [110.715269,26.57844241]; vert_143 = [63.99978579,38.39964397]
                    vert_18 = [22.56432309,25.60036935]; vert_60 = [95.99992517,32.00000666]; vert_102 = [116.9293641,27.08355156];vert_144 = [63.99974819,44.8054174]
                    vert_19 = [16.77372196,28.68516064]; vert_61 = [86.55459573,12.80059165]; vert_103 = [43.26993988,57.86530871];vert_145 = [63.99965354,51.19942166]
                    vert_20 = [16.77091587,22.65051132]; vert_62 = [94.51127584,16.54329258]; vert_104 = [22.55474539,57.59628721];vert_146 = [69.77866679,41.349502]
                    vert_21 = [11.26907516,25.89954766]; vert_63 = [99.83213313,21.33333777]; vert_105 = [11.26883165,52.73622503];vert_147 = [71.13602275,47.28894441]
                    vert_22 = [11.26814804,20.71623998]; vert_64 = [97.21591632,10.74890402]; vert_106 = [7.136172407,47.28894441];vert_148 = [75.26868199,11.26378829]
                    vert_23 = [16.77372196,35.31485267]; vert_65 = [102.9329666,15.71294652]; vert_107 = [32.00007483,64.00001331];vert_149 = [86.55459573,6.4037261]
                    vert_24 = [11.27836688,32.00000666]; vert_66 = [107.2686072,11.26378829]; vert_108 = [0.000808941,57.59628721];vert_150 = [63.99934072,6.4037261]
                    vert_25 = [11.26907516,38.10046566]; vert_67 = [75.26799838,43.28377334]; vert_109 = [0.000496118,51.19942166];vert_151 = [69.77726207,35.31485267]
                    vert_26 = [33.63806399,27.08355156]; vert_68 = [75.2689255,38.10046566];  vert_110 = [107.2697902,57.86530871];vert_152 = [69.77726207,28.68516064]
                    vert_27 = [28.88006231,23.05754669]; vert_69 = [80.77076622,41.349502];   vert_111 = [117.3586233,53.2511093]; vert_153 = [63.99979628,32.00000666]
                    vert_28 = [35.83228279,21.33333777]; vert_70 = [80.7735723,35.31485267];  vert_112 = [5.77881645,41.349502];   vert_154 = [86.55459573,57.59628721]
                    vert_29 = [30.5114255,16.54329258];  vert_71 = [86.56417344,38.39964397]; vert_113 = [5.777411726,35.31485267];vert_155 = [75.26868199,52.73622503]
                    vert_30 = [38.93311627,15.71294652]; vert_72 = [86.55459573,32.00000666]; vert_114 = [5.777411726,28.68516064];vert_156 = [63.99934072,57.59628721]
                    vert_31 = [33.21606598,10.74890402]; vert_73 = [91.78876878,35.02615533]; vert_115 = [5.77881645,22.65051132]; vert_157 = [121.6872186,40.94246662]
                    vert_32 = [43.26875682,11.26378829]; vert_74 = [75.27821722,32.00000666]; vert_116 = [0.000363874,38.39964397];vert_158 = [120.0501238,47.45672074]
                    vert_33 = [22.55474539,19.19459592]; vert_75 = [80.7735723,28.68516064];  vert_117 = [0.000353377,32.00000666];vert_159 = [0.000401474,44.8054174]
                    vert_34 = [22.55474539,12.80059165]; vert_76 = [75.2689255,25.89954766];  vert_118 = [0.000363874,25.60036935];vert_160 = [120.0501238,16.54329258]
                    vert_35 = [15.40922041,16.71106891]; vert_77 = [107.2686072,52.73622503]; vert_119 = [122.7744755,35.02615533];vert_161 = [121.6872186,23.05754669]
                    vert_36 = [37.16859935,32.00000666]; vert_78 = [97.21591632,53.2511093];  vert_120 = [122.7744755,28.97385798];vert_162 = [0.000401474,19.19459592]
                    vert_37 = [39.83795633,26.57844241]; vert_79 = [102.9329666,48.28706679]; vert_121 = [7.136172407,16.71106891]
                    vert_38 = [43.27829205,32.00000666]; vert_80 = [94.51127584,47.45672074]; vert_122 = [11.26883165,11.26378829]
                    vert_39 = [46.71541868,26.57844241]; vert_81 = [99.83213313,42.66667554]; vert_123 = [22.55474539,6.4037261]
                    vert_40 = [49.36956484,32.00000666]; vert_82 = [92.87991265,40.94246662]; vert_124 = [43.26993988,6.134704607]
                    vert_41 = [52.92951374,27.08355156]; vert_83 = [97.63791433,36.91646175]; vert_125 = [0.000496118,12.80059165]
                    vert_42 = [54.55467056,32.00000666]; vert_84 = [86.55459573,51.19942166]; vert_126 = [0.000808941,6.4037261]
                    # extra vertices to address the north pole sampling issue
                    vert_163 = [11.277,64.0]; vert_164 = [32.91,64.0]; vert_165 = [53.635,64.0]; vert_166 = [75.275,64.0]; vert_167 = [96.91,64.0]
                    vert_168 = [117.635,64.0]; vert_169 = [0.0,64.0]; vert_170 = [128.0,64.0]; vert_171 = [128.0,57.59628721]
                    # extra vertices to address the south pole sampling issue
                    vert_172 = [11.275,0.0]; vert_173 = [32.91,0.0]; vert_174 = [53.635,0.0]; vert_175 = [75.275,0.0]; vert_176 = [96.91,0.0]
                    vert_177 = [117.635,0.0]; vert_178 = [0.0,0.0]; vert_179 = [128.0,0.0]; vert_180 = [128.0,6.4037261]
                                            
                    # huge assignment, each triangle is declared as a list with the vertex numbering as the odd index and the vertex coordinates as the even index
                    tri_1 = ['vertex001', vert_1, 'vertex002', vert_2, 'vertex003', vert_3]
                    tri_2 = ['vertex003', vert_3, 'vertex004', vert_4, 'vertex005', vert_5]
                    tri_3 = ['vertex005', vert_5, 'vertex006', vert_6, 'vertex007', vert_7]
                    tri_4 = ['vertex007', vert_7, 'vertex008', vert_8, 'vertex009', vert_9]
                    tri_5 = ['vertex002', vert_2, 'vertex004', vert_4, 'vertex010', vert_10]
                    tri_6 = ['vertex004', vert_4, 'vertex006', vert_6, 'vertex011', vert_11]
                    tri_7 = ['vertex006', vert_6, 'vertex008', vert_8, 'vertex012', vert_12]
                    tri_8 = ['vertex010', vert_10, 'vertex011', vert_11, 'vertex013', vert_13] 
                    tri_9 = ['vertex011', vert_11, 'vertex012', vert_12, 'vertex014', vert_14]
                    tri_10 = ['vertex013', vert_13, 'vertex014', vert_14, 'vertex015', vert_15]
                    tri_11 = ['vertex002', vert_2, 'vertex003', vert_3, 'vertex004', vert_4]
                    tri_12 = ['vertex004', vert_4, 'vertex005', vert_5, 'vertex006', vert_6]
                    tri_13 = ['vertex006', vert_6, 'vertex007', vert_7, 'vertex008', vert_8]
                    tri_14 = ['vertex004', vert_4, 'vertex010', vert_10, 'vertex011', vert_11]
                    tri_15 = ['vertex006', vert_6, 'vertex011', vert_11, 'vertex012', vert_12]
                    tri_16 = ['vertex011', vert_11, 'vertex013', vert_13, 'vertex014', vert_14]
                    tri_17 = ['vertex001', vert_1, 'vertex003', vert_3, 'vertex016', vert_16]
                    tri_18 = ['vertex016', vert_16, 'vertex017', vert_17, 'vertex018', vert_18]
                    tri_19 = ['vertex018', vert_18, 'vertex019', vert_19, 'vertex020', vert_20]
                    tri_20 = ['vertex020', vert_20, 'vertex021', vert_21, 'vertex022', vert_22]                
                    tri_21 = ['vertex003', vert_3, 'vertex005', vert_5, 'vertex017', vert_17]
                    tri_22 = ['vertex017', vert_17, 'vertex019', vert_19, 'vertex023', vert_23]
                    tri_23 = ['vertex019', vert_19, 'vertex021', vert_21, 'vertex024', vert_24]
                    tri_24 = ['vertex005', vert_5, 'vertex007', vert_7, 'vertex023', vert_23]
                    tri_25 = ['vertex023', vert_23, 'vertex024', vert_24, 'vertex025', vert_25]
                    tri_26 = ['vertex007', vert_7, 'vertex009', vert_9, 'vertex025', vert_25]
                    tri_27 = ['vertex003', vert_3, 'vertex016', vert_16, 'vertex017', vert_17]
                    tri_28 = ['vertex017', vert_17, 'vertex018', vert_18, 'vertex019', vert_19]
                    tri_29 = ['vertex019', vert_19, 'vertex020', vert_20, 'vertex021', vert_21]
                    tri_30 = ['vertex005', vert_5, 'vertex017', vert_17, 'vertex023', vert_23] 
                    tri_31 = ['vertex019', vert_19, 'vertex023', vert_23, 'vertex024', vert_24] 
                    tri_32 = ['vertex007', vert_7, 'vertex023', vert_23, 'vertex025', vert_25]
                    tri_33 = ['vertex001', vert_1, 'vertex016', vert_16, 'vertex026', vert_26]
                    tri_34 = ['vertex026', vert_26, 'vertex027', vert_27, 'vertex028', vert_28]
                    tri_35 = ['vertex028', vert_28, 'vertex029', vert_29, 'vertex030', vert_30]
                    tri_36 = ['vertex030', vert_30, 'vertex031', vert_31, 'vertex032', vert_32]
                    tri_37 = ['vertex016', vert_16, 'vertex018', vert_18, 'vertex027', vert_27]
                    tri_38 = ['vertex027', vert_27, 'vertex029', vert_29, 'vertex033', vert_33]
                    tri_39 = ['vertex029', vert_29, 'vertex031', vert_31, 'vertex034', vert_34]
                    tri_40 = ['vertex018', vert_18, 'vertex020', vert_20, 'vertex033', vert_33]
                    tri_41 = ['vertex033', vert_33, 'vertex034', vert_34, 'vertex035', vert_35]
                    tri_42 = ['vertex020', vert_20, 'vertex022', vert_22, 'vertex035', vert_35]
                    tri_43 = ['vertex016', vert_16, 'vertex026', vert_26, 'vertex027', vert_27]
                    tri_44 = ['vertex027', vert_27, 'vertex028', vert_28, 'vertex029', vert_29]
                    tri_45 = ['vertex029', vert_29, 'vertex030', vert_30, 'vertex031', vert_31]
                    tri_46 = ['vertex018', vert_18, 'vertex027', vert_27, 'vertex033', vert_33]
                    tri_47 = ['vertex029', vert_29, 'vertex033', vert_33, 'vertex034', vert_34]                
                    tri_48 = ['vertex020', vert_20, 'vertex033', vert_33, 'vertex035', vert_35]
                    tri_49 = ['vertex001', vert_1, 'vertex026', vert_26, 'vertex036', vert_36]
                    tri_50 = ['vertex036', vert_36, 'vertex037', vert_37, 'vertex038', vert_38]
                    tri_51 = ['vertex038', vert_38, 'vertex039', vert_39, 'vertex040', vert_40]
                    tri_52 = ['vertex040', vert_40, 'vertex041', vert_41, 'vertex042', vert_42]
                    tri_53 = ['vertex026', vert_26, 'vertex028', vert_28, 'vertex037', vert_37]
                    tri_54 = ['vertex037', vert_37, 'vertex039', vert_39, 'vertex043', vert_43]
                    tri_55 = ['vertex039', vert_39, 'vertex041', vert_41, 'vertex044', vert_44]
                    tri_56 = ['vertex028', vert_28, 'vertex030', vert_30, 'vertex043', vert_43]
                    tri_57 = ['vertex043', vert_43, 'vertex044', vert_44, 'vertex045', vert_45]
                    tri_58 = ['vertex030', vert_30, 'vertex032', vert_32, 'vertex045', vert_45]
                    tri_59 = ['vertex026', vert_26, 'vertex036', vert_36, 'vertex037', vert_37]                
                    tri_60 = ['vertex037', vert_37, 'vertex038', vert_38, 'vertex039', vert_39]                 
                    tri_61 = ['vertex039', vert_39, 'vertex040', vert_40, 'vertex041', vert_41]
                    tri_62 = ['vertex028', vert_28, 'vertex037', vert_37, 'vertex043', vert_43]
                    tri_63 = ['vertex039', vert_39, 'vertex043', vert_43, 'vertex044', vert_44] 
                    tri_64 = ['vertex030', vert_30, 'vertex043', vert_43, 'vertex045', vert_45]
                    tri_65 = ['vertex001', vert_1, 'vertex002', vert_2, 'vertex036', vert_36]
                    tri_66 = ['vertex002', vert_2, 'vertex010', vert_10, 'vertex046', vert_46]
                    tri_67 = ['vertex010', vert_10, 'vertex013', vert_13, 'vertex047', vert_47]
                    tri_68 = ['vertex013', vert_13, 'vertex015', vert_15, 'vertex048', vert_48]
                    tri_69 = ['vertex036', vert_36, 'vertex038', vert_38, 'vertex046', vert_46]
                    tri_70 = ['vertex046', vert_46, 'vertex047', vert_47, 'vertex049', vert_49]
                    tri_71 = ['vertex047', vert_47, 'vertex048', vert_48, 'vertex050', vert_50]
                    tri_72 = ['vertex038', vert_38, 'vertex040', vert_40, 'vertex049', vert_49]
                    tri_73 = ['vertex049', vert_49, 'vertex050', vert_50, 'vertex051', vert_51]
                    tri_74 = ['vertex040', vert_40, 'vertex042', vert_42, 'vertex051', vert_51]
                    tri_75 = ['vertex002', vert_2, 'vertex036', vert_36, 'vertex046', vert_46]
                    tri_76 = ['vertex010', vert_10, 'vertex046', vert_46, 'vertex047', vert_47]
                    tri_77 = ['vertex013', vert_13, 'vertex047', vert_47, 'vertex048', vert_48]
                    tri_78 = ['vertex038', vert_38, 'vertex046', vert_46, 'vertex049', vert_49]
                    tri_79 = ['vertex047', vert_47, 'vertex049', vert_49, 'vertex050', vert_50]
                    tri_80 = ['vertex040', vert_40, 'vertex049', vert_49, 'vertex051', vert_51]                
                    tri_81 = ['vertex052', vert_52, 'vertex053', vert_53, 'vertex054', vert_54]
                    tri_82 = ['vertex054', vert_54, 'vertex055', vert_55, 'vertex056', vert_56]
                    tri_83 = ['vertex056', vert_56, 'vertex057', vert_57, 'vertex058', vert_58]
                    tri_84 = ['vertex058', vert_58, 'vertex059', vert_59, 'vertex060', vert_60]
                    tri_85 = ['vertex053', vert_53, 'vertex055', vert_55, 'vertex061', vert_61]
                    tri_86 = ['vertex055', vert_55, 'vertex057', vert_57, 'vertex062', vert_62]
                    tri_87 = ['vertex057', vert_57, 'vertex059', vert_59, 'vertex063', vert_63]
                    tri_88 = ['vertex061', vert_61, 'vertex062', vert_62, 'vertex064', vert_64]
                    tri_89 = ['vertex062', vert_62, 'vertex063', vert_63, 'vertex065', vert_65]
                    tri_90 = ['vertex064', vert_64, 'vertex065', vert_65, 'vertex066', vert_66]
                    tri_91 = ['vertex053', vert_53, 'vertex054', vert_54, 'vertex055', vert_55]
                    tri_92 = ['vertex055', vert_55, 'vertex056', vert_56, 'vertex057', vert_57]
                    tri_93 = ['vertex057', vert_57, 'vertex058', vert_58, 'vertex059', vert_59]
                    tri_94 = ['vertex055', vert_55, 'vertex061', vert_61, 'vertex062', vert_62]
                    tri_95 = ['vertex057', vert_57, 'vertex062', vert_62, 'vertex063', vert_63]
                    tri_96 = ['vertex062', vert_62, 'vertex064', vert_64, 'vertex065', vert_65]
                    tri_97 = ['vertex067', vert_67, 'vertex068', vert_68, 'vertex069', vert_69]
                    tri_98 = ['vertex069', vert_69, 'vertex070', vert_70, 'vertex071', vert_71]
                    tri_99 = ['vertex071', vert_71, 'vertex072', vert_72, 'vertex073', vert_73]
                    tri_100 = ['vertex058', vert_58, 'vertex060', vert_60, 'vertex073', vert_73]
                    tri_101 = ['vertex068', vert_68, 'vertex070', vert_70, 'vertex074', vert_74]
                    tri_102 = ['vertex070', vert_70, 'vertex072', vert_72, 'vertex075', vert_75]
                    tri_103 = ['vertex056', vert_56, 'vertex058', vert_58, 'vertex072', vert_72]
                    tri_104 = ['vertex074', vert_74, 'vertex075', vert_75, 'vertex076', vert_76]
                    tri_105 = ['vertex054', vert_54, 'vertex056', vert_56, 'vertex075', vert_75]
                    tri_106 = ['vertex052', vert_52, 'vertex054', vert_54, 'vertex076', vert_76]
                    tri_107 = ['vertex068', vert_68, 'vertex069', vert_69, 'vertex070', vert_70]
                    tri_108 = ['vertex070', vert_70, 'vertex071', vert_71, 'vertex072', vert_72]
                    tri_109 = ['vertex058', vert_58, 'vertex072', vert_72, 'vertex073', vert_73]
                    tri_110 = ['vertex070', vert_70, 'vertex074', vert_74, 'vertex075', vert_75]
                    tri_111 = ['vertex056', vert_56, 'vertex072', vert_72, 'vertex075', vert_75]
                    tri_112 = ['vertex054', vert_54, 'vertex075', vert_75, 'vertex076', vert_76]
                    tri_113 = ['vertex077', vert_77, 'vertex078', vert_78, 'vertex079', vert_79]
                    tri_114 = ['vertex079', vert_79, 'vertex080', vert_80, 'vertex081', vert_81]
                    tri_115 = ['vertex081', vert_81, 'vertex082', vert_82, 'vertex083', vert_83]
                    tri_116 = ['vertex060', vert_60, 'vertex073', vert_73, 'vertex083', vert_83]
                    tri_117 = ['vertex078', vert_78, 'vertex080', vert_80, 'vertex084', vert_84]
                    tri_118 = ['vertex080', vert_80, 'vertex082', vert_82, 'vertex085', vert_85]
                    tri_119 = ['vertex071', vert_71, 'vertex073', vert_73, 'vertex082', vert_82]
                    tri_120 = ['vertex084', vert_84, 'vertex085', vert_85, 'vertex086', vert_86]
                    tri_121 = ['vertex069', vert_69, 'vertex071', vert_71, 'vertex085', vert_85]
                    tri_122 = ['vertex067', vert_67, 'vertex069', vert_69, 'vertex086', vert_86]
                    tri_123 = ['vertex078', vert_78, 'vertex079', vert_79, 'vertex080', vert_80]
                    tri_124 = ['vertex080', vert_80, 'vertex081', vert_81, 'vertex082', vert_82]
                    tri_125 = ['vertex073', vert_73, 'vertex082', vert_82, 'vertex083', vert_83]
                    tri_126 = ['vertex080', vert_80, 'vertex084', vert_84, 'vertex085', vert_85]
                    tri_127 = ['vertex071', vert_71, 'vertex082', vert_82, 'vertex085', vert_85]
                    tri_128 = ['vertex069', vert_69, 'vertex085', vert_85, 'vertex086', vert_86]
                    tri_129 = ['vertex087', vert_87, 'vertex088', vert_88, 'vertex089', vert_89]
                    tri_130 = ['vertex089', vert_89, 'vertex090', vert_90, 'vertex091', vert_91]
                    tri_131 = ['vertex091', vert_91, 'vertex092', vert_92, 'vertex093', vert_93]
                    tri_132 = ['vertex060', vert_60, 'vertex083', vert_83, 'vertex093', vert_93]
                    tri_133 = ['vertex088', vert_88, 'vertex090', vert_90, 'vertex094', vert_94]
                    tri_134 = ['vertex090', vert_90, 'vertex092', vert_92, 'vertex095', vert_95]
                    tri_135 = ['vertex081', vert_81, 'vertex083', vert_83, 'vertex092', vert_92]
                    tri_136 = ['vertex094', vert_94, 'vertex095', vert_95, 'vertex096', vert_96]
                    tri_137 = ['vertex079', vert_79, 'vertex081', vert_81, 'vertex095', vert_95]
                    tri_138 = ['vertex077', vert_77, 'vertex079', vert_79, 'vertex096', vert_96]
                    tri_139 = ['vertex088', vert_88, 'vertex089', vert_89, 'vertex090', vert_90]
                    tri_140 = ['vertex090', vert_90, 'vertex091', vert_91, 'vertex092', vert_92]
                    tri_141 = ['vertex083', vert_83, 'vertex092', vert_92, 'vertex093', vert_93]
                    tri_142 = ['vertex090', vert_90, 'vertex094', vert_94, 'vertex095', vert_95]
                    tri_143 = ['vertex081', vert_81, 'vertex092', vert_92, 'vertex095', vert_95]
                    tri_144 = ['vertex079', vert_79, 'vertex095', vert_95, 'vertex096', vert_96]
                    tri_145 = ['vertex065', vert_65, 'vertex066', vert_66, 'vertex097', vert_97]
                    tri_146 = ['vertex063', vert_63, 'vertex065', vert_65, 'vertex098', vert_98]
                    tri_147 = ['vertex059', vert_59, 'vertex063', vert_63, 'vertex099', vert_99]
                    tri_148 = ['vertex059', vert_59, 'vertex060', vert_60, 'vertex093', vert_93]
                    tri_149 = ['vertex097', vert_97, 'vertex098', vert_98, 'vertex100', vert_100]
                    tri_150 = ['vertex098', vert_98, 'vertex099', vert_99, 'vertex101', vert_101]
                    tri_151 = ['vertex091', vert_91, 'vertex093', vert_93, 'vertex099', vert_99]
                    tri_152 = ['vertex100', vert_100, 'vertex101', vert_101, 'vertex102', vert_102]
                    tri_153 = ['vertex089', vert_89, 'vertex091', vert_91, 'vertex101', vert_101]
                    tri_154 = ['vertex087', vert_87, 'vertex089', vert_89, 'vertex102', vert_102]
                    tri_155 = ['vertex065', vert_65, 'vertex097', vert_97, 'vertex098', vert_98]
                    tri_156 = ['vertex063', vert_63, 'vertex098', vert_98, 'vertex099', vert_99]
                    tri_157 = ['vertex059', vert_59, 'vertex093', vert_93, 'vertex099', vert_99]
                    tri_158 = ['vertex098', vert_98, 'vertex100', vert_100, 'vertex101', vert_101]
                    tri_159 = ['vertex091', vert_91, 'vertex099', vert_99, 'vertex101', vert_101]
                    tri_160 = ['vertex089', vert_89, 'vertex101', vert_101, 'vertex102', vert_102]
                    tri_161 = ['vertex014', vert_14, 'vertex015', vert_15, 'vertex103', vert_103]
                    tri_162 = ['vertex012', vert_12, 'vertex014', vert_14, 'vertex104', vert_104]
                    tri_163 = ['vertex008', vert_8, 'vertex012', vert_12, 'vertex105', vert_105]
                    tri_164 = ['vertex008', vert_8, 'vertex009', vert_9, 'vertex106', vert_106]
                    #tri_165 = ['vertex103', vert_103, 'vertex104', vert_104, 'vertex107', vert_107]
                    tri_165 = ['vertex103', vert_103, 'vertex104', vert_104, 'vertex164', vert_164] #replace vertex107 by vertex_164 to address north pole issue
                    tri_166 = ['vertex104', vert_104, 'vertex105', vert_105, 'vertex108', vert_108]
                    tri_167 = ['vertex105', vert_105, 'vertex106', vert_106, 'vertex109', vert_109]
                    #tri_168 = ['vertex107', vert_107, 'vertex108', vert_108, 'vertex110', vert_110]
                    tri_168 = ['vertex168', vert_168, 'vertex171', vert_171, 'vertex110', vert_110] #replace vertex107 by vertex_168 and vertex108 by vertex171
                                                                                                    #to address north pole issue                    
                    tri_169 = ['vertex108', vert_108, 'vertex109', vert_109, 'vertex111', vert_111]
                    tri_170 = ['vertex077', vert_77, 'vertex110', vert_110, 'vertex111', vert_111]
                    tri_171 = ['vertex014', vert_14, 'vertex103', vert_103, 'vertex104', vert_104]
                    tri_172 = ['vertex012', vert_12, 'vertex104', vert_104, 'vertex105', vert_105]
                    tri_173 = ['vertex008', vert_8, 'vertex105', vert_105, 'vertex106', vert_106]
                    #tri_174 = ['vertex104', vert_104, 'vertex107', vert_107, 'vertex108', vert_108]
                    tri_174 = ['vertex104', vert_104, 'vertex163', vert_163, 'vertex108', vert_108] #replace vertex107 by vertex_163 to address north pole issue
                    tri_175 = ['vertex105', vert_105, 'vertex108', vert_108, 'vertex109', vert_109] 
                    tri_176 = ['vertex108', vert_108, 'vertex110', vert_110, 'vertex111', vert_111]
                    tri_177 = ['vertex009', vert_9, 'vertex025', vert_25, 'vertex112', vert_112]
                    tri_178 = ['vertex024', vert_24, 'vertex025', vert_25, 'vertex113', vert_113]
                    tri_179 = ['vertex021', vert_21, 'vertex024', vert_24, 'vertex114', vert_114]
                    tri_180 = ['vertex021', vert_21, 'vertex022', vert_22, 'vertex115', vert_115]
                    tri_181 = ['vertex112', vert_112, 'vertex113', vert_113, 'vertex116', vert_116]
                    tri_182 = ['vertex113', vert_113, 'vertex114', vert_114, 'vertex117', vert_117]
                    tri_183 = ['vertex114', vert_114, 'vertex115', vert_115, 'vertex118', vert_118]
                    tri_184 = ['vertex116', vert_116, 'vertex117', vert_117, 'vertex119', vert_119]
                    tri_185 = ['vertex117', vert_117, 'vertex118', vert_118, 'vertex120', vert_120]
                    tri_186 = ['vertex087', vert_87, 'vertex119', vert_119, 'vertex120', vert_120]
                    tri_187 = ['vertex025', vert_25, 'vertex112', vert_112, 'vertex113', vert_113]
                    tri_188 = ['vertex024', vert_24, 'vertex113', vert_113, 'vertex114', vert_114]
                    tri_189 = ['vertex021', vert_21, 'vertex114', vert_114, 'vertex115', vert_115]
                    tri_190 = ['vertex113', vert_113, 'vertex116', vert_116, 'vertex117', vert_117]
                    tri_191 = ['vertex114', vert_114, 'vertex117', vert_117, 'vertex118', vert_118]
                    tri_192 = ['vertex117', vert_117, 'vertex119', vert_119, 'vertex120', vert_120]
                    tri_193 = ['vertex022', vert_22, 'vertex035', vert_35, 'vertex121', vert_121]
                    tri_194 = ['vertex034', vert_34, 'vertex035', vert_35, 'vertex122', vert_122]
                    tri_195 = ['vertex031', vert_31, 'vertex034', vert_34, 'vertex123', vert_123]
                    tri_196 = ['vertex031', vert_31, 'vertex032', vert_32, 'vertex124', vert_124]
                    tri_197 = ['vertex121', vert_121, 'vertex122', vert_122, 'vertex125', vert_125]
                    tri_198 = ['vertex122', vert_122, 'vertex123', vert_123, 'vertex126', vert_126]
                    #tri_199 = ['vertex123', vert_123, 'vertex124', vert_124, 'vertex127', vert_127]
                    tri_199 = ['vertex123', vert_123, 'vertex124', vert_124, 'vertex173', vert_173] #replace vertex127 by vertex_173 to address south pole issue
                    tri_200 = ['vertex125', vert_125, 'vertex126', vert_126, 'vertex128', vert_128]
                    #tri_201 = ['vertex126', vert_126, 'vertex127', vert_127, 'vertex129', vert_129]
                    tri_201 = ['vertex180', vert_180, 'vertex177', vert_177, 'vertex129', vert_129] #replace vertex127 by vertex_177 and vertex126 to vertex180
                                                                                                    #to address south pole issue                           
                    tri_202 = ['vertex066', vert_66, 'vertex128', vert_128, 'vertex129', vert_129]
                    tri_203 = ['vertex035', vert_35, 'vertex121', vert_121, 'vertex122', vert_122]
                    tri_204 = ['vertex034', vert_34, 'vertex122', vert_122, 'vertex123', vert_123]
                    tri_205 = ['vertex031', vert_31, 'vertex123', vert_123, 'vertex124', vert_124]
                    tri_206 = ['vertex122', vert_122, 'vertex125', vert_125, 'vertex126', vert_126]
                    #tri_207 = ['vertex123', vert_123, 'vertex126', vert_126, 'vertex127', vert_127]
                    tri_207 = ['vertex123', vert_123, 'vertex126', vert_126, 'vertex172', vert_172] #replace vertex127 by vertex_172 to address south pole issue
                    tri_208 = ['vertex126', vert_126, 'vertex128', vert_128, 'vertex129', vert_129]
                    tri_209 = ['vertex032', vert_32, 'vertex045', vert_45, 'vertex130', vert_130]
                    tri_210 = ['vertex044', vert_44, 'vertex045', vert_45, 'vertex131', vert_131]
                    tri_211 = ['vertex041', vert_41, 'vertex044', vert_44, 'vertex132', vert_132]
                    tri_212 = ['vertex041', vert_41, 'vertex042', vert_42, 'vertex133', vert_133]
                    tri_213 = ['vertex130', vert_130, 'vertex131', vert_131, 'vertex134', vert_134]
                    tri_214 = ['vertex131', vert_131, 'vertex132', vert_132, 'vertex135', vert_135]
                    tri_215 = ['vertex132', vert_132, 'vertex133', vert_133, 'vertex136', vert_136]
                    tri_216 = ['vertex134', vert_134, 'vertex135', vert_135, 'vertex137', vert_137]
                    tri_217 = ['vertex135', vert_135, 'vertex136', vert_136, 'vertex138', vert_138]
                    tri_218 = ['vertex052', vert_52, 'vertex137', vert_137, 'vertex138', vert_138]
                    tri_219 = ['vertex045', vert_45, 'vertex130', vert_130, 'vertex131', vert_131]
                    tri_220 = ['vertex044', vert_44, 'vertex131', vert_131, 'vertex132', vert_132]
                    tri_221 = ['vertex041', vert_41, 'vertex132', vert_132, 'vertex133', vert_133]
                    tri_222 = ['vertex131', vert_131, 'vertex134', vert_134, 'vertex135', vert_135]
                    tri_223 = ['vertex132', vert_132, 'vertex135', vert_135, 'vertex136', vert_136]
                    tri_224 = ['vertex135', vert_135, 'vertex137', vert_137, 'vertex138', vert_138]
                    tri_225 = ['vertex042', vert_42, 'vertex051', vert_51, 'vertex139', vert_139]
                    tri_226 = ['vertex050', vert_50, 'vertex051', vert_51, 'vertex140', vert_140]
                    tri_227 = ['vertex048', vert_48, 'vertex050', vert_50, 'vertex141', vert_141]
                    tri_228 = ['vertex015', vert_15, 'vertex048', vert_48, 'vertex142', vert_142]
                    tri_229 = ['vertex139', vert_139, 'vertex140', vert_140, 'vertex143', vert_143]
                    tri_230 = ['vertex140', vert_140, 'vertex141', vert_141, 'vertex144', vert_144]
                    tri_231 = ['vertex141', vert_141, 'vertex142', vert_142, 'vertex145', vert_145]
                    tri_232 = ['vertex143', vert_143, 'vertex144', vert_144, 'vertex146', vert_146]
                    tri_233 = ['vertex144', vert_144, 'vertex145', vert_145, 'vertex147', vert_147]
                    tri_234 = ['vertex067', vert_67, 'vertex146', vert_146, 'vertex147', vert_147]
                    tri_235 = ['vertex051', vert_51, 'vertex139', vert_139, 'vertex140', vert_140]
                    tri_236 = ['vertex050', vert_50, 'vertex140', vert_140, 'vertex141', vert_141]
                    tri_237 = ['vertex048', vert_48, 'vertex141', vert_141, 'vertex142', vert_142]
                    tri_238 = ['vertex140', vert_140, 'vertex143', vert_143, 'vertex144', vert_144]
                    tri_239 = ['vertex141', vert_141, 'vertex144', vert_144, 'vertex145', vert_145]
                    tri_240 = ['vertex144', vert_144, 'vertex146', vert_146, 'vertex147', vert_147]
                    tri_241 = ['vertex052', vert_52, 'vertex053', vert_53, 'vertex137', vert_137]
                    tri_242 = ['vertex053', vert_53, 'vertex061', vert_61, 'vertex148', vert_148]
                    tri_243 = ['vertex061', vert_61, 'vertex064', vert_64, 'vertex149', vert_149]
                    tri_244 = ['vertex064', vert_64, 'vertex066', vert_66, 'vertex129', vert_129]
                    tri_245 = ['vertex134', vert_134, 'vertex137', vert_137, 'vertex148', vert_148]
                    tri_246 = ['vertex148', vert_148, 'vertex149', vert_149, 'vertex150', vert_150]
                    #tri_247 = ['vertex127', vert_127, 'vertex129', vert_129, 'vertex149', vert_149]
                    tri_247 = ['vertex176', vert_176, 'vertex129', vert_129, 'vertex149', vert_149] #replace vertex127 by vertex_176 to address south pole issue
                    tri_248 = ['vertex130', vert_130, 'vertex134', vert_134, 'vertex150', vert_150]
                    #tri_249 = ['vertex124', vert_124, 'vertex127', vert_127, 'vertex150', vert_150]
                    tri_249 = ['vertex124', vert_124, 'vertex174', vert_174, 'vertex150', vert_150] #replace vertex127 by vertex_174 to address south pole issue
                    tri_250 = ['vertex032', vert_32, 'vertex124', vert_124, 'vertex130', vert_130]
                    tri_251 = ['vertex053', vert_53, 'vertex137', vert_137, 'vertex148', vert_148]
                    tri_252 = ['vertex061', vert_61, 'vertex148', vert_148, 'vertex149', vert_149]
                    tri_253 = ['vertex064', vert_64, 'vertex129', vert_129, 'vertex149', vert_149]
                    tri_254 = ['vertex0134', vert_134, 'vertex148', vert_148, 'vertex150', vert_150]
                    #tri_255 = ['vertex127', vert_127, 'vertex149', vert_149, 'vertex150', vert_150]
                    tri_255 = ['vertex175', vert_175, 'vertex149', vert_149, 'vertex150', vert_150] #replace vertex127 by vertex_175 to address south pole issue
                    tri_256 = ['vertex124', vert_124, 'vertex130', vert_130, 'vertex150', vert_150]
                    tri_257 = ['vertex067', vert_67, 'vertex068', vert_68, 'vertex146', vert_146]
                    tri_258 = ['vertex068', vert_68, 'vertex074', vert_74, 'vertex151', vert_151]
                    tri_259 = ['vertex074', vert_74, 'vertex076', vert_76, 'vertex152', vert_152]
                    tri_260 = ['vertex052', vert_52, 'vertex076', vert_76, 'vertex138', vert_138]
                    tri_261 = ['vertex143', vert_143, 'vertex146', vert_146, 'vertex151', vert_151]
                    tri_262 = ['vertex151', vert_151, 'vertex152', vert_152, 'vertex153', vert_153]
                    tri_263 = ['vertex136', vert_136, 'vertex138', vert_138, 'vertex152', vert_152]
                    tri_264 = ['vertex139', vert_139, 'vertex143', vert_143, 'vertex153', vert_153]
                    tri_265 = ['vertex133', vert_133, 'vertex136', vert_136, 'vertex153', vert_153]
                    tri_266 = ['vertex042', vert_42, 'vertex133', vert_133, 'vertex139', vert_139]
                    tri_267 = ['vertex068', vert_68, 'vertex146', vert_146, 'vertex151', vert_151]
                    tri_268 = ['vertex074', vert_74, 'vertex151', vert_151, 'vertex152', vert_152]
                    tri_269 = ['vertex076', vert_76, 'vertex138', vert_138, 'vertex152', vert_152]
                    tri_270 = ['vertex143', vert_143, 'vertex151', vert_151, 'vertex153', vert_153]
                    tri_271 = ['vertex136', vert_136, 'vertex152', vert_152, 'vertex153', vert_153]
                    tri_272 = ['vertex133', vert_133, 'vertex139', vert_139, 'vertex153', vert_153]
                    tri_273 = ['vertex077', vert_77, 'vertex078', vert_78, 'vertex110', vert_110]
                    tri_274 = ['vertex078', vert_78, 'vertex084', vert_84, 'vertex154', vert_154]
                    tri_275 = ['vertex084', vert_84, 'vertex086', vert_86, 'vertex155', vert_155]
                    tri_276 = ['vertex067', vert_67, 'vertex086', vert_86, 'vertex147', vert_147]
                    #tri_277 = ['vertex107', vert_107, 'vertex110', vert_110, 'vertex154', vert_154]
                    tri_277 = ['vertex167', vert_167, 'vertex110', vert_110, 'vertex154', vert_154] #replace vertex107 by vertex_167 to address north pole issue
                    tri_278 = ['vertex154', vert_154, 'vertex155', vert_155, 'vertex156', vert_156]
                    tri_279 = ['vertex145', vert_145, 'vertex147', vert_147, 'vertex155', vert_155]
                    #tri_280 = ['vertex103', vert_103, 'vertex107', vert_107, 'vertex156', vert_156]
                    tri_280 = ['vertex103', vert_103, 'vertex165', vert_165, 'vertex156', vert_156] #replace vertex107 by vertex_165 to address north pole issue
                    tri_281 = ['vertex142', vert_142, 'vertex145', vert_145, 'vertex156', vert_156]
                    tri_282 = ['vertex015', vert_15, 'vertex103', vert_103, 'vertex142', vert_142]
                    tri_283 = ['vertex078', vert_78, 'vertex110', vert_110, 'vertex154', vert_154]
                    tri_284 = ['vertex084', vert_84, 'vertex154', vert_154, 'vertex155', vert_155]
                    tri_285 = ['vertex086', vert_86, 'vertex147', vert_147, 'vertex155', vert_155]
                    #tri_286 = ['vertex107', vert_107, 'vertex154', vert_154, 'vertex156', vert_156]
                    tri_286 = ['vertex166', vert_166, 'vertex154', vert_154, 'vertex156', vert_156] #replace vertex107 by vertex_166 to address north pole issue
                    tri_287 = ['vertex145', vert_145, 'vertex155', vert_155, 'vertex156', vert_156]
                    tri_288 = ['vertex103', vert_103, 'vertex142', vert_142, 'vertex156', vert_156]
                    tri_289 = ['vertex087', vert_87, 'vertex088', vert_88, 'vertex119', vert_119]
                    tri_290 = ['vertex088', vert_88, 'vertex094', vert_94, 'vertex157', vert_157]
                    tri_291 = ['vertex094', vert_94, 'vertex096', vert_96, 'vertex158', vert_158]
                    tri_292 = ['vertex077', vert_77, 'vertex096', vert_96, 'vertex111', vert_111]
                    tri_293 = ['vertex116', vert_116, 'vertex119', vert_119, 'vertex157', vert_157]
                    tri_294 = ['vertex157', vert_157, 'vertex158', vert_158, 'vertex159', vert_159]
                    tri_295 = ['vertex109', vert_109, 'vertex111', vert_111, 'vertex158', vert_158]
                    tri_296 = ['vertex112', vert_112, 'vertex116', vert_116, 'vertex159', vert_159]
                    tri_297 = ['vertex106', vert_106, 'vertex109', vert_109, 'vertex159', vert_159]
                    tri_298 = ['vertex009', vert_9, 'vertex106', vert_106, 'vertex112', vert_112]
                    tri_299 = ['vertex088', vert_88, 'vertex119', vert_119, 'vertex157', vert_157]
                    tri_300 = ['vertex094', vert_94, 'vertex157', vert_157, 'vertex158', vert_158]
                    tri_301 = ['vertex096', vert_96, 'vertex111', vert_111, 'vertex158', vert_158]
                    tri_302 = ['vertex116', vert_116, 'vertex157', vert_157, 'vertex159', vert_159]
                    tri_303 = ['vertex109', vert_109, 'vertex158', vert_158, 'vertex159', vert_159]
                    tri_304 = ['vertex106', vert_106, 'vertex112', vert_112, 'vertex159', vert_159]
                    tri_305 = ['vertex066', vert_66, 'vertex097', vert_97, 'vertex128', vert_128]
                    tri_306 = ['vertex097', vert_97, 'vertex100', vert_100, 'vertex160', vert_160]
                    tri_307 = ['vertex100', vert_100, 'vertex102', vert_102, 'vertex161', vert_161]
                    tri_308 = ['vertex087', vert_87, 'vertex102', vert_102, 'vertex120', vert_120]
                    tri_309 = ['vertex125', vert_125, 'vertex128', vert_128, 'vertex160', vert_160]
                    tri_310 = ['vertex160', vert_160, 'vertex161', vert_161, 'vertex162', vert_162]
                    tri_311 = ['vertex118', vert_118, 'vertex120', vert_120, 'vertex161', vert_161]
                    tri_312 = ['vertex121', vert_121, 'vertex125', vert_125, 'vertex162', vert_162]
                    tri_313 = ['vertex115', vert_115, 'vertex118', vert_118, 'vertex162', vert_162]
                    tri_314 = ['vertex022', vert_22, 'vertex115', vert_115, 'vertex121', vert_121]
                    tri_315 = ['vertex097', vert_97, 'vertex128', vert_128, 'vertex160', vert_160]
                    tri_316 = ['vertex100', vert_100, 'vertex160', vert_160, 'vertex161', vert_161]
                    tri_317 = ['vertex102', vert_102, 'vertex120', vert_120, 'vertex161', vert_161]
                    tri_318 = ['vertex125', vert_125, 'vertex160', vert_160, 'vertex162', vert_162]
                    tri_319 = ['vertex118', vert_118, 'vertex161', vert_161, 'vertex162', vert_162]
                    tri_320 = ['vertex115', vert_115, 'vertex121', vert_121, 'vertex162', vert_162]                                                                            
                    # extra triangles to deal with north pole sampling issue
                    tri_321 = ['vertex163', vert_163, 'vertex169', vert_169, 'vertex108', vert_108]
                    tri_322 = ['vertex164', vert_164, 'vertex163', vert_163, 'vertex104', vert_104]
                    tri_323 = ['vertex165', vert_165, 'vertex164', vert_164, 'vertex103', vert_103]
                    tri_324 = ['vertex166', vert_166, 'vertex165', vert_165, 'vertex156', vert_156]
                    tri_325 = ['vertex167', vert_167, 'vertex166', vert_166, 'vertex154', vert_154]
                    tri_326 = ['vertex168', vert_168, 'vertex167', vert_167, 'vertex110', vert_110]
                    tri_327 = ['vertex170', vert_170, 'vertex168', vert_168, 'vertex171', vert_171]
                    # extra triangles to deal with south pole sampling issue
                    tri_328 = ['vertex172', vert_172, 'vertex126', vert_126, 'vertex178', vert_178]
                    tri_329 = ['vertex173', vert_173, 'vertex123', vert_123, 'vertex172', vert_172]
                    tri_330 = ['vertex174', vert_174, 'vertex124', vert_124, 'vertex173', vert_173]
                    tri_331 = ['vertex175', vert_175, 'vertex150', vert_150, 'vertex174', vert_174]
                    tri_332 = ['vertex176', vert_176, 'vertex149', vert_149, 'vertex175', vert_175]
                    tri_333 = ['vertex177', vert_177, 'vertex129', vert_129, 'vertex176', vert_176]
                    tri_334 = ['vertex179', vert_179, 'vertex180', vert_180, 'vertex177', vert_177]
                    
                    #print 'tri_1= ', tri_1
                    tri_grp = [tri_1, tri_2, tri_3, tri_4, tri_5, tri_6, tri_7, tri_8, tri_9, tri_10, tri_11, tri_12,
                               tri_13, tri_14, tri_15, tri_16, tri_17, tri_18, tri_19, tri_20, tri_21, tri_22, tri_23,
                               tri_24, tri_25, tri_26, tri_27, tri_28, tri_29, tri_30, tri_31, tri_32, tri_33, tri_34,
                               tri_35, tri_36, tri_37, tri_38, tri_39, tri_40, tri_41, tri_42, tri_43, tri_44, tri_45,
                               tri_46, tri_47, tri_48, tri_49, tri_50, tri_51, tri_52, tri_53, tri_54, tri_55, tri_56,
                               tri_57, tri_58, tri_59, tri_60, tri_61, tri_62, tri_63, tri_64, tri_65, tri_66, tri_67,
                               tri_68, tri_69, tri_70, tri_71, tri_72, tri_73, tri_74, tri_75, tri_76, tri_77, tri_78,
                               tri_79, tri_80, tri_81, tri_82, tri_83, tri_84, tri_85, tri_86, tri_87, tri_88, tri_89,
                               tri_90, tri_91, tri_92, tri_93, tri_94, tri_95, tri_96, tri_97, tri_98, tri_99, tri_100,
                               tri_101, tri_102, tri_103, tri_104, tri_105, tri_106, tri_107, tri_108, tri_109, tri_110,
                               tri_111, tri_112, tri_113, tri_114, tri_115, tri_116, tri_117, tri_118, tri_119, tri_120,
                               tri_121, tri_122, tri_123, tri_124, tri_125, tri_126, tri_127, tri_128, tri_129, tri_130,
                               tri_131, tri_132, tri_133, tri_134, tri_135, tri_136, tri_137, tri_138, tri_139, tri_140,
                               tri_141, tri_142, tri_143, tri_144, tri_145, tri_146, tri_147, tri_148, tri_149, tri_150,
                               tri_151, tri_152, tri_153, tri_154, tri_155, tri_156, tri_157, tri_158, tri_159, tri_160,
                               tri_161, tri_162, tri_163, tri_164, tri_165, tri_166, tri_167, tri_168, tri_169, tri_170,
                               tri_171, tri_172, tri_173, tri_174, tri_175, tri_176, tri_177, tri_178, tri_179, tri_180,
                               tri_181, tri_182, tri_183, tri_184, tri_185, tri_186, tri_187, tri_188, tri_189, tri_190,
                               tri_191, tri_192, tri_193, tri_194, tri_195, tri_196, tri_197, tri_198, tri_199, tri_200,
                               tri_201, tri_202, tri_203, tri_204, tri_205, tri_106, tri_107, tri_208, tri_209, tri_210,
                               tri_211, tri_212, tri_213, tri_214, tri_215, tri_216, tri_217, tri_218, tri_219, tri_220,
                               tri_221, tri_222, tri_223, tri_224, tri_225, tri_226, tri_227, tri_228, tri_229, tri_230,
                               tri_231, tri_232, tri_233, tri_234, tri_235, tri_236, tri_237, tri_238, tri_239, tri_240,
                               tri_241, tri_242, tri_243, tri_244, tri_245, tri_246, tri_247, tri_248, tri_249, tri_250,
                               tri_251, tri_252, tri_253, tri_254, tri_255, tri_256, tri_257, tri_258, tri_259, tri_260,
                               tri_261, tri_262, tri_263, tri_264, tri_265, tri_266, tri_267, tri_268, tri_269, tri_270,
                               tri_271, tri_272, tri_273, tri_274, tri_275, tri_276, tri_277, tri_278, tri_279, tri_280,
                               tri_281, tri_282, tri_283, tri_284, tri_285, tri_286, tri_287, tri_288, tri_289, tri_290,
                               tri_291, tri_292, tri_293, tri_294, tri_295, tri_296, tri_297, tri_298, tri_299, tri_300,
                               tri_301, tri_302, tri_303, tri_304, tri_305, tri_306, tri_307, tri_308, tri_309, tri_310,
                               tri_311, tri_312, tri_313, tri_314, tri_315, tri_316, tri_317, tri_318, tri_319, tri_320,                     
                               # extra triangles for dealing north pole sampling issue
                               tri_321, tri_322, tri_323, tri_324, tri_325, tri_326, tri_327,
                               # extra triangles for dealing south pole sampling issue
                               tri_328, tri_329, tri_330, tri_331, tri_332, tri_333, tri_334] 
                    #print 'tri_grp[0]= ', tri_grp[0]
                                                   
                    for i in range(334): # the number in the range() will be the total number of triangles
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
                        if j == 169:                         
                            ta = [vert_coord[1][0]+128.0, vert_coord[1][1]]    
                            tb = [vert_coord[3][0]+128.0, vert_coord[3][1]]
                            #p = [x,y]
                            #print 'pixels in LEFT portion','triangle %d' % j, 'x= ', p[0], 'y= ', p[1], 'ta[0]= ', ta[0]
                        if j == 176:                         
                            ta = [vert_coord[1][0]+128.0, vert_coord[1][1]]
                        if j == 184:                         
                            ta = [vert_coord[1][0]+128.0, vert_coord[1][1]]    
                            tb = [vert_coord[3][0]+128.0, vert_coord[3][1]]
                        if j == 185:                         
                            ta = [vert_coord[1][0]+128.0, vert_coord[1][1]]    
                            tb = [vert_coord[3][0]+128.0, vert_coord[3][1]]
                        if j == 192:                         
                            ta = [vert_coord[1][0]+128.0, vert_coord[1][1]]
                        if j == 200:                         
                            ta = [vert_coord[1][0]+128.0, vert_coord[1][1]]    
                            tb = [vert_coord[3][0]+128.0, vert_coord[3][1]]
                        if j == 208:                         
                            ta = [vert_coord[1][0]+128.0, vert_coord[1][1]]
                        if j == 293:                         
                            ta = [vert_coord[1][0]+128.0, vert_coord[1][1]]
                        if j == 294:                         
                            tc = [vert_coord[5][0]+128.0, vert_coord[5][1]]
                        if j == 295:                         
                            ta = [vert_coord[1][0]+128.0, vert_coord[1][1]]
                        if j == 302:                         
                            ta = [vert_coord[1][0]+128.0, vert_coord[1][1]]
                            tc = [vert_coord[5][0]+128.0, vert_coord[5][1]]
                        if j == 303:                         
                            ta = [vert_coord[1][0]+128.0, vert_coord[1][1]]
                            tc = [vert_coord[5][0]+128.0, vert_coord[5][1]]
                        if j == 309:                         
                            ta = [vert_coord[1][0]+128.0, vert_coord[1][1]]
                        if j == 310:                         
                            tc = [vert_coord[5][0]+128.0, vert_coord[5][1]]
                        if j == 311:                         
                            ta = [vert_coord[1][0]+128.0, vert_coord[1][1]]
                        if j == 318:                         
                            ta = [vert_coord[1][0]+128.0, vert_coord[1][1]]
                            tc = [vert_coord[5][0]+128.0, vert_coord[5][1]]
                        if j == 319:                         
                            ta = [vert_coord[1][0]+128.0, vert_coord[1][1]]
                            tc = [vert_coord[5][0]+128.0, vert_coord[5][1]]
                        
                        # sample code for dealing with problematic triangles
                        #if j == 58:
                        #    if x <= 64.0:   
                        #        ta = [vert_coord[1][0]-128.0, vert_coord[1][1]]
                        #    if x > 64.0:                                                      
                        #        tb = [vert_coord[3][0]+128.0, vert_coord[3][1]]
                        #        tc = [vert_coord[5][0]+128.0, vert_coord[5][1]]    
                        #        
                        #if j == 59:
                        #    tc = [vert_coord[5][0]+128.0, vert_coord[5][1]]
                                                                    
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
                            if triArea > 80.0:
                                print
                                print 'triangle across boundries'
                                print 'this is the pixel u= ', u+1, 'and v = ', v+1
                                print 'this is the %d triangle' % j
                                print side_ab, side_bc, side_ca
                                print 'triArea= ', triArea
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