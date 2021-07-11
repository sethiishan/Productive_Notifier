import time
from plyer import notification

if __name__ == '__main__':
 	while True:
 		notification.notify(
 			title = "Ishan Drink Water Now!!!",
 			message ="Weight Loss, Max Energy, Makes You Happy and  Great Health!!!",
 			app_icon = r"E:\Projects_Ishan\Notification Generator\icon.ico",
 			timeout= 1
 			)
 		time.sleep(6)
 		#	time.sleep(60*60)
