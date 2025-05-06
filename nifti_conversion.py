# use with a recent release of dcm2niix, e.g. https://github.com/rordenlab/dcm2niix/releases/tag/v1.0.20220720
import datetime
import os
import shlex
import subprocess

from auxiliary.turbopath.turbopath import turbopath
from tqdm import tqdm

import platform


def conversion_wrapper(
    source_folder,
    output_folder,
):
    source_folder = turbopath(source_folder)
    output_folder = turbopath(output_folder)

    patients = source_folder.dirs()
    for patient in tqdm(patients):
        niftiConvert(
            inputDir=patient,
            exportDir=output_folder / patient.name,
        )


def niftiConvert(inputDir, exportDir):
    try:
        print("*** start ***")

        os.makedirs(exportDir, exist_ok=True)

        # create dcm2niix call
        dcm2niixargs = " -d 9 -f %d_%f_%i_%m_%p_%q_%s_%z -z y -o"  # extra metadata args
        # dcm2niixargs = " -f %f -z y -o "
        # dcm2niixargs = "-d 9 -z y -o"

        linux_executable_path = turbopath("dcm2niix_LNX/dcm2niix")
        mac_executable_path = turbopath("dcm2niix_mac/dcm2niix")

        if platform.system() == "Linux":
            executable_path = linux_executable_path
        elif platform.system() == "Darwin":
            executable_path = mac_executable_path
        else:
            raise Exception("Unsupported operating system")

        readableCmd = (
            executable_path + dcm2niixargs + ' "' + exportDir + '" "' + inputDir + '"'
        )

        print(readableCmd)
        command = shlex.split(readableCmd)

        logFilePath = os.path.join(
            exportDir, os.path.basename(exportDir) + "_conversion.log"
        )
        with open(logFilePath, "w") as outFile:
            subprocess.run(command, stdout=outFile, stderr=outFile)

    except Exception as e:
        print("error: " + str(e))
        print("conversion error for:", inputDir)

    time = str(datetime.datetime.now().time())

    print("** finished:", exportDir, "at:", time)


if __name__ == "__main__":
    conversion_wrapper(
        source_folder="/media/anton/DATA_112024/EPITOME_112024/Metastasen_DiCom",
        output_folder="data/nifti",
    )
