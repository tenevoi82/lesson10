import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()


#
data.loc[:,['robot','human']] = 0
data.loc[data['whoAmI'] == 'robot','robot'] = 1
data.loc[data['whoAmI'] == 'human','human'] = 1
data[data.columns[1:]]
