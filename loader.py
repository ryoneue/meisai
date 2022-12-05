import numpy as np
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
from io import StringIO

import datetime, re
import googleapiclient.discovery
import google.auth
import calendar
import glob

data_path = r"C:\Users\ryone\Documents\git\meisai\data"

pdfs = glob.glob(data_path + "/*.pdf")

