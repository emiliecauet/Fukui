# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 11:07:28 2016

@author: ecauet
"""
FPID=["1384"]
directory = "/Users/ecauet/Documents/METASPACE/Fukui-Model/Molecules-Test/TESTS/"

import os
import os.path

""" 
STEP IV:
EXTRACT THE FORCES FROM THE NWCHEM OUTPUT FILE
"""
def deletefiles(directory):
    filelist = [f for f in os.listdir(directory) if f.endswith(".inp")]
    for f in filelist:
        os.remove(directory+f)
    return
    
for FP in FPID:
    
    isThereOutput= 0
    
    myfolder = directory+"FPID_"+FP+"/Forces/"
    print myfolder
    #myfolder=str(sys.argv[1])
    folders = ['GRADIENT_NA','GRADIENT_NB']
    
    for file in os.listdir(myfolder):
        if file.endswith("energy-gradient.out00"):
            myfilename= myfolder + "energy-gradient.out00"
            myfile= open(myfilename, "r")
            isThereOutput=1

    if isThereOutput==0:
        print 'NO OUTPUT FILE - SKIPPING THIS FPID'
        continue

    try:
        for folder in folders:
            os.makedirs(os.path.join(myfolder,folder))
    except (OSError, 17), e:
            pass
    
    deletefiles(myfolder)
    deletefiles(myfolder+"GRADIENT_NA/")
    deletefiles(myfolder+"GRADIENT_NB/")

    outN_file = open(myfolder + "gradientN.inp", "w+")
    outA_file = open(myfolder + "gradientA.inp", "w+")
    outB_file = open(myfolder + "gradientB.inp", "w+") 
    gradient_NA = open(myfolder + "GRADIENT_NA/gradient_NA.inp", "w+")
    gradient_NB = open(myfolder + "GRADIENT_NB/gradient_NB.inp", "w+")

    searchlines = myfile.readlines()
    myfile.close()

    for i, line in enumerate(searchlines):

        if "No. of atoms     :" in line:
            [int(N) for N in line.split() if N.isdigit()]       
            Natom=N

        if "DFT ENERGY GRADIENTS" in line:
            for l in searchlines[i+4:i+4+int(Natom)]:
                if "Geometry - Neutral pH__" in searchlines[i-11]:
                    outN_file.write(l[5:])

                elif "Geometry - Acid pH__" in searchlines[i-11]:           
                    outA_file.write(l[5:])

                elif "Geometry - Basic pH__" in searchlines[i-11]:           
                    outB_file.write(l[5:])

                elif "Geometry - Neutral pH_1" in searchlines[i-11]:                        
                    outN1_file = open(myfolder + "/gradientN1.inp", "a+")  
                    outN1_file.write(l[5:])

                elif "Geometry - Neutral pH_2" in searchlines[i-11]:                
                    outN2_file = open(myfolder + "/gradientN2.inp", "a+")  
                    outN2_file.write(l[5:])

                elif "Geometry - Basic pH_1" in searchlines[i-11]:
                    outB1_file = open(myfolder + "/gradientB1.inp", "a+")
                    outB1_file.write(l[5:])

                elif "Geometry - Basic pH_2" in searchlines[i-11]:             
                    outB2_file = open(myfolder + "/gradientB2.inp", "a+") 
                    outB2_file.write(l[5:])

    outN_file.write("\n")
    outA_file.write("\n")
    outB_file.write("\n")

    outN_file.seek(0)
    outA_file.seek(0) 
    outB_file.seek(0)

    ### MERGE THE FILES ###

    gradient_NA.write(outN_file.read() + outA_file.read())
    outN_file.seek(0)
    outA_file.seek(0)

    gradient_NB.write(outN_file.read() + outB_file.read())       
    outN_file.seek(0)
    outB_file.seek(0)
    
    if os.path.exists(myfolder + "gradientB1.inp"):
        #os.makedirs(myfolder+"GRADIENT_NB1/")
        outB1_file.seek(0)
        gradient_NB1 = open(myfolder + "GRADIENT_NB/gradient_NB1.inp", "w")
        gradient_NB1.write(outN_file.read() + outB1_file.read() + "\n")
        outN_file.seek(0)
        outB1_file.seek(0)
        gradient_NB1.close()
    else:
        pass

    if os.path.isfile(myfolder + "/gradientB2.inp"):
        #os.makedirs(myfolder+"GRADIENT_NB2/")
        outB2_file.seek(0)
        gradient_NB2 = open(myfolder + "GRADIENT_NB/gradient_NB2.inp", "w")
        gradient_NB2.write(outN_file.read() + outB2_file.read() + "\n")
        outN_file.seek(0)
        outB2_file.seek(0)
        gradient_NB2.close()
    else:
        pass

    if os.path.isfile(myfolder + "/gradientN1.inp"):
        #os.makedirs(myfolder+"GRADIENT_N1A/")
        #os.makedirs(myfolder+"GRADIENT_N1B/")
        outN1_file.seek(0)
        gradient_N1A = open(myfolder + "GRADIENT_NA/gradient_N1A.inp", "w")
        gradient_N1B = open(myfolder + "GRADIENT_NB/gradient_N1B.inp", "w")
        gradient_N1A.write(outN1_file.read() + "\n" + outA_file.read())
        outN1_file.seek(0)
        gradient_N1B.write(outN1_file.read() + "\n" + outB_file.read())
        outN1_file.seek(0)
        outA_file.seek(0)
        outB_file.seek(0)
        gradient_N1A.close()
        gradient_N1B.close()
    else:
        pass

    if os.path.isfile(myfolder + "/gradientN2.inp"):
        #os.makedirs(myfolder+"GRADIENT_N2A/")
        #os.makedirs(myfolder+"GRADIENT_N2B/")
        outN2_file.seek(0)
        gradient_N2A = open(myfolder + "GRADIENT_NA/gradient_N2A.inp", "w")
        gradient_N2B = open(myfolder + "GRADIENT_NB/gradient_N2B.inp", "w")
        gradient_N2A.write(outN2_file.read() + "\n" + outA_file.read())
        outN2_file.seek(0)
        gradient_N2B.write(outN2_file.read() + "\n" + outB_file.read())
        outN2_file.seek(0)
        outA_file.seek(0)
        outB_file.seek(0)
        gradient_N2A.close()
        gradient_N2B.close()
    else:
        pass

    outN_file.close()
    outA_file.close() 
    outB_file.close()
    gradient_NA.close()
    gradient_NB.close()