import subprocess
# WSL DEPENDENCY!!!
# HHSUITE DEPENDENCY!!!

def hmm(input_file):
    linux_input_file = input_file.replace("\\", "/").replace("C:/", "/mnt/c/")
    output_file = linux_input_file.replace(".afa", ".hhm")
    
    wsl_command = f'wsl hhmake -i "{linux_input_file}" -o "{output_file}" -M first'
    #NOTE: Must wrap {linux_input_file} and {output_file} with "" to prevent any issues due to spaces in file path (Year 12)
    
    result = subprocess.run(wsl_command, shell=True,capture_output=True, text=True)
    
    if result.returncode ==0:
        print('Conversion Successful!')
    else:
        print('Error in conversion:', result.stderr)

hmm(r"C:\Users\nethy\OneDrive\Documents\Nethya\School\Year_12\12SE\6-Nethya-Liyanage\SE_Project_Nethya_Liyanage\tar_folder\VQPPEgQjjsEE__0\VQPPEgQjjsEE__0_resulthhs.afa")