import operator
import pandas as pd
from collections import Counter
df = pd.read_table('Brightkite_totalCheckins.txt', delim_whitespace=True, header=None)
target = df.iloc[:,-1].tolist()
print(len(target))
a = dict(Counter(target))
sorted_a = sorted(a.items(), key=operator.itemgetter(1))  
print(sorted_a)
