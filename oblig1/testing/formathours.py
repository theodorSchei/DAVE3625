def formathours(hour):
	out = ''
	stringhour = str(hour)
	
	if len(stringhour) > 1:
		out += stringhour + ':00'
	else:
		out += '0' + stringhour + ':00'
	
	return out

for i in range(0,24):
	print(formathours(i))


def row_getMonth(row):
	try:
		monthRaw = row
		month = monthRaw.split('/')[1]
	except:
		month = 0

	return month        


print(row_getMonth('10/11/2012'))