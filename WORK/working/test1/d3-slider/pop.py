import pandas as pd 
import json

fname = "data/pop_history_simple"
fname_out = "data/pop_year.json"

cols: = ['com_id', 'name', '1930', '1940', '1950',
         '1960', '1970', '1980', '1990','2000','2010']

df = pd.read_csv(fname,names=cols, header=0 )
print df.shape

dict_json ={}
dict_json["1930"]= {}


dfg = df.groupby
