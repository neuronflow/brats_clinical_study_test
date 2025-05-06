from tqdm import tqdm
from auxiliary.turbopath.turbopath import turbopath

from brats import AdultGliomaSegmenter
from brats.constants import AdultGliomaAlgorithms


from brats import MetastasesSegmenter
from brats.constants import MetastasesAlgorithms


def segmentation_wrapper(
    preprocessed_folder: str,
):
    preprocessed_folder = turbopath(preprocessed_folder)

    patients = preprocessed_folder.dirs()
    for patient in tqdm(patients):
        print("segmenting patient: ", patient)
        segment_patient(
            patient_folder=patient,
        )


def segment_patient(patient_folder: str):
    glio_segmenter = AdultGliomaSegmenter(
        algorithm=AdultGliomaAlgorithms.BraTS23_1,
        cuda_devices="0",
    )
    # these parameters are optional, by default the winning algorithm will be used on cuda:0
    glio_segmenter.infer_single(
        t1c=patient_folder / "t1c_bet_normalized.nii.gz",
        t1n=patient_folder / "t1_bet_normalized.nii.gz",
        t2f=patient_folder / "t2_bet_normalized.nii.gz",
        t2w=patient_folder / "fla_bet_normalized.nii.gz",
        output_file=patient_folder / "segmentations/glioma_2023_1.nii.gz",
        log_file=patient_folder / "segmentations/glioma_2023_1.log",
    )

    met_segmenter = MetastasesSegmenter(
        algorithm=MetastasesAlgorithms.BraTS23_1,
        cuda_devices="0",
    )
    # these parameters are optional, by default the winning algorithm will be used on cuda:0
    met_segmenter.infer_single(
        t1c=patient_folder / "t1c_bet_normalized.nii.gz",
        t1n=patient_folder / "t1_bet_normalized.nii.gz",
        t2f=patient_folder / "t2_bet_normalized.nii.gz",
        t2w=patient_folder / "fla_bet_normalized.nii.gz",
        output_file=patient_folder / "segmentations/metastasis_2023_1.nii.gz",
        log_file=patient_folder / "segmentations/metastasis_2023_1.log",
    )


if __name__ == "__main__":
    segmentation_wrapper(
        preprocessed_folder="/media/anton/DATA_112024/EPITOME_112024/NIFTI_preproc_1122024",
    )
