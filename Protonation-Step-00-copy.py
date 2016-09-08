
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
def decomplinesXYZ(grouplines):
    
    import re
    patternI=re.compile(r'[(a-zA-Z)]' )
    patternII=re.compile(r'([\-]{0,1}\d+\.\d+)[^-\d]' )
    
    Ntot=0
    list1=[]
    list2=[]
    
    for line in grouplines:
        Ntot+=1
        atom=patternI.findall(line)

        list1.append(atom)
        array=patternII.findall(line)

        coord=array[0:3]
        coord = map(float, coord)
#        coord = [x*Factor for x in coord]
        list2.append(coord)

    atom = []
    array = []
    coord = []
    return Ntot, list1, list2

import os
import copy
import Fragmenter_V4 as fg
   
directory = "/Users/ecauet/Documents/METASPACE/Fukui-Model/Molecules-Test/TESTS/FPID_1384/"
myfolder = directory

for file in os.listdir(myfolder):
    if file.endswith(".xyz") and file.startswith("elbow"):
        myfile= open(myfolder + file, "r")
        mystring=file[6:13]
        myfilename="/optMP3_" + mystring
        out_file = open(myfolder + myfilename, "w")

        lines = myfile.readlines()
        Natom=lines[0]
        Natom = int(Natom)

        out_file.writelines(lines[len(lines)-Natom:len(lines)])
        
        myfile.close()
        out_file.close()
        
        out_file = open(myfolder + myfilename, "r")
        linesN = out_file.readlines()
        
        NtotatomN, listN_atom, listN_coord = decomplinesXYZ(linesN)
        
        print NtotatomN
        print listN_atom
        print listN_coord
        out_file.close()
        
    ### Generate Bonds based on atoms and atomsXYZ - Function PredictBondsFromXYZ (Fragmenter) ###
    
        listN_weight = weight(NtotatomN, listN_atom)
        listN_isotope = isotope(NtotatomN, listN_atom)
        listN_charge = charge(NtotatomN, listN_atom)
        listN_atomaticity = atomaticity(NtotatomN, listN_atom)
        
        N_atoms=[]
        for l in range(0, NtotatomN, 1):
            tmplst5=[]
            tmplst5 = [listN_weight[l],str(listN_atom[l][0]),listN_isotope[l],listN_charge[l],listN_atomaticity[l]]
            N_atoms.append(tmplst5)
        l=0
        
        N_atomsXYZ=[]        
        N_atomsXYZ = copy.deepcopy(listN_coord)
        
        for i in range(0,len(N_atomsXYZ)):
            N_atomsXYZ[i][0]=N_atomsXYZ[i][0]/1.889725989;
            N_atomsXYZ[i][1]=N_atomsXYZ[i][1]/1.889725989;
            N_atomsXYZ[i][2]=N_atomsXYZ[i][2]/1.889725989;
        
        print 'listN_coord: ', listN_coord
        print 'N_atomsXYZ: ', N_atomsXYZ
        
        N_bonds = fg.PredictBondsFromXYZ(N_atoms,N_atomsXYZ)
        N_bonds=fg.GetUniqueBonds(N_bonds)
        Nbonds=len(N_bonds)
        print 'N_bonds: ', N_bonds