# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 11:10:00 2016

@author: ecauet
"""
FPID=["1384"]
#FPID=["1384", "1386", "1387", "1388", "1389", "1392", "1393", "1396", "1400", "12", "1405", "9629", "9631", "9634", "9635", "2006", "9643", "9645", "9646", "9656", "9670", "9678", "5727", "9702", "9705", "9708", "9710", "9711", "9144", "9712", "9714", "9912", "9913", "9914", "9915", "9916", "9930", "9932", "9933", "9935", "9942", "9944", "9945", "9964", "9965", "9966", "9967", "9969", "9973", "9996", "10016"]
directory = "/Users/ecauet/Documents/METASPACE/Fukui-Model/Molecules-Test/"

#Factor = 0.52918

import sys
import os
import os.path
import copy
import Fragmenter_V4 as fg

"""
FUNCTION :
TO CLEAN THE DIRECTORY
"""
def deletefiles(directory):
    filelist = [f for f in os.listdir(directory) if f.endswith("NA")]
    for f in filelist:
        os.remove(directory+f)
    return

"""
FUNCTION 0:
TO GENERATE A LIST WITH THE WEIGHT OF EACH ATOM
"""
def weight(N, list_atom):
    
    list_weight = []
    
    for i in range(0, N, 1):
        if list_atom[i] == ['C']:
            list_weight.append(12.0000000000000)
        elif list_atom[i] == ['H']:
            list_weight.append(1.0078250322390)
        elif list_atom[i] == ['N']:
            list_weight.append(14.0030740044320)
        elif list_atom[i] == ['O']:
            list_weight.append(15.9949146195717)
        elif list_atom[i] == ['P']:
            list_weight.append(30.9737619984270)
        elif list_atom[i] == ['F']:
            list_weight.append(18.9984031627392)
        elif list_atom[i] == ['Mg']:
            list_weight.append(23.9850416971400)
        elif list_atom[i] == ['Na']:
            list_weight.append(22.9897692820190)
        elif list_atom[i] == ['S']:
            list_weight.append(31.9720711744140)
        elif list_atom[i] == ['Cl']:
            list_weight.append(34.9688526823700)
   
    return list_weight

def isotope(N, list_atom):
    
    list_isotope = []
    
    for i in range(0, N, 1):
        list_isotope.append(int(0))

    return list_isotope


def charge(N, list_atom):
    
    list_charge = []
    
    for i in range(0, N, 1):
        list_charge.append(int(0))

    return list_charge


def atomaticity(N, list_atom):
    
    list_atomaticity = []
    
    for i in range(0, N, 1):
        list_atomaticity.append(int(0))

    return list_atomaticity

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
#        coord = [x*Factor for x in coord]
        list2.append(coord)

        gradient=array[3:7]
        gradient=map(float, gradient)
#        gradient = [y*Factor for y in gradient]
        list3.append(gradient)

    atom = []
    array = []
    coord = []
    gradient = []
    return Ntot, list1, list2, list3

"""
FUNCTION 2:
TO CALCULATE THE DIFFERENCES BETWEEN THE GRADIENT OF ATOMS OF LIST 2 AND LIST 1 (LIST2 - LIST1)
    Neutral = 1 - Acid/Base = 2
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
TO ADD THE NON-MATCHES BETWEEN TWO LISTS (LIST1 AND LIST2)
AN = 1 = A = 2
"""
def nonmatches(list1_atom, list2_atom, list1_coord, list2_coord, list1_gradient, list2_gradient):
    
    non_matches= len(list2_coord)-len(list1_atom)
    tuple_list1 = [tuple(lst) for lst in list1_coord]
    tuple_list2 = [tuple(lst) for lst in list2_coord]
    first_set = set(tuple_list1)
    second_set = set(tuple_list2)
    diff_set = first_set.symmetric_difference(second_set)
    list_diff = list(diff_set)
    
    if len(diff_set) == non_matches:
        for i in range(0, len(diff_set), 1):
            index=tuple_list2.index(list_diff[i])
    
            list1_atom.append(list2_atom[index])
            list1_coord.append(list2_coord[index])
            list1_gradient.append(list2_gradient[index])
            index=0    
    else:
        pass
    
    i=0

    return 

"""
FUNCTION 4:
TO PROJECT THE FORCES ALONG THE CHEMICAL BONDS
"""
def project(N, list_atom, list_coord, list_gradient, list_bonds):
    
    import math
        
    list_force=[]
    list_proj=[]
    list_final=[]
    list_final2=[]

    list_indexat1 = []
    list_indexat2 = []
    for a in range (0, len(list_bonds), 1):
        list_indexat1.append(list_bonds[a][0])
        list_indexat2.append(list_bonds[a][1])
    a=0
    
    for i in range(0, N, 1):
        # the force is still the difference between protonated and neutral species
        Force=math.sqrt(math.pow(list_gradient[i][0],2)+math.pow(list_gradient[i][1],2)+math.pow(list_gradient[i][2],2))
        Force=float(Force)
        list_force.append(Force)
    i=0
      
        
    for j in range(0, len(list_bonds), 1):
        
            BondX=list_coord[list_indexat2[j]][0]-list_coord[list_indexat1[j]][0]
            BondY=list_coord[list_indexat2[j]][1]-list_coord[list_indexat1[j]][1]
            BondZ=list_coord[list_indexat2[j]][2]-list_coord[list_indexat1[j]][2]

            Bond=math.sqrt(math.pow(BondX,2)+math.pow(BondY,2)+math.pow(BondZ,2))
            
            ScalarProj=((list_gradient[list_indexat1[j]][0]*BondX)+(list_gradient[list_indexat1[j]][1]*BondY)+(list_gradient[list_indexat1[j]][2]*BondZ))/Bond
            theta=(math.acos(ScalarProj/list_force[list_indexat1[j]]))*180.0/math.pi

            ProjX=ScalarProj*(BondX/Bond)
            ProjY=ScalarProj*(BondY/Bond)
            ProjZ=ScalarProj*(BondZ/Bond)

            tmplst=[]
            tmplst = [list_atom[list_indexat1[j]][0], list_coord[list_indexat1[j]][0], list_coord[list_indexat1[j]][1], list_coord[list_indexat1[j]][2], '{:.5f}'.format(ProjX), '{:.5f}'.format(ProjY), '{:.5f}'.format(ProjZ)]
            tmplst='   '.join([str(item) for item in tmplst])                                       
            list_final.append(tmplst)                                          

            tmplst2=[]                    
            tmplst2 = [list_indexat1[j], list_indexat2[j], list_atom[list_indexat1[j]][0],list_atom[list_indexat2[j]][0], list_coord[list_indexat1[j]][0], list_coord[list_indexat1[j]][1], list_coord[list_indexat1[j]][2], list_force[list_indexat1[j]], ScalarProj, theta, '{:.5f}'.format(ProjX), '{:.5f}'.format(ProjY), '{:.5f}'.format(ProjZ)]

            
            if  theta >= 90:
                tmplst2 += ['Bond ELONGATION']
            
            list_final2.append(tmplst2)

            
            tmplst2bis=[]
            tmplst2bis = [list_indexat1[j], list_indexat2[j],list_atom[list_indexat1[j]][0],list_atom[list_indexat2[j]][0],ProjX,ProjY,ProjZ]
            list_proj.append(tmplst2bis)
            
    j=0
    

    return list_indexat1, list_indexat2, list_force, list_final, list_final2, list_proj

"""
FUNCTION 5:
TO EVALUATE THE FORCES PER BOND - EITHER PROJECTED FORCES OR TOTAL FORCES
"""
def bondforce(num_bonds, list_final2):
    
    import math
    
    list_forcebonds=[]   

    for i in range(0, num_bonds, 1):
        for j in range(0, num_bonds, 1):
            if list_final2[i][0] == list_final2[j][1] and list_final2[i][1] == list_final2[j][0]:

                Fb=math.sqrt(math.pow(list_final2[i][7],2)+math.pow(list_final2[j][7],2))
                
                temp=[]
                temp = [list_final2[i][0], list_final2[i][1], Fb]
                list_forcebonds.append(temp)
                
    return list_forcebonds

    
def bondprojforce(num_bonds, list_proj):
    
    import math
    
    list_projforcebonds=[]   

    for i in range(0, num_bonds, 1):
        for j in range(0, num_bonds, 1):
            if list_proj[i][0] == list_proj[j][1] and list_proj[i][1] == list_proj[j][0]:

                FpbX=list_proj[i][4]+list_proj[j][4]
                FpbY=list_proj[i][5]+list_proj[j][5]
                FpbZ=list_proj[i][6]+list_proj[j][6]
                Fpb=math.sqrt(math.pow(FpbX,2)+math.pow(FpbY,2)+math.pow(FpbZ,2))
                
                temp=[]
                temp = [list_proj[i][0], list_proj[i][1], Fpb]
                list_projforcebonds.append(temp)
                
    return list_projforcebonds
                    
"""

ACID PART

"""

for FP in FPID:

    myfolder = directory+"FPID_"+FP+"/Forces/GRADIENT_NA/"
    #myfolder = directory+"Forces/GRADIENT_NA/TEST_FORCE"
    print myfolder
    deletefiles(myfolder)
    if not os.path.isdir(myfolder):
        print 'NO OUTPUT FILE - SKIPPING THIS FPID'
        continue
        
    for f in os.listdir(myfolder):
        if f.endswith("NA.inp"):
        #if f.endswith("NA.inp") or f.endswith("NA1.inp") or f.endswith("NA2.inp"):
            print "Filename: ", f
            #print "output_",str(f)[-7:-4]
            myfile= open(os.path.join(myfolder+f), "r")
            outputAN_file = open(os.path.join(myfolder+"output_"+FP+str(f)[-7:-4]), "w")
            scalar_file = open(os.path.join(myfolder+"scalar_"+FP+str(f)[-7:-4]), "w")
            proj_file = open(os.path.join(myfolder+"proj_"+FP+str(f)[-7:-4]), "w")
            vector_file = open(os.path.join(myfolder+"vector_"+FP+str(f)[-7:-4]), "w")
            frag_file = open(os.path.join(myfolder+"frag_"+FP+str(f)[-7:-4]), "w")
            outfrag_force = open(os.path.join(myfolder+"frag_outF_"+FP+str(f)[-7:-4]), "w")
            outfrag_proj = open(os.path.join(myfolder+"frag_outP_"+FP+str(f)[-7:-4]), "w")
            
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
        
            
            ### Add the non-matches between Neutral and Acid lists - Function nonmatches ###
            
            nonmatches(listAN_atom, listA_atom, listAN_coord, listA_coord, listAN_gradient, listA_gradient)
            
            NtotatomAN=len(listAN_atom)
            if NtotatomAN == (NtotatomN+1):
                print "Number of atoms is OK."
            else:
                print "Check the Number of atoms."
            
            ### Generate Bonds based on atoms and atomsXYZ - Function PredictBondsFromXYZ (Fragmenter) ###
            
            listAN_weight = weight(NtotatomAN, listAN_atom)
            listAN_isotope = isotope(NtotatomAN, listAN_atom)
            listAN_charge = charge(NtotatomAN, listAN_atom)
            listAN_atomaticity = atomaticity(NtotatomAN, listAN_atom)

            AN_atoms=[]
            for l in range(0, NtotatomAN, 1):
                tmplst5=[]
                tmplst5 = [listAN_weight[l],str(listAN_atom[l][0]),listAN_isotope[l],listAN_charge[l],listAN_atomaticity[l]]
                AN_atoms.append(tmplst5)
            l=0
            
            AN_atomsXYZ=[]        
            AN_atomsXYZ = copy.deepcopy(listAN_coord)
            
            for i in range(0,len(AN_atomsXYZ)):
                AN_atomsXYZ[i][0]=AN_atomsXYZ[i][0]/1.889725989;
                AN_atomsXYZ[i][1]=AN_atomsXYZ[i][1]/1.889725989;
                AN_atomsXYZ[i][2]=AN_atomsXYZ[i][2]/1.889725989;
                
            AN_bonds = fg.PredictBondsFromXYZ(AN_atoms,AN_atomsXYZ)
            AN_bonds=fg.GetUniqueBonds(AN_bonds)
            Nbonds=len(AN_bonds)
            
            ### Project the forces on the chemical bonds - Function Project ###
            
            listAN_indexat1, listAN_indexat2, listAN_force, listAN_final, listAN_final2, listAN_proj = project(NtotatomAN, listAN_atom, listAN_coord, listAN_gradient, AN_bonds)
            
            print listAN_indexat1
            print listAN_indexat2
            
            ### Evaluate the forces per bond - Function BondForce and BondprojForce ####
            listAN_forcebonds = bondforce(Nbonds, listAN_final2)
            listAN_projforcebonds = bondprojforce(Nbonds, listAN_proj)             
            
            print listAN_forcebonds
            print listAN_projforcebonds
            
            ############# Start printing what we need ##################
    
            ### 1 - Summary File ###          
            outputAN_file.seek(0)
            listAN_final2='\n'.join([str(item) for item in listAN_final2])
            print>>outputAN_file, listAN_final2
            
            ### 2 - Projection File ### 
            proj_file.seek(0)            
            listAN_final='\n'.join([str(item) for item in listAN_final])            
            print>>proj_file, Nbonds, "\n"
            print>>proj_file, listAN_final
            
            ### 3 - Force Scalar File ###
            scalar_file.seek(0)
            listAN_final3=[]
            for l in range(0, NtotatomAN, 1):
                tmplst3=[]
                tmplst3 = [listAN_atom[l][0], listAN_coord[l][0], listAN_coord[l][1], listAN_coord[l][2], listAN_force[l]]
                tmplst3='   '.join([str(item) for item in tmplst3])                                       
                listAN_final3.append(tmplst3)
            l=0
             
            listAN_final3='\n'.join([str(item) for item in listAN_final3])
            print>>scalar_file, NtotatomAN, "\n"
            print>>scalar_file, listAN_final3
            
            ### 4 - Force Vector File ###
            vector_file.seek(0)
            listAN_final4=[]
            for k in range(0, NtotatomAN, 1):
                tmplst4=[]
                tmplst4 = [listAN_atom[k][0], listAN_coord[k][0], listAN_coord[k][1], listAN_coord[k][2], '{:.2f}'.format(listAN_gradient[k][0]), '{:.2f}'.format(listAN_gradient[k][1]), '{:.2f}'.format(listAN_gradient[k][2])]
                tmplst4='   '.join([str(item) for item in tmplst4])                                       
                listAN_final4.append(tmplst4)
            k=0
            
            listAN_final4='\n'.join([str(item) for item in listAN_final4])  
            print>>vector_file, NtotatomAN, "\n"
            print>>vector_file, listAN_final4
    
            ### 5 - Fragmenter File ###
            frag_file.seek(0)
    
            # Bonds #
            
            listAN_typebonds = []            
            for m in range(0, len(AN_bonds), 1):
                if listAN_atom[listAN_indexat1[m]] == ['H'] or listAN_atom[listAN_indexat2[m]] == ['H']:
                    listAN_typebonds.append(int(1))
                elif listAN_atom[listAN_indexat1[m]] == ['C'] or listAN_atom[listAN_indexat2[m]] == ['C']:
                    listAN_typebonds.append(int(1))
                elif listAN_atom[listAN_indexat1[m]] == ['N'] or listAN_atom[listAN_indexat2[m]] == ['N']:
                    listAN_typebonds.append(int(1))
            m=0       
            
            
            # Bonds 2 - Forces on the Bonds #
    
            listAN_final8=[]
            for o in range(0, len(listAN_forcebonds), 1):
                tmplst8=[]
                tmplst8=[listAN_forcebonds[o][0],listAN_forcebonds[o][1],listAN_typebonds[o], listAN_forcebonds[o][2]]
                listAN_final8.append(tmplst8)
            o=0
            
            listAN_final8=fg.GetUniqueBonds(listAN_final8)
            
            # Bonds 3 - Projected Forces on the bonds #
            
            listAN_final9=[]
            for o in range(0, len(listAN_projforcebonds), 1):
                tmplst9=[]
                tmplst9=[listAN_projforcebonds[o][0],listAN_projforcebonds[o][1],listAN_typebonds[o], listAN_projforcebonds[o][2]]
                listAN_final9.append(tmplst9)
            o=0
            
            listAN_final9=fg.GetUniqueBonds(listAN_final9)
            
    
            print>>frag_file, AN_atoms, "\n"
            print>>frag_file, listAN_final8, "\n"
            print>>frag_file, listAN_final9, "\n"
            print>>frag_file, AN_atomsXYZ, "\n"
            
            outputAN_file.close()
            proj_file.close()            
            scalar_file.close() 
            vector_file.close()
            frag_file.close()
           
            ### FRAGMENTER _ IVAN ###
    """
            AN_bonds=listAN_final8
            AN_projbonds=listAN_final9
            AN_newbonds=fg.GetUniqueBonds(AN_bonds)
            AN_newprojbonds=fg.GetUniqueBonds(AN_projbonds)
            
            frag1 = fg.FragmenterBasic(AN_atoms, AN_newbonds, AN_atomsXYZ, breakage_threshold=0.8, breakage_threshold_absolute=False, fragmentation_depth=2, Group_Atom_Numbers=False)
            frag1.SortResults(Ascending=False);
            print(frag1.Fragments)
            print>>outfrag_force, (frag1.Fragments), "\n"
    
            frag2 = fg.FragmenterBasic(AN_atoms, AN_newprojbonds, AN_atomsXYZ, breakage_threshold=0.8, breakage_threshold_absolute=False, fragmentation_depth=2, Group_Atom_Numbers=False)
            frag2.SortResults(Ascending=False);
            print(frag2.Fragments)
            print>>outfrag_proj, (frag2.Fragments), "\n"
            
            outfrag_force.close()
            outfrag_proj.close()
        
"""
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