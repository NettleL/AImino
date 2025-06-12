NOTE ON REQUIREMENTS

This project contains large files tracked using git lfs (http://git-lfs.com/)

see https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage for info

Git LFS must be installed on the machine before cloning the repo.

1. Download & install Git LFS
2. Clone Repo (git clone https://github.com/NettleL/AImino.git )
3. Initialise Git LFS (git lfs install)
4. navigate to cloned repository (cd repository_folder)
5. download the actual file (git lfs pull)

Pip installing
- flask
- torch
- matplotlib
will provide all libraries necessary
 
Alternatively, requirements can be installed through "pip install -r requirements.txt"

NOTE ON MISC

/preprocessing_training_data is not required for the program to function - it merely documents how the preprocessing of training data was executed so the program can be replicated

/preprocessing_user_input is not required for the program to function - it contains misc. pieces of code I previously thought were useful but later learned I did not need. However, I was reluctant to delete them - I thought they may be useful to the user.

/training is not required for the program to function - this just contains the code used to train the model so it can be replicated.