from scipy.stats import percentileofscore

def percentile(rating_list):
	percentile_list = []
	for r in rating_list:
	    percentile = percentileofscore(rating_list, r, kind='mean')
	    percentile_list.append(percentile)
	return percentile_list