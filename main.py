import pymssql

try:
    conn = pymssql.connect(host='localhost', port='1433', user='sa', password='QWEASdzxc#123#', database='firstDB')
    print("Work")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dbo.firstDB")
    row = cursor.fetchone()
    while row:
        print("Имя: %s,Статус: %s" % (row[0],row[1]))        
        row = cursor.fetchone()
    conn.close() 
except (Exception, pymssql.DatabaseError) as error:
    print(error)