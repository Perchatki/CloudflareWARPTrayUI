import os, gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk, AppIndicator3 as appindicator
def main():
  indicator = appindicator.Indicator.new("customtray", "Path/To/Your/Icon.svg", appindicator.IndicatorCategory.APPLICATION_STATUS)
  indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
  indicator.set_menu(menu())
  gtk.main()
def menu():
  menu = gtk.Menu()
  
  con = gtk.MenuItem('Connect to WARP')
  con.connect('activate', defcon)
  menu.append(con)
  discon = gtk.MenuItem('Disconnect')
  discon.connect('activate', defdiscon)
  menu.append(discon)
  exittray = gtk.MenuItem('Exit Tray')
  exittray.connect('activate', quit)
  menu.append(exittray)
  
  menu.show_all()
  return menu
  
def defcon(_):
  os.system("warp-cli connect")
def defdiscon(_):
  os.system("warp-cli disconnect")
def quit(_):
  gtk.main_quit()
if __name__ == "__main__":
  main()
