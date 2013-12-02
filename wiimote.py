import  cwiid
import time

print("Premi 1+2 per connettere il wiimote")

time.sleep(2)

wm=cwiid.Wiimote()

for i in range(16):
	wm.led=i
	time.sleep(1)
	
wm.rpt_mode = cwiid.RPT_BTN

while True:
	button = wm.state['buttons']
	
	# & serve per fare il confronto bit a bit
	if(button & cwiid.BTN_LEFT):
		print("Ho premuto il tasto sinistro ",button)
	
	if(button & cwiid.BTN_RIGHT):
		print("Ho premuto il tasto destro",button)
	
	if(button & cwiid.BTN_UP):
		print("Ho premuto il tasto alto",button)
	
	if(button & cwiid.BTN_DOWN):
		print("Ho premuto il tasto basso",button)
		
	if(button & cwiid.BTN_A):
		print("Ho premuto il tasto A",button)
		
	if(button & cwiid.BTN_B):
		print("Ho premuto il tasto B",button)
		
	if(button & cwiid.BTN_1):
		print("Ho premuto il tasto 1", button)
		
	if(button & cwiid.BTN_2):
		print("Ho premuto il tasto 2",button)
		
	if(button & cwiid.BTN_MINUS):
		print("Ho premuto il tasto -",button)
	
	if(button & cwiid.BTN_PLUS):
		print("Ho premuto il tasto +",button)
		
	if(button & cwiid.BTN_HOME):
		print("Ho premuto il tasto HOME",button)
		wm.rumble= True
		time.sleep(1)
		wm.rumble = False
		exit()
		
	time.sleep(0.1)

