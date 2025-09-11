#!/bin/bash

cp xx03 xx03_Import.cpp
cp xx04 xx04_Motioncorr.cpp
cp xx05 xx05_Ctffind.cpp
cp xx06 xx06_Manualpick.cpp
cp xx07 xx07_Autopick.cpp
cp xx08 xx08_Extract.cpp
cp xx09 xx01_Select.cpp
cp xx10 xx10_Class2D.cpp
cp xx11 xx11_Inimodel.cpp
cp xx12 xx12_Class3D.cpp
cp xx13 xx13_Autorefine.cpp
cp xx14 xx14_MultiBody.cpp
cp xx15 xx15_Maskcreate.cpp
cp xx16 xx16_Joinstar.cpp
cp xx17 xx17_Subtract.cpp
cp xx18 xx18_Postprocess.cpp
cp xx19 xx19_Localres.cpp
cp xx20 xx20_DynaMight.cpp
cp xx21 xx21_ModelAngelo.cpp
cp xx22 xx22_Motionrefine.cpp
cp xx23 xx23_Ctfrefine.cpp
cp xx24 xx24_External.cpp

sed -e "s/\tjoboptions\[\"//g" xx03_Import.cpp > tmp
sed "s/\"\] = JobOption(/,/g" tmp > tst.csv
