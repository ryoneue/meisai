import numpy as np
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
from io import StringIO

import datetime, re
# import googleapiclient.discovery
# import google.auth
import calendar
import glob

def pdf2summary(pdf_path):
    
    infp = open(pdf_path, "rb")
    # 出力先をPythonコンソールするためにIOストリームを取得
    outfp = StringIO()
    
    
    # 各種テキスト抽出に必要なPdfminer.sixのオブジェクトを取得する処理
    
    rmgr = PDFResourceManager() # PDFResourceManagerオブジェクトの取得
    lprms = LAParams()          # LAParamsオブジェクトの取得
    device = TextConverter(rmgr, outfp, laparams=lprms)    # TextConverterオブジェクトの取得
    iprtr = PDFPageInterpreter(rmgr, device) # PDFPageInterpreterオブジェクトの取得
    lprms.char_margin=30
    # PDFファイルから1ページずつ解析(テキスト抽出)処理する
    for page in PDFPage.get_pages(infp):
        iprtr.process_page(page)
    
    text = outfp.getvalue()  # Pythonコンソールへの出力内容を取得
    
    contents = outfp.getvalue()
    sep = contents.split("\n")
    ignore = [" ", "　", "  ", '         ']

    sep = [i.replace(" ", "") for i in sep]
    sep = [i for i in sep if i != ""]
    
    
    # idx = sep.index(user_name)
    kinmu_list = sep[5:10]
    sikyu_list = sep[15:21]
    sonota_list = sep[26:29]
    hoteikojo_list = sep[32:37]
    kojo_list = sep[39:47]
    summary_list = sep[59]

    info = {}
    for i,key in enumerate(kinmu_list):
        info[key] = sep[5+i+5]

    for i,key in enumerate(sikyu_list):
        info[key] = sep[15+i+5]
    for i,key in enumerate(sonota_list):
        info[key] = sep[26+i+2]
    for i,key in enumerate(hoteikojo_list):
        info[key] = sep[32+i+13]
    for i,key in enumerate(kojo_list):
        info[key] = sep[39+i+12]
    # for i,key in enumerate(summary_list):
    #     info[key] = sep[59+i+2]
    info[summary_list] = sep[59+2]


    schedule = sep[idx+2].split(" ")
    
    start = sep[4]
    end = sep[6]
    
    
    outfp.close()  # I/Oストリームを閉じる
    device.close() # TextConverterオブジェクトの解放
    infp.close()     #  Fileストリームを閉じる
    return schedule, start, end, sep

data_path = r"C:\Users\ryone\Documents\git\meisai\data\2022"

pdfs = glob.glob(data_path + "/*.pdf")
for pdf in pdfs:
    pdf2summary(pdf)
    print(pdfs)
