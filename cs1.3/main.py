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


def getWindowID():
  with subprocess.Popen(['wmctrl', '-l'], stdout=subprocess.PIPE) as proc:
    output = proc.stdout.read().decode('utf-8')
    for line in output.split('\n'):
      if line.find('Half-Life') != -1:
        return int(line.split(' ')[0], 16)
  return None


def pixel2lab(pixel):
  rgbPixel = sRGBColor(pixel[0], pixel[1], pixel[2], True)
  return convert_color(rgbPixel, LabColor)


colorDiffThreshold = 90
targetValue = pixel2lab([255, 0, 198])
def isPixelTarget(pixel):
  if pixel[1] > 10:
    return False
  pixelValue = pixel2lab(pixel)
  colorDiff = delta_e_cie1976(targetValue, pixelValue)
  return colorDiff < colorDiffThreshold


def main():
  print(time.time())
  print('Searching for window of CS...')
  hlcsWindowID = getWindowID()
  while hlcsWindowID == None:
    time.sleep(2)
    hlcsWindowID = getWindowID()
  print('Found CS at', hlcsWindowID)
  time.sleep(10)
  display = Display.Display()
  displayName = display.get_display_name()
  screen = display.screen()
  width = screen.width_in_pixels
  height = screen.height_in_pixels
  print('size1: {}x{}'.format(width, height))
  xCenter = int(width / 2)
  yCenter = int(height / 2)
  xdo = Xdo()
  while True:
    time.sleep(1.01)
    screenShot = ImageGrab.grab(xdisplay=displayName).load()
    centerPixel = screenShot[xCenter, yCenter]
    if isPixelTarget(centerPixel):
      xdo.click_window(hlcsWindowID, 1)
      print('\a')
      print('target: {}.{}.{}'.format(centerPixel[0], centerPixel[1], centerPixel[2])


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
