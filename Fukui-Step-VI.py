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
import math

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
            outputAN_noproj = open(os.path.join(myfolder+"output_noproj"), "w")
            outputAN_force = open(os.path.join(myfolder+"output_force"), "w")
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

            print listAN_atom
            print listAN_coord
            print listAN_gradient
            
            
            ### Generate a list with the weight of each atoms ###
            listAN_weight = []
            
            for i in range(0, NtotatomAN, 1):
                if listAN_atom[i] == ['C']:
                    listAN_weight.append(12.0000000000000)
                elif listAN_atom[i] == ['H']:
                    listAN_weight.append(1.0078250322390)
                elif listAN_atom[i] == ['N']:
                    listAN_weight.append(14.0030740044320)
                elif listAN_atom[i] == ['O']:
                    listAN_weight.append(15.9949146195717)
                elif listAN_atom[i] == ['P']:
                    listAN_weight.append(30.9737619984270)
                elif listAN_atom[i] == ['F']:
                    listAN_weight.append(18.9984031627392)
                elif listAN_atom[i] == ['Mg']:
                    listAN_weight.append(23.9850416971400)
                elif listAN_atom[i] == ['Na']:
                    listAN_weight.append(22.9897692820190)
                    
            print listAN_weight   
            i=0
            
            ### Generate a list with the scalar forces for each atom (the force is still the difference between protonated and neutral species) ###
            listAN_force = []
            listAN_final3=[]
            
            for i in range(0, NtotatomAN, 1):    
                Force=math.sqrt(math.pow(listAN_gradient[i][0],2)+math.pow(listAN_gradient[i][1],2)+math.pow(listAN_gradient[i][2],2))
                listAN_force.append(Force)
                
                listAN_final3 += [listAN_atom[i], round(listAN_coord[i][0], 3), round(listAN_coord[i][1], 3), round(listAN_coord[i][2], 3), listAN_force[i]]
                listAN_final3='   '.join([str(item) for item in listAN_final3])
                
                print>>outputAN_force, listAN_final3                
                listAN_final3=[]
                
            print listAN_force
            print listAN_final3
            
            i=0
            
            
            
            ### Generate a list with the bonds for each atom - based on the distance for now ###
            listAN_bonds = []
            list_temp = []
            
            for i in range(0, NtotatomAN, 1):             
                for j in range(0, NtotatomAN, 1):
                    if j !=i:
                        BondX=listAN_coord[j][0]-listAN_coord[i][0]
                        BondY=listAN_coord[j][1]-listAN_coord[i][1]
                        BondZ=listAN_coord[j][2]-listAN_coord[i][2]

                        Bond=math.sqrt(math.pow(BondX,2)+math.pow(BondY,2)+math.pow(BondZ,2))
                    
                        if Bond <= Bondlimit:
                            list_temp.append(i)
                            list_temp.append(j)
                            
                            listAN_bonds.append(list_temp)
                            list_temp=[]
                j=0
            i=0
                        
            print listAN_bonds
            
            print>>outputAN_noproj, listAN_weight, "\n \n"
            print>>outputAN_noproj, listAN_force, "\n \n"
            print>>outputAN_noproj, listAN_bonds, "\n \n"
            
            ### Project the forces on the chemical bonds ###
            #nproj, listAN_final, listAN_final2, outputAN_file = project(NtotatomAN, Bondlimit, listAN_atom, listAN_coord, listAN_gradient)

            #outputAN_file.seek(0)

            #print>>outputAN2_file, nproj, "\n"

            #for line in outputAN_file.readlines():
            #    outputAN2_file.write(line)

            #nproj=0
            #outputAN_file.close()
            #outputAN2_file.close()
            
"""

BASIC PART


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
"""