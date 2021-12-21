from flask import Flask, render_template
from werkzeug.utils import redirect
import RPi.GPIO as GPIO

LED_PIN1 = 22
LED_PIN2 = 27

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

@app.route("/")
def home():
    return render_template("led.html")

@app.route("/led/<color>/<op>")
def led_op(color,op):
    if color == "red":
        if op == "on":
            GPIO.output(LED_PIN1, GPIO.HIGH)
            return "LED ON"
        elif op == "off":
            GPIO.output(LED_PIN1, GPIO.LOW)
            return "LED OFF"
    elif color == "blue":
        if op == "on":
            GPIO.output(LED_PIN2, GPIO.HIGH)
            return "LED ON"
        elif op == "off":
            GPIO.output(LED_PIN2, GPIO.LOW)
            return "LED OFF"
        

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()