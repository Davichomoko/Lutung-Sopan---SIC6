import network
import urequests
import utime
from machine import Pin
import dht

# **Koneksi WiFi ESP32**
SSID = "Mokondo"
PASSWORD = "70700724"

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(SSID, PASSWORD)

while not station.isconnected():
    print("Menghubungkan ke WiFi...")
    utime.sleep(1)

print("Terhubung ke WiFi:", station.ifconfig())

# **Inisialisasi Sensor DHT11 di GPIO5**
sensor_dht = dht.DHT11(Pin(5))

# **Inisialisasi Sensor PIR (HC-SR501) di GPIO4**
sensor_pir = Pin(18, Pin.IN) 

# **Flask API URL**
url = "http://192.168.43.200:5000/sensor1"  # Ganti dengan IP komputer Flask

while True:
    try:
        # **Baca Sensor DHT11**
        sensor_dht.measure()
        temperature = sensor_dht.temperature()
        humidity = sensor_dht.humidity()
        
        # **Baca Sensor PIR**
        motion_detected = sensor_pir.value()  # 1 jika ada gerakan, 0 jika tidak

        # **Kirim Data ke Flask**
        data = {
            "temperature": temperature,
            "humidity": humidity,
            "motion": motion_detected  # Tambahkan status PIR
        }

        print("Mengirim data:", data)
        response = urequests.post(url, json=data)
        print("Response:", response.text)
        response.close()

    except Exception as e:
        print("Error:", e)

    utime.sleep(5)  # Kirim data setiap 5 detik

