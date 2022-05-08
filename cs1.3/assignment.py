#!/usr/bin/python3

import subprocess
import time
import math

from Xlib import display as Display

from xdo import Xdo

from PIL import ImageGrab
from PIL import Image

from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie1976


# Finds the window id of CS as given by the windows manager.
def getWindowID():
  with subprocess.Popen(['wmctrl', '-l'], stdout=subprocess.PIPE) as proc:
    output = proc.stdout.read().decode('utf-8')
    for line in output.split('\n'):
      if line == "":
        continue
      windowName = line.split(' ')[-1]
      if windowName == 'Counter-Strike':
        return int(line.split(' ')[0], 16)
  return None


# This function converts a RGB pixel to colormath's LabColor type.
# We need to do this in order to utilize colormath's color diff function.
def pixel2lab(pixel):
  rgbPixel = sRGBColor(pixel[0], pixel[1], pixel[2], True)
  return convert_color(rgbPixel, LabColor)


# Find out what threshold value returned by delta_e_cie1976
colorDiffThreshold = ???
# Target value is the optimal RGB color value of the target.
# This is the same color that we have painted on the models heads.
targetValue = pixel2lab([255, 0, 198])
# This function uses the delta_e_cie1976 function to test if a
# given pixel should be considered a valid target.
def isPixelTarget(pixel):
  ???


# Scan a given area around x and y coordinates, test if it has a valid
# target and return either true or false.
def scanArea(image, x, y, hSize, vSize):
  ???


# Scan a given area around x and y coordinates and return the
# coordinates relative to x and y.
def findTarget(image, x, y, hSize, vSize):
  ???

def main():
  print('Searching for window of CS...')
  hlcsWindowID = getWindowID()
  while hlcsWindowID == None:
    time.sleep(2)
    hlcsWindowID = getWindowID()
  print('Found CS at', hlcsWindowID)
  time.sleep(10) # Give CS time to launch.
  xdo = Xdo()
  display = Display.Display()
  displayName = display.get_display_name()
  screen = display.screen()
  width = screen.width_in_pixels
  height = screen.height_in_pixels
  # x and y -Center variables should be the center point of our crosshairs aim.
  xCenter = int(???)
  yCenter = int(???)
  while True:
    time.sleep(???) # Limit the CPU useage of this script.
    screenShot = ImageGrab.grab(xdisplay=displayName).load()
    centerPixel = ???

    if isPixelTarget(centerPixel):
      # The escaped character "a" will be interpreted as a
      # bell sound by the terminal, this is quite useful for debugging.
      print('\a')

    # When we have acquired a target we can use the python libxdo tool.
    # Go to their website and look in the documentaion for helpfull functions.


if __name__ == '__main__':
  while True:
    try:
      main()
    except Exception as e:
      print('Error: ', e)
    except any as e:
      print('Error: ', any)
    finally:
      print('Oops... we crashed!')
