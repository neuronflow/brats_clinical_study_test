from auxiliary.turbopath.turbopath import turbopath
from tqdm import tqdm


from brainles_preprocessing.modality import Modality, CenterModality
from brainles_preprocessing.normalization.percentile_normalizer import (
    PercentileNormalizer,
)
from brainles_preprocessing.preprocessor import Preprocessor


def preprocessing_wrapper(
    source_folder: str,
    output_folder: str,
):
    source_folder = turbopath(source_folder)
    output_folder = turbopath(output_folder)

    patients = source_folder.dirs()
    for patient in tqdm(patients):
        print("preprocessing patient: ", patient)
        preprocess_patient(
            patient_folder=patient,
            prep_folder=output_folder / patient.name,
        )


def preprocess_patient(
    patient_folder: str,
    prep_folder: str,
):
    btk_raw_folder = patient_folder / patient_folder.name + "_btk_RAW"

    # specify a normalizer
    percentile_normalizer = PercentileNormalizer(
        lower_percentile=0.1,
        upper_percentile=99.9,
        lower_limit=0,
        upper_limit=1,
    )
    try:
        t1c_file = btk_raw_folder.files("*_t1c.nii.gz")[0]
        t1_file = btk_raw_folder.files("*_t1.nii.gz")[0]
        t2_file = btk_raw_folder.files("*_t2.nii.gz")[0]
        fla_file = btk_raw_folder.files("*_fla.nii.gz")[0]

        # define center and moving modalities
        center = CenterModality(
            modality_name="t1c",
            input_path=t1c_file,
            normalizer=percentile_normalizer,
            # specify the output paths for the raw and normalized images of each step - here only for atlas registered and brain extraction
            normalized_skull_output_path=prep_folder / "t1c_skull_normalized.nii.gz",
            normalized_bet_output_path=prep_folder / "t1c_bet_normalized.nii.gz",
            # specify output paths for the brain extraction and defacing masks
            bet_mask_output_path=prep_folder / "masks/t1c_bet_mask.nii.gz",
        )

        moving_modalities = [
            Modality(
                modality_name="t1",
                input_path=t1_file,
                normalizer=percentile_normalizer,
                # specify the output paths for the raw and normalized images of each step - here only for atlas registered and brain extraction
                normalized_skull_output_path=prep_folder / "t1_skull_normalized.nii.gz",
                normalized_bet_output_path=prep_folder / "t1_bet_normalized.nii.gz",
            ),
            Modality(
                modality_name="t2",
                input_path=t2_file,
                normalizer=percentile_normalizer,
                # specify the output paths for the raw and normalized images of each step - here only for atlas registered and brain extraction
                normalized_skull_output_path=prep_folder / "t2_skull_normalized.nii.gz",
                normalized_bet_output_path=prep_folder / "t2_bet_normalized.nii.gz",
            ),
            Modality(
                modality_name="fla",
                input_path=fla_file,
                normalizer=percentile_normalizer,
                # specify the output paths for the raw and normalized images of each step - here only for atlas registered and brain extraction
                normalized_skull_output_path=prep_folder
                / "fla_skull_normalized.nii.gz",
                normalized_bet_output_path=prep_folder / "fla_bet_normalized.nii.gz",
            ),
        ]

        # instantiate and run the preprocessor using defaults for registration/ brain extraction/ defacing backends
        preprocessor = Preprocessor(
            center_modality=center,
            moving_modalities=moving_modalities,
        )

        preprocessor.run()
    except:
        print("Patient not processed")


if __name__ == "__main__":
    preprocessing_wrapper(
        source_folder="/media/anton/DATA_112024/EPITOME_112024/Metastasen_Nifti",
        output_folder="/media/anton/DATA_112024/EPITOME_112024/NIFTI_preproc_1122024",
    )
