#색상 히스토그램2
import cv2
import numpy as np

def make_palette(rows):
    hue = [round(i*180/rows)]