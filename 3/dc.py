import requests,json,time,sys,random,os,argparse
import colorama
from colorama import Fore, Back, Style
from random import randint
from datetime import datetime
colorama.init(autoreset=True)

parser = argparse.ArgumentParser(description='999 Dice Bot | This Is Gambling Bot Plase Take Own Your Risk')
parser.add_argument(
    '-c','--betset',
    default=0,
    help='Enter Your Betset Number (default: 0)'
)
my_namespace = parser.parse_args()

with open('config.json', 'r') as myfile:
      data=myfile.read()
# parse file
obj = json.loads(data)

print (Style.NORMAL+Fore.MAGENTA+"      ___  _           ___       __\n     / _ \(_)______   / _ )___  / /_\n    / // / / __/ -_) / _  / _ \/ __/\n   /____/_/\__/\__/ /____/\___/\__/"+Style.NORMAL+Fore.GREEN+"\n=======================================\n")
hijau = Style.BRIGHT+Fore.GREEN
res = Style.RESET_ALL
abu2 = Style.NORMAL+Fore.WHITE
ungu = Style.NORMAL+Fore.MAGENTA
hijau2 = Style.NORMAL+Fore.GREEN
red2 = Style.NORMAL+Fore.RED
red = Style.BRIGHT+Fore.RED
c = requests.session()
a=0
url = "https://www.999doge.com/api/web.aspx"
ua = {
 "Origin": "file://",
 "user-agent": obj["User-Agent"],
 "Content-type": "application/x-www-form-urlencoded",
 "Accept": "*/*",
 "accept-encoding": "gzip, deflate, br",
 "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
 "X-Requested-With": "com.reland.relandicebot"
}

def konvert(persen,taruhan):
    global high
    global low
    c = str(999999 * float(persen) / 100)
    if taruhan == "Hi" or taruhan == "hi" or taruhan == "HI":
       n = str(c.split(".")[1])
       pangkat = 6 - len(n)
       low = int(int(n) * (10 ** pangkat))
       high = 999999
    if taruhan == "Lo" or taruhan == "LOW" or taruhan == "low" or taruhan == "Low" or taruhan == "LO":
       low = 0
       high = int(c.split(".")[0])


def rev(num):
    if (len(num) < 8):
        panjang_nol = int(8 - len(num))
        num = ((panjang_nol*"0")+str(num))
        result = ("0."+num)
    if (len(num) == 8):
        panjang_nol = int(8 - len(num))
        num = ((panjang_nol*"0")+str(num))
        result = ("0."+num)
    else:
        len_num = len(num)
        end = num[-8:]
        first = num[:len_num-8]
        result = (first+"."+end)
    return (result)


def dice(ws,ls):
   if my_namespace.betset == "Auto" or my_namespace.betset == "auto" or my_namespace.betset == "AUTO":
      urut = 0
      jumlahulang= 0
      while True:
         jumlahulang+=1
         try:
             pesan = obj["Config"][jumlahulang]["Name Bet Set"]
         except:
             break
   else:
      urut = int(my_namespace.betset)

   slp = int(obj["Config"][urut]["Interval"]) / 1000
   limit_a = int(obj["Config"][urut]["Reset If Win"]) - 1
   payin = int(float(obj["Config"][urut]["Base Bet"])*(10 ** 8))
   konvert(obj["Config"][urut]["Chance"],obj["Config"][urut]["Bet"]["Bet"])
   amount = payin
   data = {
      "a": "PlaceBet",
      "s": js["SessionCookie"],
      "PayIn": amount,
      "Low": low,
      "High": high,
      "ClientSeed": randint(0,999999),
      "Currency": "doge",
      "ProtocolVersion": "2"
   }
   try:
     r1 = c.post(url,headers=ua,data=data)
     jsn = json.loads(r1.text)
     jumbl = jsn["StartingBalance"] + int(jsn["PayOut"]) - int(amount)
     jum = int(jsn["PayOut"]) - int(amount)
     prof = (float(jsn["StartingBalance"] + int(jsn["PayOut"]) - int(amount) - jumbl)/(10 ** 8))
     print (hijau+"\nStarting Balance",res+str((float(int(jsn["StartingBalance"]) + int(jum))/(10 ** 8))))
     print ("Anda Menggunakan BetSet Ke "+obj["Config"][urut]["Name Bet Set"])
     n = 0
     burst = False
     stats_rolebet_lose = False
     stats_rolebet_win = False
     menit = datetime.now().strftime('%M')
     menit = int(menit) + int(obj["Interval"])
     no_win = 0
     no_lose = 0
     total_win=0
     total_lose=0
     no_rolebet = 0
     rolebet="Hi"
     while True:
        if obj["Config"][urut]["Max Bet"] == "OFF" or obj["Config"][urut]["Max Bet"] == "off" or obj["Config"][urut]["Max Bet"] == "Off":
            sys.stdout.write("")
        else:
           if amount > int(float(obj["Config"][urut]["Max Bet"])*(10 ** 8)):
               amount = payin
        if obj["Config"][urut]["Bet"]["Hi / Low"]["Toggle"] == "On" or obj["Config"][urut]["Bet"]["Hi / Low"]["Toggle"] == "ON" or obj["Config"][urut]["Bet"]["Hi / Low"]["Toggle"] == "on":
            no_rolebet +=1
            if stats_rolebet_win is True:
               if no_rolebet > int(obj["Config"][urut]["Bet"]["Hi / Low"]["If Win"]) - 1:
                  rolebet = "Lo"
               if no_rolebet > int(obj["Config"][urut]["Bet"]["Hi / Low"]["If Win"]) * 2 - 1:
                  rolebet = "Hi"
                  no_rolebet = 0
            if stats_rolebet_lose is True:
               if no_rolebet > int(obj["Config"][urut]["Bet"]["Hi / Low"]["If Lose"]) -1 :
                  rolebet = "Lo"
               if no_rolebet > int(obj["Config"][urut]["Bet"]["Hi / Low"]["If Lose"]) * 2 - 1:
                  rolebet = "Hi"
                  no_rolebet = 0
        else:
            rolebet = obj["Config"][urut]["Bet"]["Bet"]
        if my_namespace.betset == "Auto" or my_namespace.betset == "AUTO" or my_namespace.betset == "auto":
          waktu = datetime.now().strftime('%M')
          if int(waktu) > int(menit - 1):
             menit = int(menit) + int(obj["Interval"])
             urut +=1
             if urut == jumlahulang:
                urut = 0
             print ("Change Bet Set "+obj["Config"][urut]["Name Bet Set"]+"                           ")
             slp = int(obj["Config"][urut]["Interval"]) / 1000
             limit_a = int(obj["Config"][urut]["Reset If Win"]) - 1
             payin = int(float(obj["Config"][urut]["Base Bet"])*(10 ** 8))

        else:
          urut = int(my_namespace.betset)

        if obj["Config"][urut]["Random Chance"]["Toggle"] == "ON" or obj["Config"][urut]["Random Chance"]["Toggle"] == "On" or obj["Config"][urut]["Random Chance"]["Toggle"] == "on":
           hasil_chance = round(random.uniform(float(obj["Config"][urut]["Random Chance"]["Min"]),float(obj["Config"][urut]["Random Chance"]["Max"])),2)
           cok = len(str(hasil_chance))
           if cok == 3:
              sys.stdout.write("\r"+str(hasil_chance)+"   ")
           if cok == 4:
              sys.stdout.write("\r"+str(hasil_chance)+"  ")
           if cok == 5:
              sys.stdout.write("\r"+str(hasil_chance)+" ")
           konvert(hasil_chance,str(rolebet))
        else:
           konvert(obj["Config"][urut]["Chance"],str(rolebet))
        time.sleep(float(slp))
        amount = int(amount)
        n+=1
        data = {
          "a": "PlaceBet",
          "s": js["SessionCookie"],
          "PayIn": amount,
          "Low": low,
          "High": high,
          "ClientSeed": randint(0,999999),
          "Currency": "doge",
          "ProtocolVersion": "2"
        }
        if prof > float(obj["Target Profit"]):
           print (hijau+"\nYay.! \nProfit Mencapai Target.....!\n"+hijau+"Profit "+res+str(prof))
           
           sys.exit()
        r1 = c.post(url,headers=ua,data=data)
        jsn = json.loads(r1.text)
        prof = (float(jsn["StartingBalance"] + int(jsn["PayOut"]) - int(amount) - jumbl)/(10 ** 8))
        jum = int(jsn["PayOut"]) - int(amount)
        if jsn["StartingBalance"] > ws:
           print (ungu+"["+res+str(rolebet)+ungu+"] "+hijau2+str(float(amount)/(10 ** 8)),res+str(float(int(jsn["StartingBalance"]) + int(jum))/(10 ** 8)),hijau2+"Profit",res+str(prof))
           print (hijau+"Yay.!\nBalance Sudah Memenuhi Target.....!")
           
           sys.exit()
        if jsn["StartingBalance"] < ls:
           print (ungu+"["+res+str(rolebet)+ungu+"]"+red2+"-"+str(float(amount)/(10 ** 8)),res+str((float(int(jsn["StartingBalance"]) + int(jum))/(10 ** 8))),red2+"Lose ",res+str(prof))
           print (Style.BRIGHT+Fore.RED+"Lose Target....!")
           time.sleep(1)
           sys.exit()
        if jsn["PayOut"] is not a:
           no_win +=1
           no_lose = 0
           bal = int(jsn["StartingBalance"]) + int(jum)
           if prof > 0:
             print (ungu+"["+res+str(rolebet)+ungu+"] "+hijau2+str(rev(str(amount))),res+str(rev(str(bal))),hijau2+"Profit",res+str(prof))
           else:
             print (ungu+"["+res+str(rolebet)+ungu+"] "+hijau2+str(rev(str(amount))),res+str(rev(str(bal))),red2+"Lose ",res+str(prof))


        else:
           no_win = 0
           no_lose +=1
           i = 0
           burst = True
           bal = int(jsn["StartingBalance"]) + int(jum)
           if prof > 0:
             print (ungu+"["+res+str(rolebet)+ungu+"]"+red2+"-"+str(rev(str(amount))),res+str(rev(str(bal))),hijau2+"Profit",res+str(prof))
           else:
             print (ungu+"["+res+str(rolebet)+ungu+"]"+red2+"-"+str(rev(str(amount))),res+str(rev(str(bal))),red2+"Lose ",res+str(prof))

        if burst is True:
           i+=1
           amount = int(amount) * float(obj["Config"][urut]["If Lose"])
           if i > limit_a:
             i = 0
             burst = False
        else:
           if n > limit_a:
             n = 0
             amount = payin
           else:
             amount = int(amount) * float(obj["Config"][urut]["If Win"])
        if no_win > total_win:
           stats_rolebet_win = True
           stats_rolebet_lose = False
           total_win +=1
        if no_lose > total_lose:
           stats_rolebet_lose = True
           stats_rolebet_win = False
           total_lose +=1
        sys.stdout.write(hijau+"Win Streak "+res+str(total_win)+red+" Lose Streak "+res+str(total_lose)+"\r")



   except:
       print ("")
       sys.exit()
r = c.get(url,headers=ua,data={"a": "Login","Key": "7ec7f8a2c9724b2cbb8ed75e72b47ee9","Username": obj["Account"]["Username"],"Password": obj["Account"]["Password"],"Totp": ""})
js = json.loads(r.text)
try:
  print (hijau+"Balance "+abu2+": "+res+str(float(js["Doge"]["Balance"])/(10 ** 8)))
except:
  print ("Check Your Username And Your Password")
  sys.exit()

dice(int(float(obj["Target Win"])*(10 ** 8)),int(float(obj["Lose Target"])*(10 ** 8)))