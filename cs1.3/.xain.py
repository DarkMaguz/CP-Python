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


def scanArea(image, x, y, hSize, vSize):
  vHalf = int(hSize / 2)
  hHalf = int(vSize / 2)
  for v in range(hHalf * -1, hHalf):
    for h in range(vHalf * -1, vHalf):
      if isPixelTarget(image[x + h, y + v]):
        #print('size: {}x{} -> {}x{}'.format(v, h, x + h, y + v))
        return True
  return False


def findTarget(image, width, height):
  for x in range(0, width):
    for y in range(0, height):
      if isPixelTarget(image[x, y]):
        # print('target: {}x{}'.format(x, y))
        #print('size: {}x{} -> {}x{}'.format(v, h, x + h, y + v))
        return [x, y]
  return None


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
    screenShot = ImageGrab.grab(xdisplay=displayName)
    #centerPixel = screenShot[xCenter, yCenter]
    #if isPixelTarget(centerPixel):
    #  xdo.click_window(hlcsWindowID, 1)

    #if scanArea(screenShot, xCenter, yCenter, 10, 10):
    #  xdo.click_window(hlcsWindowID, 1)
    print('size2: {}x{}'.format(screenShot.width, screenShot.height))
    target = findTarget(screenShot, screenShot.width, screenShot.height)
    if target != None:
      print('\a')
      print('target: {}x{}'.format(target[0], target[1]))


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
