#!/bin/bash

battery_status=$(sudo dbus-send --system --print-reply --dest=org.freedesktop.UPower /org/freedesktop/UPower/devices/battery_BAT0 org.freedesktop.DBus.Properties.Get string:'org.freedesktop.UPower.Device' string:'State' | grep "uint32" | awk '{print $3}')

if [ "$battery_status" == "1" ]; then
  echo "Plugged in."
elif [ "$battery_status" == "2" ]; then
  echo "Not plugged in."
else
  echo "Unknown status"
fi

