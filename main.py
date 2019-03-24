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
        message_auto_speed.config(text="+{}".format(round(buy[3] * const_buy + buy[4], 1)))
    else:
        message.config(text="Not enough clicks")


def add4():
    global buy, clicks, cnt_mes
    cnt_mes = 90
    if clicks >= 5000:
        buy[4] += 1
        dlt(5000)
        message.config(text="Thank you!")
        message_auto_speed.config(text="+{}".format(round(buy[3] * const_buy + buy[4], 1)))
    else:
        message.config(text="Not enough clicks")


def dlt(n):
    global clicks
    clicks -= n


# само окно
root = Tk()
root.title("Clicker? Yes")
main_w = root.winfo_screenwidth()  # ширина экрана
main_h = root.winfo_screenheight()  # высота экрана
root_h = int(main_h / 2)
root_w = int(main_w / 3)
root.geometry("{}x{}".format(root_w, root_h))
root.resizable(False, False)
# настройка кнопки "клик"
btn_click_h = int(root_h / 3)  # высота кнопки "клик"
btn_click_w = int(root_w / 3)  # ширина кнопки "клик"
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
btn_buy1_h = int(root_h / 5)  # высота кнопки "купить доп клик1"
btn_buy1_w = int((root_w - btn_click_w) / 3)  # ширина кнопки "купить доп клик1"
btn_buy1 = Button(root,
                  text="buy +0.1 per click",
                  background="#CA901B",
                  foreground="#000000",
                  command=add1,
                  )
# расположение кнопки "купить доп клик1"
btn_buy1.place(x=root_w - btn_buy1_w,
               y=btn_buy1_h,
               height=btn_buy1_h,
               width=btn_buy1_w
               )
# настройка кнопки "купить доп клик2"
btn_buy2_h = int(root_h / 5)  # высота кнопки "купить доп клик2"
btn_buy2_w = int((root_w - btn_click_w) / 3)  # ширина кнопки "купить доп клик2"
btn_buy2 = Button(root,
                  text="buy +1 per click",
                  background="#CA901B",
                  foreground="#000000",
                  command=add2,
                  )
# расположение кнопки "купить доп клик2"
btn_buy2.place(x=root_w - btn_buy2_w,
               y=btn_buy1_h * 2,
               height=btn_buy2_h,
               width=btn_buy2_w
               )
# настройка кнопки "купить доп клик3"
btn_buy3_h = int(root_h / 5)  # высота кнопки "купить доп клик3"
btn_buy3_w = int((root_w - btn_click_w) / 3)  # ширина кнопки "купить доп клик3"
btn_buy3 = Button(root,
                  text="buy +0.1 autoclick",
                  background="#CA901B",
                  foreground="#000000",
                  command=add3,
                  )
# расположение кнопки "купить доп клик3"
btn_buy3.place(x=root_w - btn_buy2_w,
               y=btn_buy1_h * 3,
               height=btn_buy3_h,
               width=btn_buy3_w
               )

# настройка кнопки "купить доп клик4"
btn_buy4_h = int(root_h / 5)  # высота кнопки "купить доп клик4"
btn_buy4_w = int((root_w - btn_click_w) / 3)  # ширина кнопки "купить доп клик4"
btn_buy4 = Button(root,
                  text="buy +1 autoclick",
                  background="#CA901B",
                  foreground="#000000",
                  command=add4,
                  )
# расположение кнопки "купить доп клик4"
btn_buy4.place(x=root_w - btn_buy2_w,
               y=btn_buy1_h * 4,
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
                      text="+{}".format(round(buy[1] * const_buy + buy[2] + 1, 1)),
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
                           text="+{}".format(round(buy[3] * const_buy + buy[4], 1)),
                           font="16"
                           )
message_auto_speed.place(x=int((root_w - btn_click_w) / 2),
                         y=int((root_h - btn_click_h) * 17 / 20 + btn_click_h),
                         height=int((root_h - btn_click_h) / 10),
                         width=btn_click_w
                         )
# отображение "улучшения"
message_perks = Label(root,
                      text="Perks:",
                      font="16"
                      )
message_perks.place(x=root_w - btn_buy2_w,
                    y=0,
                    height=btn_buy2_h,
                    width=btn_buy2_w
                    )
# отображение "цена"
message_perks = Label(root,
                      text="Price:",
                      font="16"
                      )
message_perks.place(x=root_w - btn_buy2_w * 3 // 2,
                    y=0,
                    height=btn_buy2_h,
                    width=btn_buy2_w / 2
                    )
# отображение "20"
message_perks_20 = Label(root,
                         text="20",
                         font="16"
                         )
message_perks_20.place(x=root_w - btn_buy2_w * 3 // 2,
                       y=btn_buy1_h,
                       height=btn_buy2_h,
                       width=btn_buy2_w / 2
                       )
# отображение "120"
message_perks_120 = Label(root,
                          text="120",
                          font="16"
                          )
message_perks_120.place(x=root_w - btn_buy2_w * 3 // 2,
                        y=btn_buy1_h * 2,
                        height=btn_buy2_h,
                        width=btn_buy2_w / 2
                        )
# отображение "300"
message_perks_300 = Label(root,
                          text="300",
                          font="16"
                          )
message_perks_300.place(x=root_w - btn_buy2_w * 3 // 2,
                        y=btn_buy1_h * 3,
                        height=btn_buy2_h,
                        width=btn_buy2_w / 2
                        )
# отображение "300"
message_perks_5000 = Label(root,
                           text="5000",
                           font="16"
                           )
message_perks_5000.place(x=root_w - btn_buy2_w * 3 // 2,
                         y=btn_buy1_h * 4,
                         height=btn_buy2_h,
                         width=btn_buy2_w / 2
                         )
# отображение "statistic"
message_stats = Label(root,
                      text="Stats:",
                      font="16"
                      )
message_stats.place(x=0,
                    y=0,
                    height=btn_buy2_h,
                    width=btn_buy2_w * 3 // 2
                    )
# отображение "total clicks"
message_total = Label(root,
                      text="Total clicks: {}".format(total),
                      font="16"
                      )
message_total.place(x=0,
                    y=btn_buy1_h,
                    height=btn_buy2_h / 2,
                    width=btn_buy2_w * 3 // 2
                    )

root.protocol("WM_DELETE_WINDOW", on_closing)

while True:
    root.update_idletasks()
    root.update()
    time.sleep(0.01)
    if cnt_mes > 0:
        cnt_mes -= 1
    cnt += 1
    count_clicks.config(text="{}".format(round(clicks, 2)))
    message_total.config(text="Total clicks: {}".format(total))
    if cnt_mes == 0:
        cnt_mes = -1
        message.config(text="")
    if cnt == 100:
        cnt = 0
        clicks += buy[3] * const_buy + buy[4]
