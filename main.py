import Adafruit_DHT

pin = 18
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin)
print(humidity)
print(temperature)