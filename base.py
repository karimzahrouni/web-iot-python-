from flask import Flask,render_template
import serial

serPort = serial.Serial('/dev/ttyACM1')       

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/on")
def LEDon():
    serPort.write(b'a')
    return render_template('index.html')

@app.route("/off")
def LEDoff():
    serPort.write(b'b')
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
