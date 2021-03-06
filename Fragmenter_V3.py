# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 14:33:47 2016

@author: Dr. Ivan Laponogov, ICL, London
"""

#import numpy as np;
import math;


def GetUniqueBonds(bonds):
        uniquebonds=[];
        for i in bonds:
            if len(i)==2:
                i.append(1);
                i.append(0.0);
            elif len(i)==3:
                i.append(0.0);
            if not (([i[0],i[1],i[2],i[3]] in uniquebonds) or ([i[1],i[0],i[2],i[3]] in uniquebonds)):
                uniquebonds.append(i);
        return uniquebonds;
    

class FragmenterBasic:
    
    def __PropagateAtomGroup(self,index,groupindex):
        for i in range(0,self.AtomCount):
            if self.BondsArray[i][index]>0:
                if self.AtomGroups[i]==0:
                    self.AtomGroups[i]=groupindex;
                    self.__PropagateAtomGroup(i,groupindex);
    

    def GenerateSDFFromAtomNumbers(self,AtomNumbers):
        SDF='AtomSet %s\nBasicFingerprinter\n\n'%AtomNumbers;
        AtomBonds=[];
        for i in range(0,len(AtomNumbers)-1):
            for j in range(i+1,len(AtomNumbers)):
                if self.BondsArray[AtomNumbers[i]][AtomNumbers[j]]>0:
                    AtomBonds.append([i,j,self.BondsArray[AtomNumbers[i]][AtomNumbers[j]]]);
        SDF+='%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d V2000\n'%(len(AtomNumbers),len(AtomBonds),0,0,0,0,0,0,0,0,999);
        atoms=[];
        for i in AtomNumbers:
            atoms.append([i,self.Atoms[i],0.0,0.0,0.0]);
        
        if hasattr(self,'AtomXYZ'):
            for atom in atoms:
                atom[2]=self.AtomXYZ[atom[0]][0];
                atom[3]=self.AtomXYZ[atom[0]][1];
                atom[4]=self.AtomXYZ[atom[0]][2];
            
        for atom in atoms:
            charge=self.Atoms[atom[0]][3];
            if charge==3:
                ccc=1;
            elif charge==2:
                ccc=2;
            elif charge==1:
                ccc=3;
            elif charge==-1:
                ccc=5;
            elif charge==-2:
                ccc=6;
            elif charge==-3:
                ccc=7;
            else:
                ccc=0;
            v=0;
            for j in AtomNumbers:
                if self.BondsArray[atom[0]][j]>0:
                    v+=1;
            SDF+='%10.4f%10.4f%10.4f %3s%2d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d\n'%(atom[2],atom[3],atom[4],\
            atom[1][1],atom[1][2],\
            ccc,\
            0,1,0,v,0,0,0,0,0,0);
        for bond in AtomBonds:
            SDF+='%3d%3d%3d%3d%3d%3d%3d\n'%(bond[0]+1,bond[1]+1,bond[2],0,0,0,0);
        charge=0.0;
        for i in AtomNumbers:
            charge+=self.Atoms[i][3];
        SDF+='>  <TOTAL_CHARGE>\n%s\n'%charge;
        mass=0.0;
        for i in AtomNumbers:
            mass+=self.Atoms[i][0];
        SDF+='>  <EXACT_MASS>\n%s\n'%mass;
        SDF+='$$$$';
        return SDF;        

    def __GenerateGroups(self,current_level):
        for i in range(0,self.AtomCount):
            self.AtomGroups[i]=0;
        #self.AtomGroups=[0]*self.AtomCount;
        groupcount=0;
        for i in range(0,self.AtomCount):
            if self.AtomGroups[i]==0:
                groupcount+=1;
                self.AtomGroups[i]=groupcount;
                self.__PropagateAtomGroup(i,groupcount);
                
        for i in range(1, groupcount+1):
            mass=0.0;
            for j in range(0, self.AtomCount):
                if self.AtomGroups[j]==i:
                    mass+=self.Atoms[j][0];
            if not (mass in self.Fragments):
                self.Fragments.append(mass);
                if self.ReturnAtomNumbers:
                    self.GroupAtomNumbers.append([]);
                    FragmentIndex=len(self.Fragments)-1;
            else:
                if self.ReturnAtomNumbers:
                    FragmentIndex=self.Fragments.index(mass);
            if self.ReturnAtomNumbers:
                    numbers=[];
                    for j in range(0, self.AtomCount):
                        if self.AtomGroups[j]==i:
                            numbers.append(j);
                    if self.ReturnAtomNumbers and (not (numbers in self.GroupAtomNumbers[FragmentIndex])):
                        self.GroupAtomNumbers[FragmentIndex].append(numbers);
                    
        

    def __ProcessFragment(self,current_level):
        for i in range(0,len(self.BreakableBonds)):
            if self.BreakableBonds[i][3]==True:
                bond=self.BreakableBonds[i][1];
                self.BondsArray[bond[0]][bond[1]]=0;
                self.BondsArray[bond[1]][bond[0]]=0;
        self.__GenerateGroups(current_level);
        for i in range(0,len(self.BreakableBonds)):
            if self.BreakableBonds[i][3]==True:
                bond=self.BreakableBonds[i][1];
                if len(bond)>2:
                    self.BondsArray[bond[0]][bond[1]]=bond[2];
                    self.BondsArray[bond[1]][bond[0]]=bond[2];
                else:
                    self.BondsArray[bond[0]][bond[1]]=1;
                    self.BondsArray[bond[1]][bond[0]]=1;
            
        
    def __ProcessFragmentationLevel(self,fragmentation_depth,current_level):
        for i in range(0,len(self.BreakableBonds)):
            if self.BreakableBonds[i][3]==False:
                    self.BreakableBonds[i][3]=True;
                    self.BrokenBonds.append(self.BreakableBonds[i]);
                    self.__ProcessFragment(current_level);
                    
                    if current_level<fragmentation_depth:
                        self.__ProcessFragmentationLevel(fragmentation_depth,current_level+1);

                    self.BreakableBonds[i][3]=False;
                    #print(self.BrokenBonds);
                    self.BrokenBonds.pop();
    
    
    
    def SortResults(self,Ascending=True):
            if Ascending:
                self.Fragments=sorted(self.Fragments,key=lambda sortit: sortit[0]);
            else:
                self.Fragments=sorted(self.Fragments,key=lambda sortit: sortit[0], reverse=True);
            
        
        
        
    def __init__(self,atoms,bonds,atomsXYZ=[],breakage_threshold=0.0,breakage_threshold_absolute=True,fragmentation_depth=2,Group_Atom_Numbers=False):
        '''
        Preparation of the fragmentation inputs
        '''
        if len(atomsXYZ)>0 and len(atomsXYZ)==len(atoms):
            self.AtomXYZ=atomsXYZ;
        elif len(atomsXYZ)>0:
            raise NameError('Atoms and AtomsXYZ have different lengths!');
        if len(atoms)==0: 
            raise NameError('Empty Atoms!');
        self.ReturnAtomNumbers=Group_Atom_Numbers;
        self.AtomCount=len(atoms);
        self.Atoms=atoms;
        self.AtomGroups=[0]*self.AtomCount;
        self.BondsArray= [[0] * self.AtomCount for i in range(self.AtomCount)];
        self.Bonds=bonds;
        self.BreakableBonds=[];
        self.BrokenBonds=[];
        self.BondForces=[];
        for bond in self.Bonds:
            if len(bond)>2:
                self.BondsArray[bond[0]][bond[1]]=bond[2];
                self.BondsArray[bond[1]][bond[0]]=bond[2];
            else:
                self.BondsArray[bond[0]][bond[1]]=1;
                self.BondsArray[bond[1]][bond[0]]=1;
            
            if len(bond)>3:
                self.BondForces.append(bond[3]);
            else:
                self.BondForces.append(0.0);
        if breakage_threshold_absolute==False:
            minf=1.0e8;
            maxf=0.0;
            for bondforce in self.BondForces:
                if bondforce>maxf:
                    maxf=bondforce;
                if bondforce<minf:
                    minf=bondforce;
            ForceRange=maxf-minf;
            if abs(ForceRange)<1.0e-9:
                print('Forces Identical! Cannot normalise! Setting all to 0.0');
                for i in range(0,len(self.BondForces)):
                    self.BondForces[i]=0.0;
            else:
                for i in range(0,len(self.BondForces)):
                    self.BondForces[i]=(self.BondForces[i]-minf)/ForceRange;
        
        for i in range(0,len(self.BondForces)):
            if self.BondForces[i]>=breakage_threshold:
                self.BreakableBonds.append([i,bonds[i],self.BondForces[i],False]);
        
        fragmentation_depth=min(fragmentation_depth,len(self.BreakableBonds));
        self.Fragments=[];
        if self.ReturnAtomNumbers:
            self.GroupAtomNumbers=[];
        self.__ProcessFragment(0);
        if fragmentation_depth>0:
            self.__ProcessFragmentationLevel(fragmentation_depth,1);
        for i in range(0,len(self.Fragments)):
            self.Fragments[i]=[self.Fragments[i]];
        if self.ReturnAtomNumbers:
            for i in range(0,len(self.Fragments)):
                self.Fragments[i].append(self.GroupAtomNumbers[i]);
            
                



if __name__=='__main__':

    
    import timeit;
     
    print(timeit.timeit("atoms=[[12.0,'C',0,0,0], [12.0,'C',0,0,0], [12.0,'C',0,0,0], [12.0,'C',0,0,0], [12.0,'C',0,0,0], [12.0,'C',0,0,0], [14.003074,'N',0,0,0], [12.0,'C',0,0,0], [14.003074,'N',0,0,0], [14.003074,'N',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0]];\
    bonds=[[0, 1, 4], [0, 5, 4], [0, 11, 1], [1, 2, 4], [1, 12, 1], [2, 3, 4], [2, 13, 1], [3, 4, 4], [3, 9, 1], [4, 5, 4], [4, 6, 1], [5, 14, 1], [6, 7, 1], [6, 17, 1], [6, 18, 1], [7, 8, 1], [7, 9, 1], [8, 15, 1], [8, 16, 1], [9, 10, 1]];\
    frag=FragmenterBasic(atoms,bonds,breakage_threshold=0,\
    breakage_threshold_absolute=True,\
    fragmentation_depth=2,\
    Group_Atom_Numbers=True);", \
    setup="from __main__ import FragmenterBasic",number=100));



    atomsXYZ=[\
    [0.04945500,   -0.11684300,    0.15115200],\
    [1.41715100,   -0.09888600,    0.15645200],\
    [2.16194500,    0.05035500,    1.32240700],\
    [1.43010800,    0.11899500,    2.50812800],\
    [0.00591200,    0.12587300,    2.49966400],\
    [-0.71147800,    0.03869400,    1.30628400],\
    [-0.41136200,    0.14424700,    3.80919700],\
    [0.71067400,   0.01790900,    4.63422000],\
    [0.78900500,   -0.22026900,    5.93421500],\
    [1.81935900,    0.16876000,    3.82026600],\
    [2.77095700,   -0.00156300,    4.17986200],\
    [-0.51240000,   -0.20911300,   -0.78243100],\
    [1.97578000,   -0.13222500,   -0.78170600],\
    [3.23306900,    0.10908800,    1.35820900],\
    [-1.77494500,    0.14621100,    1.32983300],\
    [0.00939887,   -0.77833871,    6.21841999],\
    [1.63866877,   -0.70868697,    6.13300979],\
    [-1.36890700,    0.16187100,    4.15897600]];

    atoms=[[12.0,'C',0,0,0], [12.0,'C',0,0,0], [12.0,'C',0,0,0], [12.0,'C',0,0,0], [12.0,'C',0,0,0], [12.0,'C',0,0,0], [14.003074,'N',0,0,0], [12.0,'C',0,0,0], [14.003074,'N',0,0,0], [14.003074,'N',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0]];
    bonds=[[0, 1, 4], [0, 5, 4], [0, 11, 1], [1, 2, 4], [1, 12, 1], [2, 3, 4], [2, 13, 1], [3, 4, 4], [3, 9, 1], [4, 5, 4], [4, 6, 1], [5, 14, 1], [6, 7, 1], [6, 17, 1], [7, 8, 1], [7, 9, 1], [8, 15, 1], [8, 16, 1], [9, 10, 1]];
    
    frag=FragmenterBasic(atoms,bonds,atomsXYZ,breakage_threshold=0.0,breakage_threshold_absolute=True,fragmentation_depth=2,Group_Atom_Numbers=True);
    frag.SortResults(Ascending=False);
    print(frag.Fragments);
    if frag.ReturnAtomNumbers:
        print(frag.GenerateSDFFromAtomNumbers(frag.Fragments[0][1][0]));





