import time
from tkinter import *

cnt_mes = -1
f = open('venv/Include/info.txt', 'r')
s = f.read()
const_buy = 0.1
buy = list(map(float, s.split()))
clicks = buy[0]
total = int(buy[5])
f.close()

cnt = 0


def on_closing():
    buy[0] = clicks
    buy[5] = total
    f_close = open('venv/Include/info.txt', 'w')
    s_tmp = str(" ".join(map(str, buy)))
    f_close.write(s_tmp)
    f_close.close()
    root.destroy()


def click():
    global clicks, buy, total
    total += 1
    clicks += 1 + buy[1] * const_buy + buy[2]
    count_clicks.config(text="{}".format(round(clicks, 2)))
    message.config(text="")


def add1():
    global buy, clicks, cnt_mes
    cnt_mes = 90
    if clicks >= 20:
        buy[1] += 1
        dlt(20)
        count_clicks.config(text="{}".format(round(clicks, 1)))
        message_speed.config(text="+{}".format(round(1 + buy[1] * const_buy + buy[2], 1)))
        message.config(text="Thank you!")
    else:
        message.config(text="Not enough clicks")


def add2():
    global buy, clicks, cnt_mes
    cnt_mes = 90
    if clicks >= 120:
        buy[2] += 1
        dlt(120)
        message.config(text="Thank you!")
        message_speed.config(text="+{}".format(round(1 + buy[1] * const_buy + buy[2], 1)))
    else:
        message.config(text="Not enough clicks")


def add3():
    global buy, clicks, cnt_mes
    cnt_mes = 90
    if clicks >= 300:
        buy[3] += 1
        dlt(300)
        message.config(text="Thank you!")
        mes_auto.config(text="+{}".format(round(buy[3] * const_buy + buy[4], 1)))
    else:
        message.config(text="Not enough clicks")


def add4():
    global buy, clicks, cnt_mes
    cnt_mes = 90
    if clicks >= 5000:
        buy[4] += 1
        dlt(5000)
        message.config(text="Thank you!")
        mes_auto.config(text="+{}".format(round(buy[3] * const_buy + buy[4], 1)))
    else:
        message.config(text="Not enough clicks")


def dlt(n):
    global clicks
    clicks -= n


def new_button(*args):
    return Button(root,
                  text=args[0],
                  background=args[1],
                  foreground=args[2],
                  command=args[3]
                  )


def button_place(b, btn_x, btn_y, btn_h, btn_w):
    b.place(x=btn_x,
            y=btn_y,
            height=btn_h,
            width=btn_w
            )


def new_message(mes, mes_message, mes_x, mes_y, mes_h, mes_w):
    mes.config(text=mes_message, font="16")
    mes.place(x=mes_x,
              y=mes_y,
              height=mes_h,
              width=mes_w
              )


# само окно
root = Tk()
root.title("Clicker? Yes")
main_w = root.winfo_screenwidth()  # ширина экрана
main_h = root.winfo_screenheight()  # высота экрана
root_h = int(main_h / 2)
root_w = int(main_w / 3)
root.geometry("{}x{}".format(root_w, root_h))
root.resizable(False, False)

# инициализация кнопки "клик"
btn_click_h = int(root_h / 3)  # высота кнопки "клик"
btn_click_w = int(root_w / 3)  # ширина кнопки "клик"
click_x = int((root_w - btn_click_w) / 2)
btn_click = new_button("Click!", "#CA901B", "#000000", click, int(btn_click_h / 5))
button_place(btn_click, click_x, int((root_h - btn_click_h) / 2), btn_click_h, btn_click_w)
btn_click.config(font="{}".format(btn_click_h))

# инициализация кнопки "купить доп клик1"
btn_buy_h = int(root_h / 5)  # высота кнопки "купить доп клик1" (для остальных так же)
btn_buy_w = int((root_w - btn_click_w) / 3)  # ширина кнопки "купить доп клик1"
btn_buy_x = root_w - btn_buy_w  # координата Х кнопки
btn_buy1 = new_button("buy +0.1 per click", "#CA901B", "#000000", add1)
button_place(btn_buy1, btn_buy_x, btn_buy_h, btn_buy_h, btn_buy_w)

# инициализация кнопки "купить доп клик2"
btn_buy2 = new_button("buy +1 per click", "#CA901B", "#000000", add2)
button_place(btn_buy2, btn_buy_x, btn_buy_h * 2, btn_buy_h, btn_buy_w)

# инициализация кнопки "купить доп клик3"
btn_buy3 = new_button("buy +0.1 autoclick", "#CA901B", "#000000", add3)
button_place(btn_buy3, btn_buy_x, btn_buy_h * 3, btn_buy_h, btn_buy_w)

# инициализация кнопки "купить доп клик4"
btn_buy4 = new_button("buy +1 autoclick", "#CA901B", "#000000", add4)
button_place(btn_buy4, btn_buy_x, btn_buy_h * 4, btn_buy_h, btn_buy_w)

# отображение кол-ва кликов
count_clicks = Label(root,
                     font="16",
                     text="{}".format(round(clicks, 2))
                     )
count_clicks.place(x=click_x,
                   y=int((root_h - btn_click_h) * 7 / 20),
                   height=int((root_h - btn_click_h) / 10),
                   width=btn_click_w
                   )
# отображение сообщения для пользователя
message = Label(root,
                font="16"
                )
message.place(x=click_x,
              y=int((root_h - btn_click_h) * 5 / 20),
              height=int((root_h - btn_click_h) / 10),
              width=btn_click_w
              )
# отображение скорости нажатия
message_speed = Label(root,
                      text="+{}".format(round(buy[1] * const_buy + buy[2] + 1, 1)),
                      font="16"
                      )
message_speed.place(x=click_x,
                    y=int((root_h - btn_click_h) * 13 / 20 + btn_click_h),
                    height=int((root_h - btn_click_h) / 10),
                    width=btn_click_w
                    )
# отображение сообщения о скорости нажатия
message_speed_about = Label(root,
                            text="1 click gives you:",
                            font="16"
                            )
message_speed_about.place(x=click_x,
                          y=int((root_h - btn_click_h) * 11 / 20 + btn_click_h),
                          height=int((root_h - btn_click_h) / 10),
                          width=btn_click_w
                          )

# отображение сообщения о скорости нажатия
new_message(Label(root), "1 click gives you:",
            click_x, int((root_h - btn_click_h) * 15 / 20 + btn_click_h),
            int((root_h - btn_click_h) / 10), btn_click_w)

# отображение сообщения о скорости нажатия
mes_auto = Label(root)
new_message(mes_auto, "+{}".format(round(buy[3] * const_buy + buy[4], 1)),
            click_x, int((root_h - btn_click_h) * 17 / 20 + btn_click_h),
            int((root_h - btn_click_h) / 10), btn_click_w)

# отображение "улучшения"
new_message(Label(root), "Perks:", btn_buy_x, 0, btn_buy_h, btn_buy_w)

# отображение цены для кнопок
mes_x = click_x + btn_click_w
mes_w = btn_buy_w / 2
new_message(Label(root), "Price:", mes_x, 0, btn_buy_h, mes_w)
new_message(Label(root), "20", mes_x, btn_buy_h, btn_buy_h, mes_w)
new_message(Label(root), "120", mes_x, btn_buy_h * 2, btn_buy_h, mes_w)
new_message(Label(root), "300", mes_x, btn_buy_h * 3, btn_buy_h, mes_w)
new_message(Label(root), "5000", mes_x, btn_buy_h * 4, btn_buy_h, mes_w)

# отображение статистики
new_message(Label(root), "Stats:", 0, 0, btn_buy_h, btn_buy_w * 3 // 2)
mes_total = Label(root)
new_message(mes_total, "Total clicks: {}".format(total), 0, btn_buy_h,
            btn_buy_h / 2, btn_buy_w * 3 // 2)

root.protocol("WM_DELETE_WINDOW", on_closing)

while True:
    root.update_idletasks()
    root.update()
    time.sleep(0.01)
    if cnt_mes > 0:
        cnt_mes -= 1
    cnt += 1
    count_clicks.config(text="{}".format(round(clicks, 2)))
    mes_total.config(text="Total clicks: {}".format(total))
    if cnt_mes == 0:
        cnt_mes = -1
        message.config(text="")
    if cnt == 100:
        cnt = 0
        clicks += buy[3] * const_buy + buy[4]
