import numpy as np
import pandas as pd
temp='C:/unc/cep-developer-assessment/exercise1/input/%s.csv'%'xl'
xl_bars=pd.read_csv(temp)
df=pd.DataFrame(
	{"fdntext":xl_bars.fdntext,
	"fldimp":xl_bars.fldimp,
	"undrfld":xl_bars.undrfld,
	"advknow":xl_bars.advknow,
	"pubpol":xl_bars.pubpol,
	"comimp":xl_bars.comimp,
	"undrwr":xl_bars.undrwr,
	"undrsoc":xl_bars.undrsoc,
	"orgimp":xl_bars.orgimp,
	"impsust":xl_bars.impsust},columns=["fdntext",
		"fldimp",
		"undrfld",
		"advknow",
		"pubpol",
		"comimp",
		"undrwr",
		"undrsoc",		
		"orgimp",
		"impsust"])
df=df.replace('NaN',0).replace('77',0).replace('88',0)
mean=df.groupby('fdntext').mean()
mean.to_csv('C:/unc/cep-developer-assessment/exercise1/output/%s.csv'%'mean.csv', sep='\t', encoding='utf-8')


means=mean.describe()
means.to_csv('C:/unc/cep-developer-assessment/exercise1/output/%s.csv'%'stats.csv', sep='\t', encoding='utf-8')