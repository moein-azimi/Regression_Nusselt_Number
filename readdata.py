import pandas as pd

data = pd.read_csv('jadid2.txt', sep=",", header=None)
data.columns = ["A", "M", "S", "L_e","N_t","P_r","N_b","B_i","B_ii","Nu"]

print(data.describe())

data.to_csv('1.csv', sep=',')