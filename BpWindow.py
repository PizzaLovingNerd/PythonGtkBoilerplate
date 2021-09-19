import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class RtMainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, application=app, title="Boilerplate Window")
        self.set_position(Gtk.WindowPosition.CENTER)

        # Headerbar
        # self.header = Gtk.HeaderBar()
        # self.header.set_show_close_button(True)
        # self.set_titlebar(self.header)

        # self.add(widget)

        self.show_all()