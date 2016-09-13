# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 23:39:19 2016

@author: ilaponog
"""

import pybel;
import openbabel;
import Fragmenter_V2 as fg;
import os;

def PybelModel_To_Fragmenter(mol):
    
    atoms=[];atomsXYZ=[];
    for i in mol.atoms:
        aname=i.type;
        if aname[-1:] in '0123456789':
            aname=aname[:-1];
        if i.OBAtom.IsAromatic():
            ar=1;
            aname=aname.replace('ar','');
        else:
            ar=0;
        isotope=0;
        '''
        Place isotope treatment block here...... To be added.....
        
        '''
        atoms.append([i.OBAtom.GetExactMass(),aname,isotope, i.formalcharge,ar]);
        atomsXYZ.append([i.OBAtom.GetX(),i.OBAtom.GetY(),i.OBAtom.GetZ()])
    bonds=[];
    for pb in openbabel.OBMolBondIter( mol.OBMol):
        if pb.IsAromatic():
            bo=4;
        else:
            bo=pb.GetBondOrder();
        i=pb.GetBeginAtomIdx()-1;
        j=pb.GetEndAtomIdx()-1;
        bonds.append([i,j,bo]);
    forces=[1.0]*len(atoms);
    '''
    Place force estimations here if needed.
    '''
    return [atoms,forces,bonds,atomsXYZ];
    

def FragmenterHTML_Generate(out_path,out_name,fragmenter,title='Fragmenter Results'):    
    cc=0;
    if not os.path.exists(out_path+'/'+out_name):
        os.makedirs(out_path+'/'+out_name);
    fout=open(out_path+'/'+out_name+'.html','w');
    
    fout.write('<!DOCTYPE html>\n');
    fout.write('<html>\n');
    fout.write('<head>\n');
    fout.write('<title>%s</title>\n'%title);
    fout.write('</head>\n');
    fout.write('\n');
    fout.write('<body>\n');
    fout.write('<table border=1>\n');

    
    for i in fragmenter.Fragments:
        fout.write('<tr>\n');
        fout.write('<th>%12.3f</th>\n'%i[0]);
        if len(i)>1:
            for j in i[1]:
                #fout.write('<th>%s</th>\n'%j);
                sdf=fragmenter.GenerateSDFFromAtomNumbers(j);
                mol2=pybel.readstring('sdf',sdf);
                mol2.title='';
                
                cc+=1;
                filename=out_name+'/%s.png'%cc;
                print(filename);
                
                                
                
                
                #mol2.make3D();
                mol2.draw(show=False,filename=filename,usecoords=False);
                mm2=mol2.exactmass;               
                
                mm=0.0;hh=0;
                for atom in mol2.atoms:
                    mm+=atom.exactmass;
                    
                    
                    v=atom.OBAtom.GetValence();
                    vv=atom.OBAtom.GetImplicitValence();
                    hh+=vv-v;
                    
                
                #mol2.addh();
                #mm=mol2.exactmass-mm;
                
                fout.write('<th><img src=%s><p>SMILES: %s -%s x [H]</p><p>Mass: %10.3f</p><p>Mass2: %10.3f</p>'%(filename,mol2.write('smi'),hh,mm,mm2));
                
                #for atom in mol2.atoms:
                #    v=atom.OBAtom.GetValence();
                #    vv=atom.OBAtom.GetImplicitValence();
                #    atom.OBAtom.SetImplicitValence(v);
                #    vv=atom.OBAtom.GetImplicitValence();
                #    fout.write('<p>Valence %s</p><p>ImplicitValence: %s</p>'%(v,vv));
                    
                    
                
                fout.write('</th>\n');
                
                
            
        fout.write('</tr>\n');
    
    
    
    fout.write('</table>\n');

    


    fout.write('</body>\n');
    fout.write('</html> \n');
    
    #for i in fragmenter.GroupAtomNumbers:
    #    if len(i)>groupY:
    #        groupY=len(i);
            
            
    fout.close();
    

#-------------------------------------------------------------------------------
if __name__=='__main__':
    
    mol=pybel.readstring('smi','c1cnccc1C=CC#CC');
    mol.addh();
    mol.make3D();
    atoms,forces,bonds,atomsXYZ=PybelModel_To_Fragmenter(mol);
    
    frag=fg.FragmenterBasic(atoms,forces,bonds,atomsXYZ,0.0,True,2,True);
    frag.SortResults(False);
    print(frag.Fragments);
    if frag.ReturnAtomNumbers:
        sdf=frag.GenerateSDFFromAtomNumbers(frag.Fragments[len(frag.Fragments)-1][1][0]);
        print(sdf);
        mol2=pybel.readstring('sdf',sdf);
        print(mol.write('inchi'));    
        print(mol2.write('inchi'));
        currentpath=os.path.dirname(os.path.realpath(__file__)).replace('\\','/');
        print(currentpath);
        FragmenterHTML_Generate(currentpath,'FragResults',frag,'FragmenterBasic');
    
    
    #for i in frg[2]:
    #        print("%s%s-%s%s"%(frg[0][i[0]][1],i[0],frg[0][i[1]][1],i[1]));

    atoms=[[12.0,'C',0,0,0], [12.0,'C',0,0,0], [12.0,'C',0,0,0], [12.0,'C',0,0,0], [12.0,'C',0,0,0], [12.0,'C',0,0,0], [14.003074,'N',0,0,0], [12.0,'C',0,0,0], [14.003074,'N',0,0,0], [14.003074,'N',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0], [1.007825,'H',0,0,0]];
    forces=[0.007588212767180424, 0.006661618572088917, 0.009570650970545316, 0.019269484295123207, 0.08017421296776164, 0.0144983061079562, 0.06769232697285564, 0.1374647546245946, 0.03697424664546933, 0.0315693346778167, 0.007913059711641258, 0.0006550076335433046, 0.0005430184158939733, 0.0007928871294200714, 0.0026211724475890554, 0.010472723714488033, 0.008070656478874566, 0.03771033870174066, 0.0335120686022215];
    bonds=[[0, 1, 4], [0, 5, 4], [0, 11, 1], [1, 2, 4], [1, 12, 1], [2, 3, 4], [2, 13, 1], [3, 4, 4], [3, 9, 1], [4, 5, 4], [4, 6, 1], [5, 14, 1], [6, 7, 1], [6, 17, 1], [6, 18, 1], [7, 8, 1], [7, 9, 1], [8, 15, 1], [8, 16, 1], [9, 10, 1]];
    
    frag=fg.FragmenterBasic(atoms,forces,bonds,breakage_threshold=0.5,breakage_threshold_absolute=False,fragmentation_depth=2,Group_Atom_Numbers=True);
        
    frag.SortResults(Ascending=True);
    print(frag.Fragments);
    if frag.ReturnAtomNumbers:
        sdf=frag.GenerateSDFFromAtomNumbers(frag.Fragments[len(frag.Fragments)-1][1][0]);
        print(sdf);
        mol2=pybel.readstring('sdf',sdf);
        print(mol.write('inchi'));    
        print(mol2.write('inchi'));
        currentpath=os.path.dirname(os.path.realpath(__file__)).replace('\\','/');
        print(currentpath);
        FragmenterHTML_Generate(currentpath,'FragResults2',frag,'FragmenterBasic');
    

