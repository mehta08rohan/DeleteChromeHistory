import sqlite3
import re


con = sqlite3.connect('C:/Users/mehta/AppData/Local/Google/Chrome/User Data/Default/History')
print('Connection Done!')
cur = con.cursor()
keyword = str(input("Enter keyword to delete: "))

id = 0
result = True

print('Just outside While')
while result:
	print('Enter While Loop')
	result=False
	ids=[]

	for rows in cur.execute(f"SELECT id,url FROM urls WHERE url LIKE '%{keyword}%'"):
		print('Printing Rows!')
		print(rows)
		# id=row[0]
		# ids.append((id,))

	# con.executemany('DELETE FROM urls WHERE id=?',ids)

	# con.commit()
con.close()