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
            if len(i)<3:
                i.append(1);
            if not (([i[0],i[1],i[2]] in uniquebonds) or ([i[1],i[0],i[2]] in uniquebonds)):
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
            
        
        
        
    def __init__(self,atoms,forces,bonds,atomsXYZ=[],breakage_threshold=0.0,breakage_threshold_absolute=True,fragmentation_depth=2,Group_Atom_Numbers=False):
        '''
        Preparation of the fragmentation inputs
        '''
        if len(atomsXYZ)>0 and len(atomsXYZ)==len(atoms):
            self.AtomXYZ=atomsXYZ;
        elif len(atomsXYZ)>0:
            raise NameError('Atoms and AtomsXYZ have different lengths!');
        if len(atoms)!=len(forces): 
            raise NameError('Atoms and Forces have different lengths!');
        if len(atoms)==0: 
            raise NameError('Empty Atoms!');
        if len(forces)==0:
            raise NameError('Empty Forces!');            
        self.ReturnAtomNumbers=Group_Atom_Numbers;
        self.AtomCount=len(atoms);
        self.Atoms=atoms;
        self.AtomGroups=[0]*self.AtomCount;
        self.BondsArray= [[0] * self.AtomCount for i in range(self.AtomCount)];
        self.BreakableBonds=[];
        self.BrokenBonds=[];
        self.BondForces=[];
        for bond in bonds:
            if len(bond)>2:
                self.BondsArray[bond[0]][bond[1]]=bond[2];
                self.BondsArray[bond[1]][bond[0]]=bond[2];
            else:
                self.BondsArray[bond[0]][bond[1]]=1;
                self.BondsArray[bond[1]][bond[0]]=1;
            f1=forces[bond[0]];
            f2=forces[bond[1]];
            BondForce=math.sqrt(f1*f1+f2*f2);
            self.BondForces.append(BondForce);
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
                raise NameError('Forces Identical! Cannot normalise!');
            else:
                for i in range(0,len(self.BondForces)):
                    self.BondForces[i]=(self.BondForces[i]-minf)/ForceRange;
        
        for i in range(0,len(self.BondForces)):
            if self.BondForces[i]>=breakage_threshold:
                self.BreakableBonds.append([i,bonds[i],self.BondForces[i],False]);
        print('Bond forces ', self.BondForces);
        print('Breakable bonds ', self.BreakableBonds);
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
    forces=[0.007588212767180424, 0.006661618572088917, 0.009570650970545316, 0.019269484295123207, 0.08017421296776164, 0.0144983061079562, 0.06769232697285564, 0.1374647546245946, 0.03697424664546933, 0.0315693346778167, 0.007913059711641258, 0.0006550076335433046, 0.0005430184158939733, 0.0007928871294200714, 0.0026211724475890554, 0.010472723714488033, 0.008070656478874566, 0.03771033870174066, 0.0335120686022215];\
    bonds=[[0, 1, 4], [0, 5, 4], [0, 11, 1], [1, 2, 4], [1, 12, 1], [2, 3, 4], [2, 13, 1], [3, 4, 4], [3, 9, 1], [4, 5, 4], [4, 6, 1], [5, 14, 1], [6, 7, 1], [6, 17, 1], [6, 18, 1], [7, 8, 1], [7, 9, 1], [8, 15, 1], [8, 16, 1], [9, 10, 1]];\
    frag=FragmenterBasic(atoms,forces,bonds,breakage_threshold=0.5,\
    breakage_threshold_absolute=False,\
    fragmentation_depth=2,\
    Group_Atom_Numbers=True);", \
    setup="from __main__ import FragmenterBasic",number=100));


    atoms=[[12.0,'C',0,0,0], [12.0,'C',0,0,0], [12.0,'C',0,0,0], [12.0,'C',0,0,0], [12.0,'C',0,0,0], [12.0,'C',0,0,0], [14.003074,'N',0,0,0], [12.0,'C',0,0,0], [14.003074,'N',0,0,0], [14.003074,'N',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0]];
    forces=[0.007588212767180424, 0.006661618572088917, 0.009570650970545316, 0.019269484295123207, 0.08017421296776164, 0.0144983061079562, 0.06769232697285564, 0.1374647546245946, 0.03697424664546933, 0.0315693346778167, 0.007913059711641258, 0.0006550076335433046, 0.0005430184158939733, 0.0007928871294200714, 0.0026211724475890554, 0.010472723714488033, 0.008070656478874566, 0.03771033870174066, 0.0335120686022215];
    bonds=[[0, 1, 4], [0, 5, 4], [0, 11, 1], [1, 2, 4], [1, 12, 1], [2, 3, 4], [2, 13, 1], [3, 4, 4], [3, 9, 1], [4, 5, 4], [4, 6, 1], [5, 14, 1], [6, 7, 1], [6, 17, 1], [6, 18, 1], [7, 8, 1], [7, 9, 1], [8, 15, 1], [8, 16, 1], [9, 10, 1]];
    
    frag=FragmenterBasic(atoms,forces,bonds,breakage_threshold=0.5,breakage_threshold_absolute=False,fragmentation_depth=2,Group_Atom_Numbers=True);
    frag.SortResults(Ascending=True);
    print(frag.Fragments);
    if frag.ReturnAtomNumbers:
        print(frag.GenerateSDFFromAtomNumbers(frag.Fragments[0][1][0]));





