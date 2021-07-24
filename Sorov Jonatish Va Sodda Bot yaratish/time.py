# response=r.get(UPDATE_URL)
# response_dic=json.loads(response.text)
#vaqt=response_dic["result"][-1]["message"]["data"]

from datetime import datetime
from time import time 

vaqt=int(input("vaqt: "))
dt= datetime.fromtimestamp(vaqt)
chasa="{}:{}:{}".format(dt.hour,dt.minute,dt.second)
print(chasa)