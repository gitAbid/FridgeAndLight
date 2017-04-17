from firebase import firebase
import app
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

firebase=firebase.FirebaseApplication("https://light-and-fridge.firebaseio.com/",None)
while(1):
    result=firebase.get("/fridge/state",None)
    if(result=="send"):
        GPIO.output(18,GPIO.HIGH)
        app.dropbox_app()
        firebase.put("/fridge","state","!send")
        GPIO.output(18,GPIO.LOW)
  

