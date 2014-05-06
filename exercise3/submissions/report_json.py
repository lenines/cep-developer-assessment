import numpy as np
import pandas as pd

mean_path='C:/unc/cep-developer-assessment/exercise3/input/%s.csv'%'mean'
pct_path='C:/unc/cep-developer-assessment/exercise3/input/%s.csv'%'pct'
stats_path='C:/unc/cep-developer-assessment/exercise3/input/%s.csv'%'stats'

mean_bars=pd.read_csv(mean_path)
pct_bars=pd.read_csv(pct_path)
stats_bars=pd.read_csv(stats_path)

dict_mean=dict(mean_bars.ix[8])
dict_pct=dict(pct_bars.ix[8])
dict_stats={
				"fldimp":list(stats_bars.fldimp)[-5:],
				"undrfld":list(stats_bars.undrfld)[-5:],
				"advknow":list(stats_bars.advknow)[-5:],
				"pubpol":list(stats_bars.pubpol)[-5:],
				"comimp":list(stats_bars.comimp)[-5:],
				"undrwr":list(stats_bars.undrwr)[-5:],
				"undrsoc":list(stats_bars.undrsoc)[-5:],
				"orgimp":list(stats_bars.orgimp)[-5:],
				"impsust":list(stats_bars.impsust)[-5:]
			}
elements={}
for k,v in  dict_stats.items():
	elem={"type":"percentileChart"}
	elem["absolutes"]=v
	current={"name": "2014"}
	current["value"]=dict_mean[k]
	current["percentage"]=dict_pct[k]
	elem["current"]=current
	elem["cohorts"]=[]
	elem["past_results"]=[]
	elem["segmentations"]=[]
	elements[k]=elem

df=pd.DataFrame(elements)
df.to_json(date_format='utf-8')