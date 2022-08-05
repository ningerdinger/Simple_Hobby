import cbsodata
import pandas as pd
tables = cbsodata.get_table_list()
# print(tables)

# for item in tables:
    # print(item['Identifier'])
data = cbsodata.get_data('80072NED')
print(data)
# for id in data:
#     print(id)

df = pd.DataFrame(data)
print(df)
print(df.columns)