import pickle

with open('certificated_stock_dic.pickle', 'rb') as f:
    certificated_stock_dic = pickle.load(f)

print(certificated_stock_dic)