from tkinter import *

clicks = 0
buy_1 = 0
buy_2 = 0


def click():
    global clicks, buy_1
    clicks += 1 + buy_1 * 0.1 + buy_2
    count_clicks.config(text="{}".format(round(clicks, 1)))
    message.config(text="")


def add1():
    global buy_1, clicks
    if clicks >= 20:
        buy_1 += 1
        dlt(20)
        count_clicks.config(text="{}".format(round(clicks, 1)))
        message_speed.config(text="+{}".format(1 + buy_1 * 0.1 + buy_2))
    else:
        message.config(text="Not enough clicks")


def add2():
    global buy_2, clicks
    if clicks >= 20:
        buy_2 += 1
        dlt(130)
        count_clicks.config(text="{}".format(round(clicks, 1)))
        message_speed.config(text="+{}".format(1 + buy_1 * 0.1 + buy_2))
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


# отображение кол-ва кликов
count_clicks = Label(root,
                     font="16",
                     text="{}".format(clicks)
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

root.mainloop()
