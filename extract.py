f = open('data.csv', 'r')

f.readline()






line = f.readline().rstrip('\r\n')
data_list = line.split('|')
sql = "INSERT INTO ohapp_photos VALUES("

for i in range(0, len(data_list)):
	if i > 1:
		sql = sql + '\''
	sql = sql + data_list[i]

	if i > 1:
		sql = sql + '\''
	if i != len(data_list) - 1:
		sql += ', '

sql += ');'

print sql

f2 = open('insert3.sql', 'w')
f2.write(sql)