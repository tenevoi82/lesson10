# Урок 10. Построение графиков
# ** СДАВАТЬ ССЫЛКОЙ НА ВАШ РЕПОЗИТОРИЙ НА ГИТХАБ**
# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?



import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()



# РЕШЕНИЕ


# Добавим две колонки с значением по умолчанию 0 (int)
data.loc[:,['robot','human']] = 0

# заполним колонки 
data.loc[data['whoAmI'] == 'robot','robot'] = 1
data.loc[data['whoAmI'] == 'human','human'] = 1

# отброзим (можно и сохранить) в требемом виде (не показываем первую колонку)
data[data.columns[1:]]
