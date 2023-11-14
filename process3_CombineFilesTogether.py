import pandas as pd
from process1_ManipulateData import manipulate_data
from process2_VerifyDataStructure import verify_data_structure


def combine_files_together(csv_dict):
    combine_data = pd.DataFrame()
    for csv_file, position in csv_dict.items():
        if verify_data_structure(csv_file):
            temp = manipulate_data(csv_file, position)
            pd.DataFrame(temp)
            combine_data = pd.concat([combine_data, temp])
        else:
            print(csv_file + 'has the wrong format!')

    newly_dataframe = combine_data.reset_index(drop=True, col_level=1)
    return newly_dataframe
