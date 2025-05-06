# EPITOME - Epilepsy Prediction In Tumorpatients using MachinE learning
use a Python 3.10 virtual environment

## dcm2niix
https://github.com/rordenlab/dcm2niix

### naming flags
%b=basename, %c=comments, %d=description, %e=echo number, %f=folder name, %g=accession number, %i=ID of patient, %j=seriesInstanceUID, %k=studyInstanceUID, %m=manufacturer, %n=name of patient, %o=mediaObjectInstanceUID, %p=protocol, %r=instance number, %s=series number, %t=time, %u=acquisition number, %v=vendor, %x=study ID; %z=sequence name; default '%f_%p_%t_%s')


## modsort
https://syncandshare.lrz.de/getlink/fi7E1ZNFXdmfFmweXhagdh/

## itk snap:
http://www.itksnap.org/download/snap/process.php?link=16120&root=nitrc

http://www.itksnap.org/pmwiki/pmwiki.php?n=Documentation.TutorialSectionInstallation


### docker post install instructions
https://docs.docker.com/engine/install/linux-postinstall/

### init development
1. generate ssh key:
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux

2. add to github:
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?platform=linux&tool=webui

3. clone the repo:
```git clone git@github.com:neuronflow/epitome.git```



## "cooking recipe"
1. nifti-conversion
2. preprocessing (co-registration, skull stripping, normalization etc.)
3. optional: synthesize missing sequences
4. generate segmentations
5. optional: fuse segmentations


## atlas: SRI-24
https://www.nitrc.org/projects/sri24/