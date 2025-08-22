import requests
import folium
import json


FIREBASE_URL = "https://gps-tracker-project-07-default-rtdb.firebaseio.com/GPSTracker.json"


response = requests.get(FIREBASE_URL)
data = response.json()


mymap = folium.Map(location=[32.0459, 74.0773], zoom_start=15)


if isinstance(data, dict):
    for name, coord_string in data.items():
        try:
            
            coords = json.loads(coord_string)

            if isinstance(coords, list) and len(coords) == 2:
                lat, lon = coords

               
                folium.Marker(
                    location=[lat, lon],
                    popup=f"{name}\nLat: {lat}, Lon: {lon}",
                    icon=folium.Icon(color="blue", icon="info-sign")
                ).add_to(mymap)
            else:
                raise ValueError("Coordinates not in [lat, lon] format")

        except Exception as e:
            print(f"Error for {name}: {e}")
else:
    print("Error: Unexpected Firebase data format")


mymap.save("gps_tracker_map.html")
print(" Map saved as gps_tracker_map.html")
