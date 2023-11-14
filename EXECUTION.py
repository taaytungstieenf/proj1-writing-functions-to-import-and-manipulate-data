from process3_CombineFilesTogether import combine_files_together
from process5_AnalyzeData import analyze_data

root = 'D:/Career Track 1 - DATA ENGINEER/SOFTWARE. JetBrains PyCharm/PROJ1 - Writing Functions for Product Analysis/data'

gk_csv = f'{root}/goalkeeper.csv'
df_csv = f'{root}/defender.csv'
mf_csv = f'{root}/midfielder.csv'
at_csv = f'{root}/attacker.csv'

dict_test = {gk_csv: 'GK', df_csv: 'DF', mf_csv: 'MF', at_csv: 'AT'}

dataframe = combine_files_together(dict_test)
A, B, C = analyze_data(dataframe)

print(dataframe)
print('Percentage of elite players: {}%'.format(A))
print('Percentage of good players: {}%'.format(B))
print('Percentage of average players: {}%'.format(C))
