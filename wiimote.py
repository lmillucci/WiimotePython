import  cwiid
import time

print("Premi 1+2 per connettere il wiimote")

time.sleep(2)

wm=cwiid.Wiimote()

for i in range(16):
	wm.led=i
	time.sleep(0.5)
	
wm.rpt_mode = cwiid.RPT_BTN

while True:
	button = wm.state['buttons']
	
	# & serve per fare il confronto bit a bit
	if(button & cwiid.BTN_LEFT):
		print("Ho premuto il tasto sinistro ",button)
	
	if(button & cwiid.BTN_RIGHT):
		print("Ho premuto il tasto destro",button)
	
	time.sleep(0.1)

