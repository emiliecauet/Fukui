import numpy
import Fragmenter_V2 as fg

atoms=[[12.0, 'C', 0, 0, 0], [12.0, 'C', 0, 0, 0], [12.0, 'C', 0, 0, 0], [12.0, 'C', 0, 0, 0], [12.0, 'C', 0, 0, 0], [12.0, 'C', 0, 0, 0], [14.003074004432, 'N', 0, 0, 0], [12.0, 'C', 0, 0, 0], [14.003074004432, 'N', 0, 0, 0], [14.003074004432, 'N', 0, 0, 0], [1.007825032239, 'H', 0, 0, 0], [1.007825032239, 'H', 0, 0, 0], [1.007825032239, 'H', 0, 0, 0], [1.007825032239, 'H', 0, 0, 0], [1.007825032239, 'H', 0, 0, 0], [1.007825032239, 'H', 0, 0, 0], [1.007825032239, 'H', 0, 0, 0], [1.007825032239, 'H', 0, 0, 0], [1.007825032239, 'H', 0, 0, 0]]

forces=[0.004015530432136538, 0.0035251953159780134, 0.00506459708059317, 0.010197025699293297, 0.042426590018280114, 0.007672213626208262, 0.03582142558749575, 0.07274359885224296, 0.019566031839849462, 0.01670586052480704, 0.00418743293820632, 0.00034661693951844563, 0.00028735448532277294, 0.0004195800111465136, 0.0013870720358151757, 0.005541955935232777, 0.004270829995490843, 0.017733916462923573, 0.019955557034187124]

bonds=[[0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1], [0, 5, 1], [0, 6, 1], [0, 7, 1], [0, 9, 1], [0, 10, 1], [0, 11, 1], [0, 12, 1], [0, 13, 1], [0, 14, 1], [0, 17, 1], [0, 18, 1], [1, 0, 1], [1, 2, 1], [1, 3, 1], [1, 4, 1], [1, 5, 1], [1, 6, 1], [1, 7, 1], [1, 9, 1], [1, 10, 1], [1, 11, 1], [1, 12, 1], [1, 13, 1], [1, 14, 1], [1, 17, 1], [1, 18, 1], [2, 0, 1], [2, 1, 1], [2, 3, 1], [2, 4, 1], [2, 5, 1], [2, 6, 1], [2, 7, 1], [2, 8, 1], [2, 9, 1], [2, 10, 1], [2, 11, 1], [2, 12, 1], [2, 13, 1], [2, 14, 1], [2, 16, 1], [2, 17, 1], [2, 18, 1], [3, 0, 1], [3, 1, 1], [3, 2, 1], [3, 4, 1], [3, 5, 1], [3, 6, 1], [3, 7, 1], [3, 8, 1], [3, 9, 1], [3, 10, 1], [3, 11, 1], [3, 12, 1], [3, 13, 1], [3, 14, 1], [3, 15, 1], [3, 16, 1], [3, 17, 1], [3, 18, 1], [4, 0, 1], [4, 1, 1], [4, 2, 1], [4, 3, 1], [4, 5, 1], [4, 6, 1], [4, 7, 1], [4, 8, 1], [4, 9, 1], [4, 10, 1], [4, 11, 1], [4, 12, 1], [4, 13, 1], [4, 14, 1], [4, 15, 1], [4, 16, 1], [4, 17, 1], [4, 18, 1], [5, 0, 1], [5, 1, 1], [5, 2, 1], [5, 3, 1], [5, 4, 1], [5, 6, 1], [5, 7, 1], [5, 8, 1], [5, 9, 1], [5, 10, 1], [5, 11, 1], [5, 12, 1], [5, 13, 1], [5, 14, 1], [5, 15, 1], [5, 17, 1], [5, 18, 1], [6, 0, 1], [6, 1, 1], [6, 2, 1], [6, 3, 1], [6, 4, 1], [6, 5, 1], [6, 7, 1], [6, 8, 1], [6, 9, 1], [6, 10, 1], [6, 11, 1], [6, 12, 1], [6, 13, 1], [6, 14, 1], [6, 15, 1], [6, 16, 1], [6, 17, 1], [6, 18, 1], [7, 0, 1], [7, 1, 1], [7, 2, 1], [7, 3, 1], [7, 4, 1], [7, 5, 1], [7, 6, 1], [7, 8, 1], [7, 9, 1], [7, 10, 1], [7, 13, 1], [7, 14, 1], [7, 15, 1], [7, 16, 1], [7, 17, 1], [7, 18, 1], [8, 2, 1], [8, 3, 1], [8, 4, 1], [8, 5, 1], [8, 6, 1], [8, 7, 1], [8, 9, 1], [8, 10, 1], [8, 13, 1], [8, 15, 1], [8, 16, 1], [8, 17, 1], [8, 18, 1], [9, 0, 1], [9, 1, 1], [9, 2, 1], [9, 3, 1], [9, 4, 1], [9, 5, 1], [9, 6, 1], [9, 7, 1], [9, 8, 1], [9, 10, 1], [9, 11, 1], [9, 12, 1], [9, 13, 1], [9, 14, 1], [9, 15, 1], [9, 16, 1], [9, 17, 1], [9, 18, 1], [10, 0, 1], [10, 1, 1], [10, 2, 1], [10, 3, 1], [10, 4, 1], [10, 5, 1], [10, 6, 1], [10, 7, 1], [10, 8, 1], [10, 9, 1], [10, 12, 1], [10, 13, 1], [10, 15, 1], [10, 16, 1], [10, 17, 1], [10, 18, 1], [11, 0, 1], [11, 1, 1], [11, 2, 1], [11, 3, 1], [11, 4, 1], [11, 5, 1], [11, 6, 1], [11, 9, 1], [11, 12, 1], [11, 13, 1], [11, 14, 1], [11, 17, 1], [11, 18, 1], [12, 0, 1], [12, 1, 1], [12, 2, 1], [12, 3, 1], [12, 4, 1], [12, 5, 1], [12, 6, 1], [12, 9, 1], [12, 10, 1], [12, 11, 1], [12, 13, 1], [12, 14, 1], [13, 0, 1], [13, 1, 1], [13, 2, 1], [13, 3, 1], [13, 4, 1], [13, 5, 1], [13, 6, 1], [13, 7, 1], [13, 8, 1], [13, 9, 1], [13, 10, 1], [13, 11, 1], [13, 12, 1], [13, 14, 1], [13, 16, 1], [13, 17, 1], [13, 18, 1], [14, 0, 1], [14, 1, 1], [14, 2, 1], [14, 3, 1], [14, 4, 1], [14, 5, 1], [14, 6, 1], [14, 7, 1], [14, 9, 1], [14, 11, 1], [14, 12, 1], [14, 13, 1], [14, 17, 1], [14, 18, 1], [15, 3, 1], [15, 4, 1], [15, 5, 1], [15, 6, 1], [15, 7, 1], [15, 8, 1], [15, 9, 1], [15, 10, 1], [15, 16, 1], [15, 17, 1], [15, 18, 1], [16, 2, 1], [16, 3, 1], [16, 4, 1], [16, 6, 1], [16, 7, 1], [16, 8, 1], [16, 9, 1], [16, 10, 1], [16, 13, 1], [16, 15, 1], [16, 17, 1], [16, 18, 1], [17, 0, 1], [17, 1, 1], [17, 2, 1], [17, 3, 1], [17, 4, 1], [17, 5, 1], [17, 6, 1], [17, 7, 1], [17, 8, 1], [17, 9, 1], [17, 10, 1], [17, 11, 1], [17, 13, 1], [17, 14, 1], [17, 15, 1], [17, 16, 1], [17, 18, 1], [18, 0, 1], [18, 1, 1], [18, 2, 1], [18, 3, 1], [18, 4, 1], [18, 5, 1], [18, 6, 1], [18, 7, 1], [18, 8, 1], [18, 9, 1], [18, 10, 1], [18, 11, 1], [18, 13, 1], [18, 14, 1], [18, 15, 1], [18, 16, 1], [18, 17, 1]]

atomsXYZ=[[0.049455046079999995, -0.11684347317999999, 0.15115285847999999], [1.41715832786, -0.09888627906, 0.15645259618], [2.16195642312, 0.05035518126, 1.32241394066], [1.43011530016, 0.11899564824, 2.5081412165], [0.0059119989599999995, 0.1258734007, 2.4996769824], [-0.71148145164, 0.03869417078, 1.30629088442], [-0.41136389397999995, 0.14424758866, 3.80921703202], [0.7106776272199999, 0.017909038739999997, 4.63424410708], [0.78900896754, -0.22027011663999999, 5.9342456872], [1.8193684661999998, 0.1687607938, 3.8202858900799996], [2.7709711638199996, -0.00156319772, 4.17988380892], [-0.51240287728, -0.20911394388, -0.7824349643999999], [1.97579036994, -0.13222567742, -0.7817099877999999], [3.2330860657, 0.10908834028, 1.35821614274], [-1.7749543888, 0.14621190482000002, 1.3298399236], [0.00939876598, -0.77834281546, 6.2184523898], [1.6386773093, -0.70869055632, 6.13304167944], [-1.03746903196, -0.6179695246599999, 3.9736173826199996], [-0.87548121298, 1.00870227798, 4.0024100664199995]]

newbonds=fg.GetUniqueBonds(bonds)
print (newbonds)
frag1 = fg.FragmenterBasic(atoms, forces, newbonds, atomsXYZ, breakage_threshold=0.5, breakage_threshold_absolute=False, fragmentation_depth=2, Group_Atom_Numbers=True)

frag1.SortResults(Ascending=False);
print(frag1.Fragments)

