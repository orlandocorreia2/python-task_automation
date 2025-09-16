import pyautogui
import pandas
import time

pyautogui.PAUSE = 1

pyautogui.click(x=1343, y=22)

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(1)
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(site)
pyautogui.press("enter")
pyautogui.click(x=445, y=375)
pyautogui.write('ocnascimento2@gmail.com')

pyautogui.click(x=445, y=478)
pyautogui.write('01020304')
pyautogui.click(x=650, y=533)

time.sleep(1)
pyautogui.click(x=856, y=363)

table = pandas.read_csv('produtos.csv')

for line in table.index:
  pyautogui.click(x=470, y=260)
  for col in table.columns:
    value = str(table.loc[line, col])
    if value != "nan":
      pyautogui.write(str(table.loc[line, col]))    
    pyautogui.press('tab')

  pyautogui.press('enter')
  pyautogui.scroll(10000)

# time.sleep(5)
# print(pyautogui.position())
