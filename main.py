import datetime
import time
import webbrowser
import pyautogui as gui
import pandas as pd


def sendmessege(to, msg):
    interval = 2
    url = 'https:/wa.me/{}?text={}'.format(to, msg)
    webbrowser.open(url)
    time.sleep(10)
    gui.press('enter')
    time.sleep(interval)


ds = pd.read_excel("")   #Add Excel or csv file here.  
today = datetime.datetime.now().strftime("%d-%m")
yearNow = datetime.datetime.now().strftime("%Y")
writeInd = []
for index, item in ds.iterrows():
    bday = item['Bday'].strftime("%d-%m")
    if (today == bday) and yearNow not in str(item['Year']):
        sendmessege(item['Whatsapp'], item['Message'])
        writeInd.append(index)

for i in writeInd:
    yr = ds.loc[i, 'Year']
    ds.loc[i, 'Year'] = str(yr) + ', ' + str(yearNow)

ds.to_excel('Birthday.xlsx', index=False)
