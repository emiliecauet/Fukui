# -*- coding: utf-8 -*-
"""
Created on Thu May 12 15:36:31 2016

@author: ecauet
"""
#import visit_utils
#import sys
#from visit_utils import *
#eleteAllPlots()
#OpenDatabase("localhost:/Users/ecauet/Documents/METASPACE/Fukui-Model/Py-Files/Files/testvisit.xyz database", 0)
#OpenDatabase("localhost:/Users/ecauet/Documents/METASPACE/Fukui-Model/Py-Files/Files/testvisit.xyz", 0)
#OpenDatabase("/Users/ecauet/Documents/METASPACE/Fukui-Model/Py-Files/Files/testvisit", 0, "XYZ 1.0") 

# PLOT MOLECULE
AddPlot("Molecule", "element", 1, 1)
DrawPlots()

# CONTROL ANNOTATION 3D (Bounding Box, Axes, ...)
AnnotationAtts = AnnotationAttributes()
AnnotationAtts.axes2D.visible = 1
AnnotationAtts.axes2D.autoSetTicks = 1
AnnotationAtts.axes2D.autoSetScaling = 1
AnnotationAtts.axes2D.lineWidth = 0
AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
AnnotationAtts.axes2D.xAxis.title.visible = 1
AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.title.font.scale = 1
AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.title.font.bold = 1
AnnotationAtts.axes2D.xAxis.title.font.italic = 1
AnnotationAtts.axes2D.xAxis.title.userTitle = 0
AnnotationAtts.axes2D.xAxis.title.userUnits = 0
AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes2D.xAxis.title.units = ""
AnnotationAtts.axes2D.xAxis.label.visible = 1
AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.label.font.scale = 1
AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.label.font.bold = 1
AnnotationAtts.axes2D.xAxis.label.font.italic = 1
AnnotationAtts.axes2D.xAxis.label.scaling = 0
AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.xAxis.grid = 0
AnnotationAtts.axes2D.yAxis.title.visible = 1
AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.title.font.scale = 1
AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.title.font.bold = 1
AnnotationAtts.axes2D.yAxis.title.font.italic = 1
AnnotationAtts.axes2D.yAxis.title.userTitle = 0
AnnotationAtts.axes2D.yAxis.title.userUnits = 0
AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes2D.yAxis.title.units = ""
AnnotationAtts.axes2D.yAxis.label.visible = 1
AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.label.font.scale = 1
AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.label.font.bold = 1
AnnotationAtts.axes2D.yAxis.label.font.italic = 1
AnnotationAtts.axes2D.yAxis.label.scaling = 0
AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.yAxis.grid = 0
AnnotationAtts.axes3D.visible = 0
AnnotationAtts.axes3D.autoSetTicks = 1
AnnotationAtts.axes3D.autoSetScaling = 1
AnnotationAtts.axes3D.lineWidth = 0
AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
AnnotationAtts.axes3D.triadFlag = 1
AnnotationAtts.axes3D.bboxFlag = 0
AnnotationAtts.axes3D.xAxis.title.visible = 1
AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.title.font.scale = 1
AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.title.font.bold = 0
AnnotationAtts.axes3D.xAxis.title.font.italic = 0
AnnotationAtts.axes3D.xAxis.title.userTitle = 0
AnnotationAtts.axes3D.xAxis.title.userUnits = 0
AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes3D.xAxis.title.units = ""
AnnotationAtts.axes3D.xAxis.label.visible = 1
AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.label.font.scale = 1
AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.label.font.bold = 0
AnnotationAtts.axes3D.xAxis.label.font.italic = 0
AnnotationAtts.axes3D.xAxis.label.scaling = 0
AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.xAxis.grid = 0
AnnotationAtts.axes3D.yAxis.title.visible = 1
AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.title.font.scale = 1
AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.title.font.bold = 0
AnnotationAtts.axes3D.yAxis.title.font.italic = 0
AnnotationAtts.axes3D.yAxis.title.userTitle = 0
AnnotationAtts.axes3D.yAxis.title.userUnits = 0
AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes3D.yAxis.title.units = ""
AnnotationAtts.axes3D.yAxis.label.visible = 1
AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.label.font.scale = 1
AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.label.font.bold = 0
AnnotationAtts.axes3D.yAxis.label.font.italic = 0
AnnotationAtts.axes3D.yAxis.label.scaling = 0
AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.yAxis.grid = 0
AnnotationAtts.axes3D.zAxis.title.visible = 1
AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.title.font.scale = 1
AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.title.font.bold = 0
AnnotationAtts.axes3D.zAxis.title.font.italic = 0
AnnotationAtts.axes3D.zAxis.title.userTitle = 0
AnnotationAtts.axes3D.zAxis.title.userUnits = 0
AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
AnnotationAtts.axes3D.zAxis.title.units = ""
AnnotationAtts.axes3D.zAxis.label.visible = 1
AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.label.font.scale = 1
AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.label.font.bold = 0
AnnotationAtts.axes3D.zAxis.label.font.italic = 0
AnnotationAtts.axes3D.zAxis.label.scaling = 0
AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.zAxis.grid = 0
AnnotationAtts.axes3D.setBBoxLocation = 0
AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
AnnotationAtts.userInfoFlag = 1
AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.userInfoFont.scale = 1
AnnotationAtts.userInfoFont.useForegroundColor = 1
AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.userInfoFont.bold = 0
AnnotationAtts.userInfoFont.italic = 0
AnnotationAtts.databaseInfoFlag = 1
AnnotationAtts.timeInfoFlag = 1
AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.databaseInfoFont.scale = 1
AnnotationAtts.databaseInfoFont.useForegroundColor = 1
AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.databaseInfoFont.bold = 0
AnnotationAtts.databaseInfoFont.italic = 0
AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
AnnotationAtts.databaseInfoTimeScale = 1
AnnotationAtts.databaseInfoTimeOffset = 0
AnnotationAtts.legendInfoFlag = 1
AnnotationAtts.backgroundColor = (255, 255, 255, 255)
AnnotationAtts.foregroundColor = (0, 0, 0, 255)
AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
AnnotationAtts.backgroundImage = ""
AnnotationAtts.imageRepeatX = 1
AnnotationAtts.imageRepeatY = 1
AnnotationAtts.axesArray.visible = 1
AnnotationAtts.axesArray.ticksVisible = 1
AnnotationAtts.axesArray.autoSetTicks = 1
AnnotationAtts.axesArray.autoSetScaling = 1
AnnotationAtts.axesArray.lineWidth = 0
AnnotationAtts.axesArray.axes.title.visible = 1
AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.title.font.scale = 1
AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.title.font.bold = 0
AnnotationAtts.axesArray.axes.title.font.italic = 0
AnnotationAtts.axesArray.axes.title.userTitle = 0
AnnotationAtts.axesArray.axes.title.userUnits = 0
AnnotationAtts.axesArray.axes.title.title = ""
AnnotationAtts.axesArray.axes.title.units = ""
AnnotationAtts.axesArray.axes.label.visible = 1
AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.label.font.scale = 1
AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.label.font.bold = 0
AnnotationAtts.axesArray.axes.label.font.italic = 0
AnnotationAtts.axesArray.axes.label.scaling = 0
AnnotationAtts.axesArray.axes.tickMarks.visible = 1
AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
AnnotationAtts.axesArray.axes.grid = 0
SetAnnotationAttributes(AnnotationAtts)

# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/ecauet/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.

# MOLECULES PLOTS ATTRIBUTES (Atoms, Bonds, ...)
MoleculeAtts = MoleculeAttributes()
MoleculeAtts.drawAtomsAs = MoleculeAtts.ImposterAtoms  # NoAtoms, SphereAtoms, ImposterAtoms
MoleculeAtts.scaleRadiusBy = MoleculeAtts.Covalent  # Fixed, Covalent, Atomic, Variable
MoleculeAtts.drawBondsAs = MoleculeAtts.CylinderBonds  # NoBonds, LineBonds, CylinderBonds
MoleculeAtts.colorBonds = MoleculeAtts.ColorByAtom  # ColorByAtom, SingleColor
MoleculeAtts.bondSingleColor = (128, 128, 128, 255)
MoleculeAtts.radiusVariable = "default"
MoleculeAtts.radiusScaleFactor = 0.4
MoleculeAtts.radiusFixed = 0.3
MoleculeAtts.atomSphereQuality = MoleculeAtts.Super  # Low, Medium, High, Super
MoleculeAtts.bondCylinderQuality = MoleculeAtts.Medium  # Low, Medium, High, Super
MoleculeAtts.bondRadius = 0.12
MoleculeAtts.bondLineWidth = 0
MoleculeAtts.bondLineStyle = MoleculeAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
MoleculeAtts.elementColorTable = "cpk_jmol"
MoleculeAtts.residueTypeColorTable = "amino_shapely"
MoleculeAtts.residueSequenceColorTable = "Default"
MoleculeAtts.continuousColorTable = "Default"
MoleculeAtts.legendFlag = 1
MoleculeAtts.minFlag = 0
MoleculeAtts.scalarMin = 0
MoleculeAtts.maxFlag = 0
MoleculeAtts.scalarMax = 1
SetPlotOptions(MoleculeAtts)
MoleculeAtts = MoleculeAttributes()
MoleculeAtts.drawAtomsAs = MoleculeAtts.ImposterAtoms  # NoAtoms, SphereAtoms, ImposterAtoms
MoleculeAtts.scaleRadiusBy = MoleculeAtts.Covalent  # Fixed, Covalent, Atomic, Variable
MoleculeAtts.drawBondsAs = MoleculeAtts.CylinderBonds  # NoBonds, LineBonds, CylinderBonds
MoleculeAtts.colorBonds = MoleculeAtts.SingleColor  # ColorByAtom, SingleColor
MoleculeAtts.bondSingleColor = (128, 128, 128, 255)
MoleculeAtts.radiusVariable = "default"
MoleculeAtts.radiusScaleFactor = 0.6
MoleculeAtts.radiusFixed = 0.3
MoleculeAtts.atomSphereQuality = MoleculeAtts.Super  # Low, Medium, High, Super
MoleculeAtts.bondCylinderQuality = MoleculeAtts.Super  # Low, Medium, High, Super
MoleculeAtts.bondRadius = 0.02
MoleculeAtts.bondLineWidth = 0
MoleculeAtts.bondLineStyle = MoleculeAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
MoleculeAtts.elementColorTable = "cpk_jmol"
MoleculeAtts.residueTypeColorTable = "amino_shapely"
MoleculeAtts.residueSequenceColorTable = "Default"
MoleculeAtts.continuousColorTable = "Default"
MoleculeAtts.legendFlag = 1
MoleculeAtts.minFlag = 0
MoleculeAtts.scalarMin = 0
MoleculeAtts.maxFlag = 0
MoleculeAtts.scalarMax = 1
SetPlotOptions(MoleculeAtts)
AddOperator("CreateBonds", 1)
CreateBondsAtts = CreateBondsAttributes()
CreateBondsAtts.elementVariable = "element"
CreateBondsAtts.atomicNumber1 = (1, -1)
CreateBondsAtts.atomicNumber2 = (-1, -1)
CreateBondsAtts.minDist = (0.4, 0.4)
CreateBondsAtts.maxDist = (2.5, 2.9)
CreateBondsAtts.maxBondsClamp = 10
CreateBondsAtts.addPeriodicBonds = 0
CreateBondsAtts.useUnitCellVectors = 1
CreateBondsAtts.periodicInX = 1
CreateBondsAtts.periodicInY = 1
CreateBondsAtts.periodicInZ = 1
CreateBondsAtts.xVector = (1, 0, 0)
CreateBondsAtts.yVector = (0, 1, 0)
CreateBondsAtts.zVector = (0, 0, 1)
SetOperatorOptions(CreateBondsAtts, 1)
CreateBondsAtts = CreateBondsAttributes()
CreateBondsAtts.elementVariable = "element"
CreateBondsAtts.atomicNumber1 = (1, -1)
CreateBondsAtts.atomicNumber2 = (-1, -1)
CreateBondsAtts.minDist = (0.4, 0.4)
CreateBondsAtts.maxDist = (2.5, 2.9)
CreateBondsAtts.maxBondsClamp = 10
CreateBondsAtts.addPeriodicBonds = 0
CreateBondsAtts.useUnitCellVectors = 1
CreateBondsAtts.periodicInX = 1
CreateBondsAtts.periodicInY = 1
CreateBondsAtts.periodicInZ = 1
CreateBondsAtts.xVector = (1, 0, 0)
CreateBondsAtts.yVector = (0, 1, 0)
CreateBondsAtts.zVector = (0, 0, 1)
SetOperatorOptions(CreateBondsAtts, 1)
DrawPlots()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.143431, 0.907554, 0.394682)
View3DAtts.focus = (1.37773, -0.575969, 5.13627)
View3DAtts.viewUp = (0.77778, 0.349971, -0.522091)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 8.18216
View3DAtts.nearPlane = -16.3643
View3DAtts.farPlane = 16.3643
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (1.37773, -0.575969, 5.13627)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.867446, -0.317207, -0.383299)
View3DAtts.focus = (1.37773, -0.575969, 5.13627)
View3DAtts.viewUp = (-0.49738, -0.533836, -0.683837)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 8.18216
View3DAtts.nearPlane = -16.3643
View3DAtts.farPlane = 16.3643
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (1.37773, -0.575969, 5.13627)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

# VECTORS PLOT ATTRIBUTES
DefineVectorExpression("Force3", "{var0, var1, var2}")
AddPlot("Vector", "Force3", 1, 1)
DrawPlots()
VectorAtts = VectorAttributes()
VectorAtts.glyphLocation = VectorAtts.AdaptsToMeshResolution  # AdaptsToMeshResolution, UniformInSpace
VectorAtts.useStride = 0
VectorAtts.stride = 1
VectorAtts.nVectors = 400
VectorAtts.lineStyle = VectorAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
VectorAtts.lineWidth = 0
VectorAtts.scale = 0.7
VectorAtts.scaleByMagnitude = 1
VectorAtts.autoScale = 1
VectorAtts.headSize = 0.25
VectorAtts.headOn = 1
VectorAtts.colorByMag = 1
VectorAtts.useLegend = 1
VectorAtts.vectorColor = (0, 0, 0, 255)
VectorAtts.colorTableName = "Default"
VectorAtts.invertColorTable = 0
VectorAtts.vectorOrigin = VectorAtts.Tail  # Head, Middle, Tail
VectorAtts.minFlag = 0
VectorAtts.maxFlag = 0
VectorAtts.limitsMode = VectorAtts.OriginalData  # OriginalData, CurrentPlot
VectorAtts.min = 0
VectorAtts.max = 1
VectorAtts.lineStem = VectorAtts.Cylinder  # Cylinder, Line
VectorAtts.geometryQuality = VectorAtts.High  # Fast, High
VectorAtts.stemWidth = 0.10
VectorAtts.origOnly = 1
VectorAtts.glyphType = VectorAtts.Arrow  # Arrow, Ellipsoid
SetPlotOptions(VectorAtts)

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0459054, -0.946, -0.320899)
View3DAtts.focus = (1.37773, -0.575969, 5.13627)
View3DAtts.viewUp = (-0.982478, 0.0153322, -0.185745)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 8.18216
View3DAtts.nearPlane = -16.3643
View3DAtts.farPlane = 16.3643
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (1.37773, -0.575969, 5.13627)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.0991466, -0.980796, -0.167958)
View3DAtts.focus = (1.37773, -0.575969, 5.13627)
View3DAtts.viewUp = (-0.990836, -0.112868, 0.0742002)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 8.18216
View3DAtts.nearPlane = -16.3643
View3DAtts.farPlane = 16.3643
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (1.37773, -0.575969, 5.13627)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

figure = SaveWindowAttributes()
figure.family = 0
figure.format = figure.PNG
figure.width = 1024
figure.height = 1024