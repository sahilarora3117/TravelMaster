import requests
import json
lineList = [line.rstrip('\n') for line in open('Assets/temp.txt')]
import csv
reader = csv.DictReader(open("Assets/city_list.csv"))
id = ""
for i in reader:
    if i['City name'] == lineList[1]:
        id = i['City ID']
        break
if id == "":
    print("Not Found")
response = requests.get("http://developer.goibibo.com/api/cyclone/?app_id=1a7d2727&app_key=c7c71ee22f2d3044fe8e550fbe50f18d&city_id={id}&check_in=20191013&check_out=20191014".format(id = id))

a = response.json()['data']
l=[]
ll = []
k = 5
for i in a:
    if a[i]['op'] < int (lineList[2]) and k!=0:
        l.append(i)
        l.append(a[i]['op'])
        k-=1
for i in range (0,len(l),2):
    response = requests.get("http://developer.goibibo.com/api/voyager/?app_id=1a7d2727&app_key=c7c71ee22f2d3044fe8e550fbe50f18d&method=hotels.get_hotels_data&id_list=%5B{id}%5D&id_type=_id".format(id = l[i]))
    a = response.json()['data']
    id_new = l[i]
    ll.append(a[id_new]['hotel_geo_node']['name'])
  
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Handler:
    def on_destroy(self, *args):
        Gtk.main_quit()
    def button_add(self, button):
        l1 = builder.get_object("l1")

        l2 = builder.get_object("l2")
        l3 = builder.get_object("l3")
        l1.set_text(str(ll[0]) + " : " + str(l[1]))
        l2.set_text(str(ll[1]) + " : " + str(l[3]))
        l3.set_text(str(ll[3]) + " : " + str(l[5]))


builder = Gtk.Builder()
builder.add_from_file("hotels.glade")
builder.connect_signals(Handler())

window = builder.get_object("mainWindow")
window.show_all()
Gtk.main()
