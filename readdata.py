import pandas as pd


file1 = open('1.txt', 'r')
Lines = file1.readlines()
A = []
for line in Lines:
    A.append(line)
B = []
C = []
for i in range(len(A)):
    A[i] = A[i].replace('\n','').replace(' ','')
    if A[i] != '':
        if A[i].startswith('H'):
            B.append(A[i-2]+A[i])
        else:
            if A[i].endswith(')'):        
                B.append(A[i])

textfile = open("a_file.txt", "w")
for element in B:
    textfile. write(element + "\n")
textfile. close()

data = pd.read_csv('a_file.txt', sep=",", header=None)
data.columns = ["A", "M", "S", "L_e","N_t","P_r","N_b","B_i","B_ii","Nu"]


for i, item in  enumerate(data['Nu']):
    data['Nu'].iloc[i] = str(item).replace('\nHFloat(',' ').replace("HFloat("," ").replace(")","")

print(data.head())

data.to_csv('1.csv', sep=',')
