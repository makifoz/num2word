
birler = {"0":"","1":"Bir","2":"İki","3":"Üç","4":"Dört","5":"Beş","6":"Altı","7":"Yedi","8":"Sekiz","9":"Dokuz"}
onlar = {"1":"On","2":"Yirmi","3":"Otuz","4":"Kırk","5":"Elli","6":"Altmış","7":"Yetmiş","8":"Seksen","9":"Doksan"}
yuzler = {"0":"","1":"Yüz"}
basamak = {"1":"","2":"Bin","3":"Milyon","4":"Milyar"}

def num2word3(d):
      
    if len(d) == 3:
        sayı= yuzler.get(d[0],birler.get(d[0],"")+" Yüz")+" "+ onlar.get(d[1],"") + " "+ birler.get(d[2],"")
        return sayı
    if len(d) == 2:
        sayı = onlar.get(d[0],"") + " "+  birler.get(d[1],"")
        return  sayı
    if len(d) == 1:
        return birler.get(d[0],"")

def num2word(i):
    d = str(i)
   
    deger =""
    

    basaSifirEkle = len(d)%3
   
    if basaSifirEkle == 1:
        d = "00"+d
    
    elif basaSifirEkle == 2:
        d = "0"+d
    else:
        d = d
    j = int(len(d)/3)
    while j!=0:
        if not num2word3(d[0:3]).isspace():
            deger = deger + " "+ num2word3(d[0:3])+" " +basamak[str(j)]
        d = d[3:]
        j -=1

    print(deger)
        
    	

def check_number(i):
    return_result = False
    i = int(i)
    if  (0 <= i and i <= 2147483647):
        return_result = True
    return return_result

def getInput():
    while 1:
        print("Lütfen Bir Sayı Giriniz...")
        i =  input()
        if i == "0":
            print("Sıfır")
            continue
        if(check_number(i)):
            i = int(i)
            num2word(i)
        else:
            print("Hatalı Sayı Girdiniz.")

if __name__ == '__main__':
    getInput()	
