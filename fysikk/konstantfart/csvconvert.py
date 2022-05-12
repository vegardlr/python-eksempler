from datetime import datetime

innfil = 'konstantfart.csv'
utfil  = 'konstantfart_no.csv'

inn = open(innfil,"r")
ut  = open(utfil,"w")

firstLine = True
for linje in inn:
    utlinje = linje.replace(",",".").split(";")
    ut.write(";".join(utlinje[1:-1])+"\n")

inn.close()
ut.close()


