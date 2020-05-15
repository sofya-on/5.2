## Copyright (C) 2020 Olga Chernova

#GNU Octave, version 5.2.0
#Copyright (C) 2020 John W. Eaton and others.
#This is free software; see the source code for copying conditions.
#There is ABSOLUTELY NO WARRANTY; not even for MERCHANTABILITY or
#FITNESS FOR A PARTICULAR PURPOSE.  For details, type 'warranty'.

#Octave was configured for "x86_64-w64-mingw32".

function retval = L4N1 (matrix1, matrix2)
  size1 = size(matrix1);
  size2 = size(matrix2);
 
  if (!(size1(1) <= 2 && size1(2) <= 2 &&size2(1) <=2 && size2(2) <=2))
    MA1_1 = matrix1(1:floor(size1(1)/2), 1:floor(size1(2)/2));
    MA1_2 = matrix1(1:floor(size1(1)/2), floor(size1(2)/2)+1:size1(2));
    MA2_1 = matrix1(floor(size1(1)/2)+1:size1(1), 1:floor(size1(2)/2));
    MA2_2 = matrix1(floor(size1(1)/2)+1:size1(1), floor(size1(2)/2)+1:size1(2));
    
    MB1_1 = matrix2(1:floor(size2(1)/2), 1:floor(size2(2)/2));
    MB1_2 = matrix2(1:floor(size2(1)/2), floor(size2(2)/2)+1:size2(2));
    MB2_1 = matrix2(floor(size2(1)/2)+1:size2(1), 1:floor(size2(2)/2));
    MB2_2 = matrix2(floor(size2(1)/2)+1:size2(1), floor(size2(2)/2)+1:size2(2));
    
    matrixrez1_1 = L4N1(MA1_1, MB1_1)+ L4N1(MA1_2,MB2_1);
    matrixrez1_2 = L4N1(MA1_1,MB1_2) + L4N1(MA1_2, MB2_2);
    matrixrez2_1 = L4N1(MA2_1,MB1_1)+L4N1(MA2_2,MB2_1);
    matrixrez2_2 = L4N1(MA2_1,MB1_2) +L4N1(MA2_2,MB2_2);  
    tmp1 = [matrixrez1_1,matrixrez1_2];
    tmp2 = [matrixrez2_1,matrixrez2_2];
    retval = [tmp1; tmp2];
  else 
    retval = matrix1*matrix2;
  
  endif
  
endfunction
