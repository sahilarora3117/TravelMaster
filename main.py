import gi
import sqlite3
import os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
couter = True
class Handler:
    def on_destroy(self, *args):
        os.system("killall `ps -aux | grep app | grep -v grep | awk '{ print $1 }'` && killall inotifywait")
        Gtk.main_quit()

    def button_add(self, button):
        label_result = builder.get_object("label_result")
        UserName = builder.get_object("entry_number1").get_text()
        Password = builder.get_object("entry_number2").get_text()
        with sqlite3.connect("Assets/login.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        cursor.execute(find_user,[(UserName), (Password)])
        results = cursor.fetchall()
        if results:
            
            label_result.set_text("Login Approved. Close this window to proceed.")
            print ("Hola")
            button.set_sensitive(False)
            exit()
            
            
            
        else:
            print ("Nola")
            label_result.set_text("Bad Credentials.")
    
    def but_reg(self,button):
        label_result = builder.get_object("reg")
        UserName = builder.get_object("entry_number1").get_text()
        Password = builder.get_object("entry_number2").get_text()
        with sqlite3.connect("Assets/login.db") as db:
            cursor = db.cursor()
        cursor.execute('INSERT INTO user(username,password) VALUES(?,?)' ,(UserName, Password))
        db.commit ()
        exit()





builder = Gtk.Builder()
builder.add_from_file("login.glade")
builder.connect_signals(Handler())

window = builder.get_object("mainWindow")
window.show_all()
Gtk.main()
