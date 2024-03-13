from IPython import get_ipython
from IPython.core.display import display, HTML
import pandas as pd
from tqdm.notebook import tqdm
tqdm.pandas()
import seaborn as sns
import pysam
from scipy.stats import pearsonr, spearmanr
from glob import glob
import pylab
import matplotlib.pyplot as plt
import terra_pandas


display(HTML("<style>#notebook-container { width:100% ;}</style>"))
display(HTML("<style>#menubar-container { width:100% !important;}</style>"))

ipython = get_ipython()
ipython.magic("config InlineBackend.print_figure_kwargs={'facecolor' : 'w'}")
ipython.magic("pylab inline")

params = {'legend.fontsize': '40',
          'figure.figsize': (10, 10),
          'axes.labelsize': '40',
          'axes.titlesize': '50',
          'xtick.labelsize': '40',
          'ytick.labelsize': '40',
          'axes.linewidth': '0.5',
          'pdf.fonttype': '42',
          'font.sans-serif': 'Helvetica'}
pylab.rcParams.update(params)

preferred_styles = ['seaborn-v0_8-white', 'seaborn-white']
for style in preferred_styles:
    if style in plt.style.available:
        plt.style.use(style)
        break