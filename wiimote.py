import  cwiid
import time

print("Premi 1+2 per connettere il wiimote")

time.sleep(1)

wm=cwiid.Wiimote()

for i in range(16):
	wm.led=i
	time.sleep(1)

