import pydicom
import numpy as np
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from skimage import morphology
from skimage import measure
from skimage.transform import resize
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly import figure_factory as FF
from plotly.graph_objs import *
import sys
import glob
import scipy.ndimage

# To open images inline and not in a new window
%matplotlib inline

# To create interactive widgets we need the following packages
import ipywidgets as ipyw
from ipywidgets import interactive, interact, widgets, Layout, Button, Box
from IPython.display import display

