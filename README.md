# BraTS clinical test

## installation
1. use a Python 3.10/3.11/3.12 virtual environment
2. `pip install -r requirements.txt`

Look at `main.py` and adjust it as necessary

## dcm2niix
https://github.com/rordenlab/dcm2niix

### naming flags
%b=basename, %c=comments, %d=description, %e=echo number, %f=folder name, %g=accession number, %i=ID of patient, %j=seriesInstanceUID, %k=studyInstanceUID, %m=manufacturer, %n=name of patient, %o=mediaObjectInstanceUID, %p=protocol, %r=instance number, %s=series number, %t=time, %u=acquisition number, %v=vendor, %x=study ID; %z=sequence name; default '%f_%p_%t_%s')

as dcm2niix pypi installation is broken (see https://github.com/rordenlab/dcm2niix/issues/931 ) we call the binary file with a subprocess
