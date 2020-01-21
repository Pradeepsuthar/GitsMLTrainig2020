from datamatrix import DataMatrix
data = {
    'Mahendra suthar': (19,'1234567890','Dabok',313022),
    'Pradeep suthar': (21,'8440077147','Udaipur',307022),
    'Vishal suthar': (20,'0987654321','Pindwara',303122)
}

dm = DataMatrix(length=len(data))
dm.name = data.key()
dm.age = data.value()
print(dm)