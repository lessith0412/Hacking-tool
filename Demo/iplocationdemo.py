import geocoder
import folium

def iplocator():
    g=geocoder.ip('101.223.255.255')
    myaddress= g.latlng
    my_map= folium.Map(location=myaddress,
                       zoom_start=12)
    folium.CircleMarker(location=myaddress,
                        radius=50).add_to(my_map)

    my_map.save('1.html')
if __name__=="__main__":
    iplocator()
