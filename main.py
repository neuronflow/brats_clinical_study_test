from nifti_conversion import niftiConvert

from auxiliary.turbopath import turbopath
from auxiliary.io import read_image
from auxiliary.conversion import nifti_to_dicom_itk

# TODO first we define directories
# DCM sources
T1N_DCM_DIR = turbopath("TODO")
T1C_DCM_DIR = turbopath("TODO")
T2W_DCM_DIR = turbopath("TODO")
T2F_DCM_DIR = turbopath("TODO")

# NII targets
T1N_NII_DIR = turbopath("TODO")
T1C_NII_DIR = turbopath("TODO")
T2W_NII_DIR = turbopath("TODO")
T2F_NII_DIR = turbopath("TODO")


# now we convert all files from the folders to nifti
niftiConvert(input_dir=T1N_DCM_DIR, output_dir=T1N_NII_DIR)
niftiConvert(input_dir=T1C_DCM_DIR, output_dir=T1C_NII_DIR)
niftiConvert(input_dir=T2W_DCM_DIR, output_dir=T2W_NII_DIR)
niftiConvert(input_dir=T2F_DCM_DIR, output_dir=T2F_NII_DIR)

# now we check if only one nifti came out for each conversion
T1N_file_List = T1N_NII_DIR.files("*.nii.gz")
if len(T1N_file_List) != 1:
    raise ValueError(f"Expected exactly one T1N file, but found {len(T1N_file_List)} !")

T1C_file_List = T1C_NII_DIR.files("*.nii.gz")
if len(T1C_file_List) != 1:
    raise ValueError(f"Expected exactly one T1C file, but found {len(T1C_file_List)} !")
T2W_file_List = T2W_NII_DIR.files("*.nii.gz")
if len(T2W_file_List) != 1:
    raise ValueError(f"Expected exactly one T2W file, but found {len(T2W_file_List)} !")
T2F_file_List = T2F_NII_DIR.files("*.nii.gz")
if len(T2F_file_List) != 1:
    raise ValueError(f"Expected exactly one T2F file, but found {len(T2F_file_List)} !")

# define source nifti files in native space
T1N_file = T1N_file_List[0]
T1C_file = T1C_file_List[0]
T2W_file = T2W_file_List[0]
T2F_file = T2F_file_List[0]

# TODO do preprocessing and segmentation magic here

# TODO adjust paths to resulting segmentation files
T1N_NII_segmentation_file = turbopath("TODO")
T1C_NII_segmentation_file = turbopath("TODO")
T2W_NII_segmentation_file = turbopath("TODO")
T2F_NII_segmentation_file = turbopath("TODO")


# now we write the segmentation files to .dcm using the dicom series as reference
T1N_DCM_segmentation_file = turbopath("TODO")
T1C_DCM_segmentation_file = turbopath("TODO")
T2W_DCM_segmentation_file = turbopath("TODO")
T2F_DCM_segmentation_file = turbopath("TODO")


nifti_to_dicom_itk(
    input_file=T1N_NII_segmentation_file,
    output_file=T1N_DCM_segmentation_file,
    reference_dicom_dir=T1N_DCM_DIR,
)
nifti_to_dicom_itk(
    input_file=T1C_NII_segmentation_file,
    output_file=T1C_DCM_segmentation_file,
    reference_dicom_dir=T1C_DCM_DIR,
)
nifti_to_dicom_itk(
    input_file=T2W_NII_segmentation_file,
    output_file=T2W_DCM_segmentation_file,
    reference_dicom_dir=T2W_DCM_DIR,
)
nifti_to_dicom_itk(
    input_file=T2F_NII_segmentation_file,
    output_file=T2F_DCM_segmentation_file,
    reference_dicom_dir=T2F_DCM_DIR,
)
