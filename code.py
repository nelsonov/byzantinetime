from adafruit_datetime import datetime as datetime
import sunrise  
s = sunrise.sun(lat=46,long=-114)  
print('sunset at ',s.sunset(when=datetime.now()))
