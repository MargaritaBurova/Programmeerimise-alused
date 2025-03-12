logid = [
  {"aeg": "2025-03-10", "tüüp": "info", "sõnum": "Server käivati"},
  {"aeg": "2025-03-10", "tüüp": "info", "sõnum": "Kasutaja sisselogimine edukas"},
  {"aeg": "2025-03-10", "tüüp": "error", "sõnum": "Andmebaasi ühenduse viga"},
  {"aeg": "2025-03-10", "tüüp": "warn", "sõnum": "Mälu kasutus ületab piirangut"},
  {"aeg": "2025-03-10", "tüüp": "info", "sõnum": "Serveris tehtud uuendus"},
  {"aeg": "2025-03-10", "tüüp": "info", "sõnum": "Taustaprotsess käivitati"},
  {"aeg": "2025-03-10", "tüüp": "error", "sõnum": "Võrguprobleem, ühendus katkestatud"},
  {"aeg": "2025-03-10", "tüüp": "info", "sõnum": "Kasutaja väljalogimine edukas"},
  {"aeg": "2025-03-10", "tüüp": "warn", "sõnum": "Kasutaja õigused piiratud"},
  {"aeg": "2025-03-10", "tüüp": "info", "sõnum": "Logimine lõpetatud"}
]

def errorCount(data):
    infoCount = 0
    for elem in range(0,len(logid)):
        if logid[elem]["tüüp"] == "error":
            infoCount = infoCount + 1     
    return{"error":infoCount}

def worningCount(data):
    infoCount = 0
    for elem in range(0,len(logid)):
        if logid[elem]["tüüp"] == "warn":
            infoCount = infoCount + 1     
    return{"warn":infoCount}

def infoCount(data):
    infoCount = 0
    for elem in range(0,len(logid)):
        if logid[elem]["tüüp"] == "info":
            infoCount = infoCount + 1     
    return{"info":infoCount}

myList = [errorCount(logid),worningCount(logid),infoCount(logid)]
print(myList)

try:
    myList = [5,4,3]
    print(myList[2])
    x=10
    x/0
except IndexError:
    print("Error: vale pandnud indexid")
except ZeroDivisionError:
    print("Error: ma ei saa jagad nuliks")
except ValueError:
    print("Error: ma ei saa jagad nuliks")
finally:
    print("Programm lõppetab oma töö")

# print(errorCount(logid))





# print(logid[0]["aeg"])
# print(logid[0]["tüüp"])
# print(logid[-1])
# 
# for elem in range(0,len(logid)):
#     print(logid[elem]['tüüp'])
#     if logid[elem]['tüüp'] == "Info":
#         infoCount = infoCount + 1
        
# print(infoCount)
    
   
   #or   
# 
# for elem in logid:
#     print(elem['tüüp'])
    

    