from process3_CombineFilesTogether import combine_files_together
from process5_AnalyzeData import analyze_data


class ImportAndManipulateData:
    def __init__(self, gk_file, df_file, mf_file, at_file):
        self.c = None
        self.b = None
        self.a = None
        self.gk = gk_file
        self.df = df_file
        self.mf = mf_file
        self.at = at_file

    def execute(self):
        dict_test = {self.gk: 'GK', self.df: 'DF', self.mf: 'MF', self.at: 'AT'}
        dataframe = combine_files_together(dict_test)
        self.a, self.b, self.c = analyze_data(dataframe)

        print(dataframe)
        print('A. Percentage of elite  players: {}%'.format(self.a))
        print('B. Percentage of solid  players: {}%'.format(self.b))
        print('C. Percentage of casual players: {}%'.format(self.c))


root = '/home/tae/PycharmProjects/prj1-Writing-Function-to-Import-and-Manipulate-Data/data'

gk_csv = f'{root}/best_GK.csv'
df_csv = f'{root}/best_DF.csv'
mf_csv = f'{root}/best_MF.csv'
at_csv = f'{root}/best_AT.csv'

obj = ImportAndManipulateData(gk_csv, df_csv, mf_csv, at_csv)
obj.execute()
