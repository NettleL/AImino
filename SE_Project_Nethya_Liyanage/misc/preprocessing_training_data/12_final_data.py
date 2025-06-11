import torch
import os

folder_path = r"C:\Users\cgwl\Documents\AImino_Training\training_data\rnn_data_batches"
final_dict = {}

count = 0
for file in os.listdir(folder_path):
    model_path = os.path.join(folder_path, file)

    state_dict = torch.load(model_path, weights_only=False)  # data container
    final_dict.update(state_dict)
    
    count = count + 1
    print(f'batch {count}. merged')


save_path = r"C:\Users\cgwl\Documents\AImino_Training\final_dataset.pt"
torch.save(final_dict, save_path)


