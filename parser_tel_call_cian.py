from selenium import webdriver
from datetime import datetime
import tkinter
import threading

URL = 'https://www.cian.ru/cat.php?deal_type=rent&engine_version=2&is_by_homeowner=1&offer_type=flat&region=1&room1=1' \
      '&room2=1&room3=1&sort=creation_date_desc&type=4 '
tel_num = ''
phone_numbers = []
client_info = []
driver = webdriver.Chrome('E:\Рома\chromedriver')
driver.get(URL)


def user_interface():
    def call_phone():
        lbl.configure(text='Звоню...')

    def cancel_call():
        lbl.configure(text='Вызов завершен')

    def about_client():
        lbl.configure(text=client_info[0] + '\n' + client_info[1] + '\n' + client_info[2])


    window = tkinter.Tk()
    window.title('made by Hellgenoid')
    window.geometry('500x500')  # размер окна
    lbl = tkinter.Label(window, font=('Calibry', 15))
    lbl.grid(padx=90, row=0)  # позиция текста
    button1 = tkinter.Button(window, text='Позвонить', font=('Arial', 15), fg='green', command=call_phone)
    button1.grid(padx=90, pady=10, row=1, ipadx=94, ipady=10)  # позиция кнопки
    button2 = tkinter.Button(window, text='Завершить вызов', font=('Arial', 15), fg='red', command=cancel_call)
    button2.grid(padx=90, row=2, ipadx=60, ipady=10)
    button3 = tkinter.Button(window, text='Информация о клиенте', font=('Arial', 15), command=about_client)
    button3.grid(padx=90, pady=12, row=3, ipadx=37, ipady=10)
    window.mainloop()


def find_push_button():
    find_info()
    element = driver.find_element_by_class_name('_93444fe79c--phone-button--3RYRY')
    cookie = driver.find_element_by_css_selector('#cookie-agreement > div > div._6eb00b8e53--button-wrapper--2MPyr > '
                                                 'button')
    cookie.click()
    element.click()
    try:
        number = driver.find_element_by_css_selector('body > div._93444fe79c--overlay--3m5HM > div > div > '
                                                     'div._93444fe79c--body--16wEB > div > div > div > div:nth-child('
                                                     '2) > a > span')
    except Exception:
        number = driver.find_element_by_css_selector('#frontend-serp > div > div._93444fe79c--wrapper--E9jWb > '
                                                     'article:nth-child(1) > div._93444fe79c--card--2umme > '
                                                     'div._93444fe79c--content--2IC7j > div._93444fe79c--aside--3CYFS '
                                                     '> div._93444fe79c--agent-cont--1SAAz > '
                                                     'div._93444fe79c--agent--1Ima_ > div > '
                                                     'div._93444fe79c--phone-button--3RYRY > div:nth-child(1) > div > '
                                                     'span')
    global tel_num
    tel_num = number.text


def refresh_and_check():
    driver.refresh()
    element = driver.find_element_by_class_name('_93444fe79c--phone-button--3RYRY')
    element.click()
    try:
        number = driver.find_element_by_css_selector('body > div._93444fe79c--overlay--3m5HM > div > div > '
                                                     'div._93444fe79c--body--16wEB > div > div > div > div:nth-child('
                                                     '2) > a > span')
    except Exception:
        number = driver.find_element_by_css_selector('#frontend-serp > div > div._93444fe79c--wrapper--E9jWb > '
                                                     'article:nth-child(1) > div._93444fe79c--card--2umme > '
                                                     'div._93444fe79c--content--2IC7j > div._93444fe79c--aside--3CYFS '
                                                     '> div._93444fe79c--agent-cont--1SAAz > '
                                                     'div._93444fe79c--agent--1Ima_ > div > '
                                                     'div._93444fe79c--phone-button--3RYRY > div:nth-child(1) > div > '
                                                     'span')
    global tel_num
    tel_num = number.text


def find_info():
    if client_info:
        client_info.clear()
    title = driver.find_element_by_class_name('_93444fe79c--container--JdWD4').text
    address = driver.find_element_by_class_name('_93444fe79c--labels--1J6M3').text
    price = driver.find_element_by_css_selector('#frontend-serp > div > div._93444fe79c--wrapper--E9jWb > '
                                                'article:nth-child(1) > div._93444fe79c--card--2umme > '
                                                'div._93444fe79c--content--2IC7j > div._93444fe79c--general--2SDGY > '
                                                'div > div:nth-child(4) > div:nth-child(1) > span > span').text
    client_info.append(title), client_info.append(address), client_info.append(price)


def start_refresh():
    while True:
        refresh_and_check()
        if tel_num in phone_numbers:
            print(f"Данные обновлены. Прошло времени: {datetime.now() - start_time}.")
        else:
            phone_numbers.append(tel_num)
            find_info()


if __name__ == '__main__':
    start_time = datetime.now()
    find_push_button()
    proc = threading.Thread(target=user_interface)
    proc.start()
    start_refresh()

