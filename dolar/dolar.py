from forex_python.converter import CurrencyRates
from playsound import playsound
import time

c=CurrencyRates()

mem = c.get_rate("USD","TRY")
print(f"Anlık dolar kuru: {mem}")
# mem=1

while True:
    kur = c.get_rate("USD","TRY")
    print(kur)

    if kur>mem:
        print("Arttı.")
        playsound("ses.mp3")
        mem=kur
    
    time.sleep(5)

