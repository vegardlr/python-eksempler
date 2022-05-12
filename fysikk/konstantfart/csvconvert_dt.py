from datetime import datetime
innfil = 'konstantfart.csv'
utfil  = 'konstantfart_no.csv'

inn = open(innfil,"r")
ut  = open(utfil,"w")

firstLine = True
for linje in inn:
    utlinje = linje.replace(",",".").split(";")
    datotid = utlinje[0]
    try:
        tid = datetime.strptime(utlinje[0],"%d.%m.%Y %H.%M.%S")
    except ValueError:
        ut.write(";".join(utlinje))
        continue

    if firstLine:
        tid_start = tid
        utlinje[0] = '0'
        firstLine = False
    else:
        utlinje[0] = str((tid-tid_start).seconds)
    
    ut.write(";".join(utlinje))

inn.close()
ut.close()


