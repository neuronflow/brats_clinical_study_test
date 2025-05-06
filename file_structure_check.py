from auxiliary.turbopath.turbopath import turbopath
from tqdm import tqdm
import os


def delete_hidden_files(folder_path):
    """
    Deletes all hidden files (starting with a dot) in the specified folder.
    """
    for file in folder_path.files():
        if file.name.startswith('.'):
            try:
                os.remove(file)
                print(f"Deleted hidden file: {file}")
            except Exception as e:
                print(f"Failed to delete {file}: {e}")


def inspection_wrapper(
    source_folder: str,
):
    source_folder = turbopath(source_folder)

    patients = source_folder.dirs()
    success_patients = []
    fail_patients = []
    for patient in tqdm(patients):
        # print("preprocessing patient: ", patient)
        success = inspect_patient(
            patient_folder=patient,
        )
        if success:
            success_patients.append(patient)
        else:
            fail_patients.append(patient)
    print("************************************")
    print("Patients fine: ", len(success_patients))
    print("Patients not fine: ", len(fail_patients))
    print("************************************")


def inspect_patient(
    patient_folder: str,
):
    try:   
        btk_raw_folder = patient_folder / patient_folder.name + "_btk_RAW"

        # Delete hidden files before proceeding
        delete_hidden_files(btk_raw_folder)

        t1c_file_list = btk_raw_folder.files("*_t1c.nii.gz")
        t1_file_list = btk_raw_folder.files("*_t1.nii.gz")
        t2_file_list = btk_raw_folder.files("*_t2.nii.gz")
        fla_file_list = btk_raw_folder.files("*_fla.nii.gz")
    except:
        print("************************************")
        print("Patient not fine: ", patient_folder.name)
        print(
            f"Error: Could not find the btk raw folder for patient {patient_folder.name}"
        )
        print("************************************")
        return
    
    success={"t1c": False, "t1": False, "t2": False, "fla": False,}
        
        
    if len(t1c_file_list) != 1:
        print(
                f"Expected exactly one t1c file, but found {len(t1c_file_list)} !"
            )
    else:
        print(
                f"Expected exactly one t1c file and found {len(t1c_file_list)}"
            )
        success["t1c"] = True
    if len(t1_file_list) != 1:
        print(
                f"Expected exactly one t1 file, but found {len(t1_file_list)} !"
            )
    else:
        print(
                f"Expected exactly one t1 file and found {len(t1_file_list)}"
            )
        success["t1"] = True
        
    if len(t2_file_list) != 1:
        print(
                f"Expected exactly one t2 file, but found {len(t2_file_list)} !"
                )
    else:
        print(
                f"Expected exactly one t2 file and found {len(t2_file_list)}"
            )
        success["t2"] = True
        
    if len(fla_file_list) != 1:
            print(
                f"Expected exactly one fla file, but found {len(fla_file_list)} !"
            )
    else:
        print(
                f"Expected exactly one fla file and found {len(fla_file_list)}"
            )
        success["fla"] = True
    if all(success.values()):
        print("************************************")
        print("Patient fine: ", patient_folder.name)
        print("************************************")
        return True
    else:
        print("************************************")
        print("Patient not fine: ", patient_folder.name)
        print("please check btk raw folder:")
        print(btk_raw_folder)
        print("************************************")
        return False


        

if __name__ == "__main__":
    inspection_wrapper(
        source_folder="/home/anton/Desktop/EPITOME/epitome/GBM_01_2025_nifti",
    )
