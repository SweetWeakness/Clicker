import time
from tkinter import *


cnt = 0
clicks = float(0)
buy_1 = 0
buy_2 = 0
buy_3 = 0
buy_4 = 0


def click():
    global clicks, buy_1
    clicks += 1 + buy_1 * 0.1 + buy_2 + buy_3 * 0.1
    count_clicks.config(text="{}".format(round(clicks, 2)))
    message.config(text="")


def add1():
    global buy_1, clicks
    if clicks >= 20:
        buy_1 += 1
        dlt(20)
        count_clicks.config(text="{}".format(round(clicks, 1)))
        message_speed.config(text="+{}".format(1 + buy_1 * 0.1 + buy_2 + buy_3 * 0.1))
        message.config(text="Thnx m8)")
    else:
        message.config(text="Not enough clicks")


def add2():
    global buy_2, clicks
    if clicks >= 120:
        buy_2 += 1
        dlt(120)
        message.config(text="Thnx m8)")
        count_clicks.config(text="{}".format(round(clicks, 1)))
        message_speed.config(text="+{}".format(1 + buy_1 * 0.1 + buy_2 + buy_3 * 0.1))
    else:
        message.config(text="Not enough clicks")


def add3():
    global buy_3, clicks
    if clicks >= 300:
        buy_3 += 1
        dlt(300)
        message.config(text="Thnx m8)")
        message_auto_speed.config(text="+{}".format(round(buy_3 * 0.1, 1)))

    else:
        message.config(text="Not enough clicks")


def add4():
    global buy_4, clicks
    if clicks >= 5000:
        buy_4 += 1
        dlt(5000)
        message.config(text="Thnx m8)")
        message_auto_speed.config(text="+{}".format(round(buy_4 * 5, 1)))

    else:
        message.config(text="Not enough clicks")


def dlt(n):
    global clicks
    clicks -= n


# само окно
root = Tk()
root.title("Clicker? Yes")
main_w = root.winfo_screenwidth()    # ширина экрана
main_h = root.winfo_screenheight()   # высота экрана
root_h = int(main_h / 2)
root_w = int(main_w / 3)
root.geometry("{}x{}".format(root_w, root_h))
root.resizable(False, False)
# настройка кнопки "клик"
btn_click_h = int(root_h / 3)   # высота кнопки "клик"
btn_click_w = int(root_w / 3)   # ширина кнопки "клик"
btn_click = Button(root,
                   text="Click!",
                   background="#CA901B",
                   foreground="#000000",
                   command=click,
                   font="{}".format(int(btn_click_h / 5))
                   )
# расположение кнопки "клик"
btn_click.place(x=int((root_w - btn_click_w) / 2),
                y=int((root_h - btn_click_h) / 2),
                height=btn_click_h,
                width=btn_click_w
                )
# настройка кнопки "купить доп клик1"
btn_buy1_h = int(root_h / 5)   # высота кнопки "купить доп клик1"
btn_buy1_w = int((root_w - btn_click_w) / 3)  # ширина кнопки "купить доп клик1"
btn_buy1 = Button(root,
                  text="buy +0.1 per click",
                  background="#CA901B",
                  foreground="#000000",
                  command=add1,
                  )
# расположение кнопки "купить доп клик1"
btn_buy1.place(x=root_w - btn_buy1_w,
               y=0,
               height=btn_buy1_h,
               width=btn_buy1_w
               )
# настройка кнопки "купить доп клик2"
btn_buy2_h = int(root_h / 5)   # высота кнопки "купить доп клик2"
btn_buy2_w = int((root_w - btn_click_w) / 3)  # ширина кнопки "купить доп клик2"
btn_buy2 = Button(root,
                  text="buy +1 per click",
                  background="#CA901B",
                  foreground="#000000",
                  command=add2,
                  )
# расположение кнопки "купить доп клик2"
btn_buy2.place(x=root_w - btn_buy2_w,
               y=btn_buy1_h,
               height=btn_buy2_h,
               width=btn_buy2_w
               )
# настройка кнопки "купить доп клик3"
btn_buy3_h = int(root_h / 5)   # высота кнопки "купить доп клик3"
btn_buy3_w = int((root_w - btn_click_w) / 3)  # ширина кнопки "купить доп клик3"
btn_buy3 = Button(root,
                  text="buy +0.5 autoclick",
                  background="#CA901B",
                  foreground="#000000",
                  command=add3,
                  )
# расположение кнопки "купить доп клик3"
btn_buy3.place(x=root_w - btn_buy2_w,
               y=btn_buy1_h * 2,
               height=btn_buy3_h,
               width=btn_buy3_w
               )

# настройка кнопки "купить доп клик4"
btn_buy4_h = int(root_h / 5)   # высота кнопки "купить доп клик4"
btn_buy4_w = int((root_w - btn_click_w) / 3)  # ширина кнопки "купить доп клик4"
btn_buy4 = Button(root,
                  text="buy +5 autoclick",
                  background="#CA901B",
                  foreground="#000000",
                  command=add4,
                  )
# расположение кнопки "купить доп клик4"
btn_buy4.place(x=root_w - btn_buy2_w,
               y=btn_buy1_h * 3,
               height=btn_buy3_h,
               width=btn_buy3_w
               )

# отображение кол-ва кликов
count_clicks = Label(root,
                     font="16",
                     text="{}".format(round(clicks, 2))
                     )
count_clicks.place(x=int((root_w - btn_click_w) / 2),
                   y=int((root_h - btn_click_h) * 7 / 20),
                   height=int((root_h - btn_click_h) / 10),
                   width=btn_click_w
                   )
# отображение сообщения для пользователя
message = Label(root,
                font="16"
                )
message.place(x=int((root_w - btn_click_w) / 2),
              y=int((root_h - btn_click_h) * 5 / 20),
              height=int((root_h - btn_click_h) / 10),
              width=btn_click_w
              )
# отображение скорости нажатия
message_speed = Label(root,
                      text="+1.0",
                      font="16"
                      )
message_speed.place(x=int((root_w - btn_click_w) / 2),
                    y=int((root_h - btn_click_h) * 13 / 20 + btn_click_h),
                    height=int((root_h - btn_click_h) / 10),
                    width=btn_click_w
                    )
# отображение сообщения о скорости нажатия
message_speed_about = Label(root,
                            text="1 click gives you:",
                            font="16"
                            )
message_speed_about.place(x=int((root_w - btn_click_w) / 2),
                          y=int((root_h - btn_click_h) * 11 / 20 + btn_click_h),
                          height=int((root_h - btn_click_h) / 10),
                          width=btn_click_w
                          )

# отображение сообщения о скорости нажатия
message_auto = Label(root,
                     text="and auto gives:",
                     font="16"
                     )
message_auto.place(x=int((root_w - btn_click_w) / 2),
                   y=int((root_h - btn_click_h) * 15 / 20 + btn_click_h),
                   height=int((root_h - btn_click_h) / 10),
                   width=btn_click_w
)

# отображение сообщения о скорости нажатия
message_auto_speed = Label(root,
                           text="+0.0",
                           font="16"
                           )
message_auto_speed.place(x=int((root_w - btn_click_w) / 2),
                         y=int((root_h - btn_click_h) * 17/ 20 + btn_click_h),
                         height=int((root_h - btn_click_h) / 10),
                         width=btn_click_w
                         )



while True:
    root.update_idletasks()
    root.update()
    time.sleep(0.01)
    cnt += 1
    count_clicks.config(text="{}".format(round(clicks, 2)))
    if cnt == 10:
        message.config(text="")
    if cnt == 100:
        cnt = 0
        clicks += buy_3 * 0.1 + buy_4 * 5
