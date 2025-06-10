Git LFS must be installed on the machine before cloning the repo.

The actual file must be downloaded via: git lfs pull

Note
/preprocessing_training_data is not required for the program to function - it merely documents how the preprocessing of training data was executed so the program can be replicated

/preprocessing_user_input is not required for the program to function - it contains misc. pieces of code I previously thought were useful but later learned I did not need. However, I was reluctant to delete them - I thought they may be useful to the user.

/training is not required for the program to function - this just contains the code used to train the model so it can be replicated.

Note on AImino
I believed training the model would take significantly longer than it actually did (multiple days) and thus I wouldn't be able to train my model multiple times. Therefore I opted for a semi-waterfall approach - determining the full architecture of the model before training it instead of training submodules to determine the effectiveness 

However, due to Kaggle GPU accelerators, full training took an hour, and single epoch training fifteen minutes, and thus I was able to train the model on single epochs multiple times to determine effectiveness

Due to my belief I would only be able to train the model once, my model architecture contains a large amount of modules - I kept adding modules to try to compensate for the flaws of RNN (sequential) predicting distance maps (not sequential) (I couldn't use CNN because it requires pairwise data l x l, which is quadratically larger) - and because I didn't think I would be able to train the model multiple times I trained all the modules at once

If I could do it again I would opt for a bottom up approach - training on each individual model (15 mins) separately to determine effectiveness. However due to time constraints (I still need to test and debug) I will be leaving it as is, and hope that each individual model significantly improves the accuracy of the RNN

I hope that I have adequately explained why the neural network model has so many modules
