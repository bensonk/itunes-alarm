#!/usr/bin/env pythonw2.6
from time import sleep
from datetime import datetime, time
from sys import argv

def wake():
  import appscript
  itunes = appscript.app("iTunes")
  itunes.play()

def format(delt):
  sec = delt.seconds
  hours = int(sec / 3600)
  sec = sec % 3600
  min = int(sec / 60)
  sec = sec % 60
  return "%d:%d:%d" % (hours, min, sec)

assert len(argv) > 1, "Please supply a time of the format hh:mm"
target = [ int(x) for x in argv[1].split(":") ]
assert len(target) == 2, "Please supply a valid time in the form hh:mm"
targetDate = datetime.combine(datetime.today(), time(*target))
assert targetDate > datetime.now(), "Time must be in the future."
delt = targetDate - datetime.now()
assert delt.days == 0, "Time is not until tomorrow.  That's not going to work."
print "sleeping for %s" % format(delt)
sleep(delt.seconds)
wake()
