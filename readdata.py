import pandas as pd

data = pd.read_csv('1.txt', sep=",", header=None)
data.columns = ["A", "M", "S", "L_e","N_t","P_r","N_b","B_i","B_ii","Nu"]


for i, item in  enumerate(data['Nu']):
    data['Nu'].iloc[i] = float(str(item).replace("HFloat("," ").replace(")",""))

print(data.head())

data.to_csv('1.csv', sep=',')
