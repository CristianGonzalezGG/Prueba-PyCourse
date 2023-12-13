import datetime
#print(datetime.date.today())
completed = datetime.datetime.now()
mensaje = input("Quiere ver la hora? ")
while mensaje.lower() == "si":
    print(f'Hora: {datetime.datetime.now()}')
    mensaje = input("Quiere ver la hora? ")