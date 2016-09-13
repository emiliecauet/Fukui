# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 11:03:41 2016

@author: ecauet
"""

SMILES=["Oc(c([C@H](O5)[C@@H]([C@H]([C@@H]([C@H]5CO)O)O)O)1)c([C@H](O4)[C@@H]([C@@H](O)[C@@H](O)C4)O)c(c(C2=O)c1OC(c(c3)ccc(O)c3)=C2)O", "c(c5)(O)cc(c(c51)C(C(O[C@H](O3)[C@@H]([C@H]([C@@H]([C@H]3CO[C@@H]([C@@H]4O)O[C@H]([C@@H]([C@H]4O)O)C)O)O)O)=C(c(c2)ccc(O)c2)O1)=O)O", "COc(c1)c(O)c(OC)cc1C(=C2)Oc(c3)c(c(O)cc(O)3)C(=O)2", "OC[C@H]([C@@H](O)4)O[C@H]([C@H](O)[C@@H](O)4)c(c(O)1)c(O)c(C(=O)3)c(OC(=C3)c(c2)ccc(O)c2)c1", "Oc(c4)ccc(c4)C(O1)=C(OC(O3)C(O)C(O)C(O)C(C)3)C(=O)c(c(O)2)c(cc(O)c2)1", "CCCCCCC(=O)CCCCCCC=CCC(O)C(O)C(N)(CO)C(O)=O", "CCCCCCC(=O)C=CCCCCC=CC[C@@H](O)[C@H](O)[C@@](N)(CO)C(O)=O", "C1C(OC2=CC(=CC(=C2C1=O)O)O)C3=CC=C(C=C3)O", "C1=CC(=CC=C1C=CC(=O)C2=C(C=C(C=C2O)O)O)O", "C1=CC(=CC=C1C2=C(C(=O)C3=C(C=C(C=C3O2)O)O)O)O", "C1=CC(=C(C=C1C2=C(C(=O)C3=C(C=C(C=C3O2)O)O)O)O)O", "COC1=CC=C(C=C1)C2=COC3=CC(=CC(=C3C2=O)O)O", "CC(C(C(=O)O)N)O", "C1=CC(=CC=C1CC(C(=O)O)N)O", "C1=CC=C2C(=C1)C(=CN2)CC(C(=O)O)N", "C1=C(NC=N1)CC(C(=O)O)N", "C(C(C(=O)O)N)C(=O)O", "C(CC(=O)O)C(C(=O)O)N", "C(CC(=O)N)C(C(=O)O)N", "C1=COC(=C1)CNC2=NC=NC3=C2NC=N3", "C1=CC(=CC=C1C=CC2=CC(=CC(=C2)O)O)O", "C1=CC(=CC=C1CCC(=O)C2=C(C=C(C=C2O)O)O)O", "C1=CC(=C(C=C1C2=CC(=O)C3=C(C=C(C=C3O2)O)O)O)O", "CC1C(C(C(C(O1)OC2C(C(C(OC2OC3=CC(=C4C(=O)CC(OC4=C3)C5=CC=C(C=C5)O)O)CO)O)O)O)O)O", "C1=CC(=CC=C1C2=COC3=C(C2=O)C=CC(=C3)O)O", "C1C(C(OC2=CC(=CC(=C21)O)O)C3=CC(=C(C=C3)O)O)O", "CC1C(C(C(C(O1)OCC2C(C(C(C(O2)OC3=C(OC4=CC(=CC(=C4C3=O)O)O)C5=CC(=C(C=C5)O)O)O)O)O)O)O)O", "CC(=CCC1=C(C=C(C(=C1O)C(=O)C=CC2=CC=C(C=C2)O)OC)O)C", "C1=CC(=CC=C1CCC(=O)C2=C(C=C(C=C2OC3C(C(C(C(O3)CO)O)O)O)O)O)O", "CC1C(C(C(C(O1)OC2C(C(C(OC2C3=C(C=C(C4=C3OC(=CC4=O)C5=CC=C(C=C5)O)O)O)CO)O)O)O)O)O"]
FPID=["9716", "9717", "9718", "9719", "9720", "9722", "9723", "9912", "9913", "9914", "9915", "9916", "9930", "9932", "9933", "9942", "9944", "9945", "9964", "9965", "9966", "9967", "9969", "9970", "9973", "9974", "9996", "10016", "10017"]
directory = "/Users/ecauet/Documents/METASPACE/Fukui-Model/Molecules-Test/"

print len(SMILES)
print len(FPID)

import sys
import os
os.system("source /usr/local/phenix-1.10.1-2155/phenix_env.sh")

"""
STEPS I and II: 
MM OPTIMIZATION + CREATION OF A GAUSSVIEW FILE
"""
#Insert the list of molecules to be optimised (smiles + FPID)
#One directory FPID_# is created for each molecule in /Users/ecauet/Documents/METASPACE/Fukui-Model/Molecules-Test.
#The MM geometry optimization is perfromed for each molecules with elbow.

for S, FP in zip(SMILES, FPID):
    smiles_dir = directory+"FPID_"+FP+"/"
    if not os.path.exists(smiles_dir):
       os.makedirs(smiles_dir)
    command = "/usr/local/phenix-1.10.1-2155//build/bin/phenix.elbow --opt --smiles=\""+S+"\" --output=/Users/ecauet/Documents/METASPACE/Fukui-Model/Molecules-Test/test1/FPID_"+FP+"/elbow_FPID_"+FP
    #print command
    os.system(command)
    os.makedirs(smiles_dir+"Forces/")
    S_file=open(os.path.join(smiles_dir+str(S)), "w")
    S_file.write(S)
    S_file.close()


#STEP II: CREATE A GAUSSVIEW FILE 
    
    
for FP in FPID:
    myfolder = directory+"FPID_"+FP+"/"
    #myfolder=str(sys.argv[1])

    for file in os.listdir(myfolder):
        if file.endswith(".xyz") and file.startswith("elbow"):
            myfile= open(myfolder + file, "r")
            mystring=file[6:15]
            myfilename="/gv_" + mystring +".com"
            out_file = open(myfolder + myfilename, "w")

            lines = myfile.readlines()
            Natom=lines[0]
            Natom = int(Natom)

            out_file.write("#P HF/STO-3G opt\n\n")
            out_file.write(lines[0])
            out_file.write("\n0 1 \n")
            out_file.writelines(lines[len(lines)-Natom:len(lines)])
            out_file.write("\n")

    myfile.close()
    out_file.close()
"""
"""
#STEP III
#CREATION OF A NWCHEM FILE AFTER THE MOLECULE HAS BEEN PROTONATED AND UNPROTONATED MANUALLY
"""

import sys
import os
import os.path
import re

for FP in FPID:
    
    isThereNeutral= 0
    isThereAcid=0
    isThereBasic=0
    
    myfolder = directory+"FPID_"+FP+"/"
    chargeN=int(input("Enter the charge at neutral pH of the species FPID "+FP+" : "))
    print 'THE CHARGE OF THE NEUTRAL SPECIES IS:', chargeN
    
    for file in os.listdir(myfolder):
        if file.endswith("neutralpH.com"):
            myfileN= open(myfolder + file, "r")
            isThereNeutral=1
            
        elif file.endswith("acidpH.com"):
            myfileA= open(myfolder + file, "r")
            isThereAcid=1

        elif file.endswith("basicpH.com"):
            myfileB= open(myfolder + file, "r")
            isThereBasic=1

    if isThereNeutral==0:
        print 'NO OPTIMIZED GEOMETRY - SKIPPING THIS FPID'
        continue
    
    out_file = open(myfolder + "/energy-gradient.nw", "w")
    mytemplate = open(directory+"energy-template.nw", "r")
    
    lines = mytemplate.readlines()
    linesN = myfileN.readlines()
    
    pattern=re.compile(r'[(a-zA-Z)] \s+ [+-]?\d+(?:\.\d+)? \s+ [+-]?\d+(?:\.\d+)? \s+ [+-]?\d+(?:\.\d+)?' )
    out_file.writelines(lines[0:8])
    
    for line in linesN:
        if pattern.findall(line):
            array=pattern.findall(line)
            out_file.writelines(array)
            out_file.write("\n")
        else:
            pass

    out_file.write("end\n\n")

    if isThereAcid==1:
        out_file.write(lines[10])
        linesA = myfileA.readlines()
        for line_a in linesA:
            if pattern.findall(line_a):
                array_a=pattern.findall(line_a)
                out_file.writelines(array_a)
                out_file.write("\n")
            else:
                pass
        out_file.write("end\n\n")
    else:
        print 'NO PROTONATED GEOMETRY - SKIPPING THE ACID PART'
        pass

    if isThereBasic==1:
        out_file.write(lines[13])
        linesB = myfileB.readlines()
        for line_b in linesB:
            if pattern.findall(line_b):
                array_b=pattern.findall(line_b)
                out_file.writelines(array_b)
                out_file.write("\n")
            else:
                pass
        out_file.write("end\n")
    else:
        print 'NO UNPROTONATED GEOMETRY - SKIPPING THE BASIC PART'
        pass

    out_file.write("\n")

    for file in os.listdir(myfolder):
        if file.endswith("neutralpH_1.com"):
            myfileN1= open(myfolder + file, "r")
            linesN1 = myfileN1.readlines()
            out_file.write('geometry "Neutral1" noautosym units angstroms noautoz nocenter\n')
            for line_n1 in linesN1:
                if pattern.findall(line_n1):
                    array_n1=pattern.findall(line_n1)
                    out_file.writelines(array_n1)
                    out_file.write("\n")
            out_file.write("end\n")
            out_file.write("\n")
            myfileN1.close()

        elif file.endswith("neutralpH_2.com"):
            myfileN2= open(myfolder + file, "r")
            linesN2 = myfileN2.readlines()
            out_file.write('geometry "Neutral2" noautosym units angstroms noautoz nocenter\n')
            for line_n2 in linesN2:
                if pattern.findall(line_n2):
                    array_n2=pattern.findall(line_n2)
                    out_file.writelines(array_n2)
                    out_file.write("\n")
            out_file.write("end\n")
            out_file.write("\n")
            myfileN2.close()

        elif file.endswith("basicpH_1.com"):
            myfileB1= open(myfolder + file, "r")
            linesB1 = myfileB1.readlines()
            out_file.write('geometry "Basic1" noautosym units angstroms noautoz nocenter\n')
            for line_b1 in linesB1:
                if pattern.findall(line_b1):
                    array_b1=pattern.findall(line_b1)
                    out_file.writelines(array_b1)
                    out_file.write("\n")
            out_file.write("end\n")
            out_file.write("\n")
            myfileB1.close()

        elif file.endswith("basicpH_2.com"):
            myfileB2= open(myfolder + file, "r")
            linesB2 = myfileB2.readlines()
            out_file.write('geometry "Basic2" noautosym units angstroms noautoz nocenter\n')
            for line_b2 in linesB2:
                if pattern.findall(line_b2):
                    array_b2=pattern.findall(line_b2)
                    out_file.writelines(array_b2)
                    out_file.write("\n")
            out_file.write("end\n")
            out_file.write("\n")
            myfileB2.close()
        else:
            pass

    ### Writing the Command Lines ###

    out_file.writelines(lines[15:29])
    out_file.write("\n")
    out_file.write('set geometry "Neutral"\n')
    out_file.write('title "Geometry - Neutral pH__"\n')
    out_file.write('charge {:01d}\n'.format(chargeN))
    out_file.write('task dft gradient\n\n')

    if isThereAcid==1:
        out_file.write('set geometry "Acid"\n')
        out_file.write('title "Geometry - Acid pH__"\n')
        out_file.write('charge {:01d}\n'.format(chargeN+1))
        out_file.write('task dft gradient\n\n')
    else:
        pass

    if isThereBasic==1:
        out_file.write('set geometry "Basic"\n')
        out_file.write('title "Geometry - Basic pH__"\n')
        out_file.write('charge {:01d}\n'.format(chargeN-1))
        out_file.write('task dft gradient\n\n')
    else:
        pass

    ### Add Extra options ###
    
    for file in os.listdir(myfolder):
        if file.endswith("neutralpH_1.com"):
           out_file.write('set geometry "Neutral1"\n')
           out_file.write('title "Geometry - Neutral pH_1"\n')
           out_file.write('charge {:01d}\n'.format(chargeN))
           out_file.write('task dft gradient\n\n')

        elif file.endswith("neutralpH_2.com"):
           out_file.write('set geometry "Neutral2"\n')
           out_file.write('title "Geometry - Neutral pH_2"\n')
           out_file.write('charge {:01d}\n'.format(chargeN))
           out_file.write('task dft gradient\n\n')

        elif file.endswith("basicpH_1.com"):
           out_file.write('set geometry "Basic1"\n')
           out_file.write('title "Geometry - Basic pH_1"\n')
           out_file.write('charge {:01d}\n'.format(chargeN-2))
           out_file.write('task dft gradient\n\n')

        elif file.endswith("basicpH_2.com"):
           out_file.write('set geometry "Basic2"\n')
           out_file.write('title "Geometry - Basic pH_2"\n')
           out_file.write('charge {:01d}\n'.format(chargeN-3))
           out_file.write('task dft gradient\n\n')
        else:
            pass

    myfileN.close()
    myfileA.close()
    myfileB.close()
    mytemplate.close()
    out_file.close()

"""