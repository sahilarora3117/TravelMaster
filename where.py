import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Handler:
    def on_destroy(self, *args):
        Gtk.main_quit()

    def button_add(self, button):
        From = builder.get_object("entry_number1").get_text()
        To = builder.get_object("entry_number2").get_text()
        Budget = builder.get_object("entry_number3").get_text()
        c1 = builder.get_object("ch1").get_active()
        c2 = builder.get_object("ch2").get_active()
        c3 = builder.get_object("ch3").get_active()
        f = open("Assets/temp.txt", "w+")
        open("Assets/temp.txt", 'w').close()
        f.write(To + "\n" + From + "\n" + Budget + "\n" + str(c1) + "\n" + str(c2) + "\n" + str(c3) + "\n")
        button.set_sensitive(False)
        exit()



builder = Gtk.Builder()
builder.add_from_file("where.glade")
builder.connect_signals(Handler())

window = builder.get_object("mainWindow")
window.show_all()
Gtk.main()
