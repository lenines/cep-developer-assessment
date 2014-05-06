import numpy as np
import pandas as pd
from helpers import percentile

temp='C:/unc/cep-developer-assessment/exercise2/input/%s.csv'%'mean'
mean_bars=pd.read_csv(temp)

df=pd.DataFrame(
	{
		"fdntext":mean_bars.fdntext,
		"fldimp":percentile(mean_bars.fldimp),
		"undrfld":percentile(mean_bars.undrfld),
		"advknow":percentile(mean_bars.advknow),
		"pubpol":percentile(mean_bars.pubpol),
		"comimp":percentile(mean_bars.comimp),
		"undrwr":percentile(mean_bars.undrwr),
		"undrsoc":percentile(mean_bars.undrsoc),		
		"orgimp":percentile(mean_bars.orgimp),
		"impsust":percentile(mean_bars.impsust)
	},columns=["fdntext",
		"fldimp",
		"undrfld",
		"advknow",
		"pubpol",
		"comimp",
		"undrwr",
		"undrsoc",		
		"orgimp",
		"impsust"])

df.to_csv('C:/unc/cep-developer-assessment/exercise2/output/%s.csv'%'pct',sep='\t', encoding='utf-8')