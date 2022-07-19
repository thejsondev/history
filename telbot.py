import requests
import time
from datetime import datetime
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    min = now.strftime("%M")
    print(min)
    if min == "11":
        url = requests.get('https://api.telegram.org/bot5380558715:AAE4Km1cHmiOHrugGNjtar6zDU3uq8WaGEM/sendMessage?chat_id=1374029322&text=commit')
        time.sleep(60)
    else:
        time.sleep(60)