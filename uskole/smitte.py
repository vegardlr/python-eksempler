# SMITTE - Pythonskole
# En kalkulator som viser hvor raskt hele befolkningen 
# i en by kan bli smittet, for et gitt R-tall og 
# et gitt antall som tar med seg smitten hjem
# (f.eks. fra ferie). 
# 7.2.2022, kontakt@pythonskole.no

befolkning = 10000   # Så mange mennesker bor i byen
antall_smittede = 10 # Så mange var smittet første dag
antall_dager = 365   # Velg maks antall dager
R = 0.99             # Reproduksjonstallet

dag = 1 # Start en teller for dagene
while dag<antall_dager and smitte<1.0 and antall_smittede > 1:
    # Regn ut antall smittede den neste dagen
    antall_smittede = antall_smittede*R
    # Regn ut den prosentvise smitten, rund av til 2 desimaler
    smitte_prosent = round(100.0*antall_smittede/befolkning,2)
    # Skriv ut status for smitten
    print("Dag",dag,":",smitte_prosent,
            "% av befolkningen er smittet!")
    dag = dag + 1
