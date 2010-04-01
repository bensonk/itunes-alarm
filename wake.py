#!/usr/bin/env pythonw2.6
from time import sleep
from datetime import datetime, time, timedelta
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
  return "%02d:%02d:%02d" % (hours, min, sec)

assert len(argv) > 1, "Please supply a time of the format hh:mm"
target = [ int(x) for x in argv[1].split(":") ]
assert len(target) == 2 or len(target) == 3, "Please supply a valid time in the form hh:mm"
targetDate = datetime.combine(datetime.today(), time(*target))

if targetDate < datetime.now(): targetDate += timedelta(days=1)
print "Waking at %s" % targetDate
assert targetDate >= datetime.now(), "Time must be in the future."

delt = targetDate - datetime.now()
assert delt.days == 0, "Time is more than a day into the future.  That's not going to work."
print "sleeping for %s" % format(delt)
sleep(delt.seconds)
wake()
