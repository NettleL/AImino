NOTE ON REQUIREMENTS
This project contains large files tracked using git lfs (http://git-lfs.com/)

Git LFS must be installed on the machine before cloning the repo.

1. Download & install Git LFS
2. Clone Repo
3. git lfs install
4. cd repository_folder (navigate to cloned repository)
5. git lfs pull (to download the actual file)

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