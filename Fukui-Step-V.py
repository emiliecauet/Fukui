# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 11:10:00 2016

@author: ecauet
"""

FPID=["1384"]
directory = "/Users/ecauet/Documents/METASPACE/Fukui-Model/Molecules-Test/TESTS/"
Bondlimit = 2.8

import sys
import os
import os.path

"""
FUNCTION 1:
TO READ THE LINES AND DECOMPOSE THEM INTO DIFFERENT LISTS OF ATOMS< COORDINATES AND GRADIENTS
"""
def decomplines(grouplines):
    
    import re
    patternI=re.compile(r'[(a-zA-Z)]' )
    patternII=re.compile(r'([\-]{0,1}\d+\.\d+)[^-\d]' )
    
    Ntot=0
    list1=[]
    list2=[]
    list3=[]
    
    for line in grouplines:
        Ntot+=1
        atom=patternI.findall(line)

        list1.append(atom)
        array=patternII.findall(line)

        coord=array[0:3]
        coord = map(float, coord)
        list2.append(coord)

        gradient=array[3:7]
        gradient=map(float, gradient)
        list3.append(gradient)

    atom = []
    array = []
    coord = []
    gradient = []
    return Ntot, list1, list2, list3

"""
FUNCTION 2:
TO CALCULATE THE DIFFERENCES BETWEEN THE GRADIENT OF ATOMS OF LIST 2 AND LIST 1 (LIST2 - LIST1)
"""
def diffgradient(N, list1_atom, list2_atom, list1_coord, list2_coord, list1_gradient, list2_gradient):
    
    list_temp =[]
    list21_atom =[]
    list21_coord =[]
    list21_gradient =[]
    
    for i in range(0, N, 1):
        for j in range(0, N, 1):
        
            if list2_atom[i] == list1_atom[j] and (list2_coord[i][0]-list1_coord[j][0]) == 0 and (list2_coord[i][1]-list1_coord[j][1]) == 0 and (list2_coord[i][2]-list1_coord[j][2]) == 0:
              
              diffX = list2_gradient[i][0]-list1_gradient[j][0]
              list_temp.append(diffX)
              
              diffY = list2_gradient[i][1]-list1_gradient[j][1]
              list_temp.append(diffY)

              diffZ = list2_gradient[i][2]-list1_gradient[j][2]
              list_temp.append(diffZ)
              
              list21_atom.append(list2_atom[i])
              list21_coord.append(list2_coord[i])
              list21_gradient.append(list_temp)
              
              list_temp = []
              break
    
    return list21_atom, list21_coord, list21_gradient

"""
FUNCTION 3:
TO PROJECT THE FORCES ALONG THE CHEMICAL BONDS
"""
def project(N, limit, list_atom, list_coord, list_gradient):
    
    import math
    
    output_file = open("temp", "w+")
    
    num_proj=0
    list_final=[]
    list_final2=[]
    
    for i in range(0, N, 1):    
        Force=math.sqrt(math.pow(list_gradient[i][0],2)+math.pow(list_gradient[i][1],2)+math.pow(list_gradient[i][2],2))

        for j in range(0, N, 1):
            if j !=i:

                BondX=list_coord[j][0]-list_coord[i][0]
                BondY=list_coord[j][1]-list_coord[i][1]
                BondZ=list_coord[j][2]-list_coord[i][2]

                Bond=math.sqrt(math.pow(BondX,2)+math.pow(BondY,2)+math.pow(BondZ,2))

                if Bond <= limit:
                    num_proj+=1
                    ScalarProj=((list_gradient[i][0]*BondX)+(list_gradient[i][1]*BondY)+(list_gradient[i][2]*BondZ))/Bond
                    theta=(math.acos(ScalarProj/Force))*180.0/math.pi

                    ProjX=ScalarProj*(BondX/Bond)
                    ProjY=ScalarProj*(BondY/Bond)
                    ProjZ=ScalarProj*(BondZ/Bond)

                    list_final += [''.join(list_atom[i]), round(list_coord[i][0], 3), round(list_coord[i][1], 3), round(list_coord[i][2], 3)]
                    list_final += [round(ProjX, 3), round(ProjY, 3), round(ProjZ, 3)]

                    list_final2 += [i, list_atom[i], j, list_atom[j], round(list_coord[i][0], 3), round(list_coord[i][1], 3), round(list_coord[i][2], 3), round(Bond, 3), round(Force, 3)]
                    list_final2 += [round(ScalarProj, 3), round(theta, 3), round(ProjX, 3), round(ProjY, 3), round(ProjZ, 3)]

                    if  theta >= 90:
                        list_final2 += ['Bond ELONGATION']

                    list_final='   '.join([str(item) for item in list_final])
                    list_final2=",  ".join( repr(e) for e in list_final2 )
                    
                    print>>output_file, list_final
                    list_final =[]
                    list_final2 =[]
                    
                else:
                    j += 1
    i=0
    j=0
    
    return num_proj, list_final, list_final2, output_file

"""

ACID PART

"""

for FP in FPID:

    myfolder = directory+"FPID_"+FP+"/Forces/GRADIENT_NA/"
    print myfolder
    if not os.path.isdir(myfolder):
        print 'NO OUTPUT FILE - SKIPPING THIS FPID'
        continue
        
    for f in os.listdir(myfolder):
        if f.endswith("A.inp") or f.endswith("A1.inp") or f.endswith("A2.inp"):
            print "Filename: ", f
            #print "output_",str(f)[-7:-4]
            myfile= open(os.path.join(myfolder+f), "r")
            outputAN2_file = open(os.path.join(myfolder+"output_"+str(f)[-7:-4]), "w")
            
            lines = myfile.readlines()
            lines = filter(lambda x: not x.isspace(), lines)

            num_lines = sum(1 for line in lines)
            N=(num_lines-1)/2

            Neutrallines = lines[0:N]
            Acidlines = lines [N:2*N+1]

            ### Decomposition of the lines - Function decomplines ###

            NtotatomN, listN_atom, listN_coord, listN_gradient = decomplines(Neutrallines)
            NtotatomA, listA_atom, listA_coord, listA_gradient = decomplines(Acidlines)

            ### Calculating the differences of the forces - Function diffgradient ###

            listAN_atom, listAN_coord, listAN_gradient = diffgradient(NtotatomN, listN_atom, listA_atom, listN_coord, listA_coord, listN_gradient, listA_gradient)

            ### Add the non-matches between Neutral and Acid lists ###

            non_matches= len(listA_coord)-len(listAN_atom)
            tuple_list1 = [tuple(lst) for lst in listAN_coord]
            tuple_list2 = [tuple(lst) for lst in listA_coord]
            first_set = set(tuple_list1)
            second_set = set(tuple_list2)
            diff_set = first_set.symmetric_difference(second_set)
            list_diff = list(diff_set)

            if len(diff_set) == non_matches:
                for i in range(0, len(diff_set), 1):
                    index=tuple_list2.index(list_diff[i])

                    listAN_atom.append(listA_atom[index])
                    listAN_coord.append(listA_coord[index])
                    listAN_gradient.append(listA_gradient[index])
                    index=0    
            else:
                pass

            NtotatomAN=len(listAN_atom)
            if NtotatomAN == (NtotatomN+1):
                print "Number of atoms is OK."
            else:
                print "Check the Number of atoms."

            i=0
            j=0

            ### Project the forces on the chemical bonds ###
            nproj, listAN_final, listAN_final2, outputAN_file = project(NtotatomAN, Bondlimit, listAN_atom, listAN_coord, listAN_gradient)

            outputAN_file.seek(0)

            print>>outputAN2_file, nproj, "\n"

            for line in outputAN_file.readlines():
                outputAN2_file.write(line)

            nproj=0
            outputAN_file.close()
            outputAN2_file.close()
            
"""

BASIC PART

"""

for FP in FPID:
    myfolder = directory+"FPID_"+FP+"/Forces/GRADIENT_NB/"
    print myfolder
    if not os.path.isdir(myfolder):
        print 'NO OUTPUT FILE - SKIPPING THIS FPID'
        continue
        
    for f in os.listdir(myfolder):
        if f.endswith("B.inp") or f.endswith("B1.inp") or f.endswith("B2.inp"):
            print "Filename: ", f
            #print "output_",str(f)[-7:-4]
            myfile= open(os.path.join(myfolder+f), "r")
            outputBN2_file = open(os.path.join(myfolder+"output_"+str(f)[-7:-4]), "w")
            
            lines = myfile.readlines()
            lines = filter(lambda x: not x.isspace(), lines)

            num_lines = sum(1 for line in lines)
            N=(num_lines+1)/2

            Neutrallines = lines[0:N]
            Basiclines = lines [N:2*N-1]

            ### Decomposition of the lines - Function decomplines ###

            NtotatomN, listN_atom, listN_coord, listN_gradient = decomplines(Neutrallines)
            NtotatomB, listB_atom, listB_coord, listB_gradient = decomplines(Basiclines)

            ### Calculating the differences of the forces - Function diffgradient ###

            listBN_atom, listBN_coord, listBN_gradient = diffgradient(NtotatomB, listN_atom, listB_atom, listN_coord, listB_coord, listN_gradient, listB_gradient)

            ### Add the non-matches between Neutral and Basic lists ###

            #non_matches= len(listB_coord)-len(listBN_atom)
            tuple_list1 = [tuple(lst) for lst in listBN_coord]
            tuple_list2 = [tuple(lst) for lst in listN_coord]
            first_set = set(tuple_list1)
            second_set = set(tuple_list2)
            diff_set = first_set.symmetric_difference(second_set)
            list_diff = list(diff_set)
            
            print len(diff_set)
            
            for i in range(0, len(diff_set), 1):
                index=tuple_list2.index(list_diff[i])
                if listN_atom[index] == ['H']:
                    print "One H has been (re)moved"
                else:
                    print "A heavy atom has been moved"
                        
                listBN_atom.append(listN_atom[index])
                listBN_coord.append(listN_coord[index])
                listBN_gradient.append(listN_gradient[index])    
                index=0 

            NtotatomBN=len(listBN_atom)
            if NtotatomBN == (NtotatomN):
                print "Number of atoms is OK."
            else:
                print "Check the Number of atoms."


            i=0
            j=0

            ### Project the forces on the chemical bonds ###
            nproj, listBN_final, listBN_final2, outputBN_file = project(NtotatomBN, Bondlimit, listBN_atom, listBN_coord, listBN_gradient)

            outputBN_file.seek(0)

            print>>outputBN2_file, nproj, "\n"

            for line in outputBN_file.readlines():
                outputBN2_file.write(line)

            nproj=0
            outputBN_file.close()
            outputBN2_file.close()