import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
import requests
import json

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.api_key = "0a7c9ddb50825a0b60ca7374d0103b72"

        self.title = "Weather App"
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.city_label = QLabel("City:", self)
        self.city_input = QLineEdit(self)

        self.get_weather_button = QPushButton("Get Weather", self)
        self.get_weather_button.clicked.connect(self.get_weather)

        self.temp_label = QLabel("", self)

        h_box = QHBoxLayout()
        h_box.addWidget(self.city_label)
        h_box.addWidget(self.city_input)

        v_box = QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addWidget(self.get_weather_button)
        v_box.addWidget(self.temp_label)

        self.setLayout(v_box)

    def get_weather(self):
        city = self.city_input.text()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
        res = requests.get(url)
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        self.temp_label.setText(f"Temperature in {city}: {temp} K")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WeatherApp()
    ex.show()
    sys.exit(app.exec_())

