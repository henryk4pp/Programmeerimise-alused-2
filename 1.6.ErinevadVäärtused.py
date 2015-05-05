def kõik_erinevad(järjend):
    for i in range(len(järjend)):
        for j in range(len(järjend)):
            if järjend[i]==järjend[j] and i != j:
               return "Kõik järjendi liikmed pole erinevad"
    return "Kõik järjendi liikmed on erinevad"        
   
           
        
def kõik_erinevad2(järjend):
    hulk = set(järjend)
    if len(hulk)==len(järjend):
        return "Kõik järjendi liikmed on erinevad"
    else:
        return "Kõik järjendi liikmed pole erinevad"
