
import tkinter as tk
import tkinter.font as font
import sys
import pandas as pd
import random


class stock_monitor():

    def main_button(self):
        return(1)

    def quit(self):
        sys.exit()

    def refresh_button(self):
        print("here")
        self.refresh.config(image=self.live_image3)

    def motion(self,event):
        x,y = event.x,event.y
        if x%5:
            r = x%5
            x = x + (5 - r)
        for i in range(len(self.plotted_values)):
            if (self.plotted_values[i][0] == x):
                self.graph.after(100,self.graph.delete,self.pos)
                if self.plotted_values[i][1] > self.plotted_values[i+1][1]:
                    y1 = self.plotted_values[i][1] - 8
                    x2 = x-8
                    y2 = self.plotted_values[i][1]
                else:
                    y1 = self.plotted_values[i][1] + 8
                    x2 = x + 8
                    y2 = y2 = self.plotted_values[i][1]
                update_smiley = random.choice(self.smileys)
                self.smiley.config(text=update_smiley)
                self.pos = self.graph.create_oval(x,y1,x2,y2,fill="red")

    def __init__(self):

        main_window = tk.Tk()

        stocks_list = ["stock_1","stock_2",'stock_3','stock_4','stock_5','stock_6','stock_7','stock_8','stock_9','stock_10']
        value_list = ["value_1",'value_2','value_3','value_4','value_5','value_6','value_7','value_8','value_9','value_10']
        days = ["Live"+"\u2022","1 Day","3 Day","Week","Month","All"]
        self.smileys = ["😃",'😄','😅','😆','😓','😨','😩','😱']

        main_frame_left = tk.Frame(main_window,background = "black")
        main_frame_left.grid(row=0,column=0,sticky="nw")

        main_frame_center = tk.Frame(main_window,background = "black")
        main_frame_center.grid(row=0,column=1)

        main_frame_center_top = tk.Frame(main_frame_center,background = "black")
        main_frame_center_top.grid(row=0,column=0,sticky="w")

        main_frame_center_bot = tk.Frame(main_frame_center,background = "black")
        main_frame_center_bot.grid(row=1,column=0,sticky="w")

        main_frame_right = tk.Frame(main_window,background = "black")
        main_frame_right.grid(row=0,column=2,sticky="n")

        main_frame_right_top = tk.Frame(main_frame_right,background = "black")
        main_frame_right_top.grid(row=0,column=0)

        main_frame_right_bot = tk.Frame(main_frame_right,background = "black")
        main_frame_right_bot.grid(row=1,column=0)

        selection = tk.StringVar(main_frame_right_top)

        img = tk.PhotoImage(file="logo.png")
        live_image = tk.PhotoImage(file="2.png")
        self.live_image3 = tk.PhotoImage(file="3.png")

        logo = tk.Label(main_frame_left,text="logo",image= img,highlightbackground="black",bg="black",width=60,height=60)
        logo.grid(row=0,column=0)

        menu = tk.Button(main_frame_left,text="      "+"\u2630",command=self.main_button,highlightbackground="black",bg="black")
        menu.grid(row=1,column=0,pady=9,sticky="w")

        portfolio = tk.Button(main_frame_left,text="      "+"\u25D1",command=self.main_button,highlightbackground="black",bg="black")
        portfolio.grid(row=2,column=0,pady=9,sticky="w")

        portfolio = tk.Button(main_frame_left,text="      "+"\u25D1",command=self.main_button,highlightbackground="black",bg="black")
        portfolio.grid(row=3,column=0,pady=9,sticky="w")

        portfolio = tk.Button(main_frame_left,text="      "+"\u25D1",command=self.main_button,highlightbackground="black",bg="black")
        portfolio.grid(row=4,column=0,pady=9,sticky="w")

        portfolio = tk.Button(main_frame_left,text="      "+"\u25D1",command=self.main_button,highlightbackground="black",bg="black")
        portfolio.grid(row=5,column=0,pady=9,sticky="w")

        portfolio = tk.Button(main_frame_left,text="      "+"\u26CC",highlightbackground="black",bg="black",
                            command=lambda: self.quit())
        portfolio.grid(row=7,column=0,pady=9,sticky="w")

        data = pd.read_csv("data/temp.csv")
        data.columns = ["value"]

        days_dict = {}
        column=0
        for day in days:
            days_dict[day] = tk.Button(main_frame_center_top,text=day,
                                    highlightbackground="black",width=6,fg="black")
            days_dict[day].grid(row=0,column=column)
            column += 1

        self.refresh = tk.Button(main_frame_center_top,text = "Refresh",image=live_image,highlightbackground="black",bg="black",
                                            width=75,height=1,command=lambda: self.refresh_button(),fg="blue")
        self.refresh.grid(row=0,column=column,sticky="e")

        self.smiley = tk.Label(main_frame_center_top,text="😃",highlightbackground="black",bg= "black",width=4)
        self.smiley.grid(row=0,column=column+1,sticky="w")

        #blank = tk.Label(main_frame_center_top,text='',highlightbackground="black",width=6,bg="black")
        #blank.grid(row=1,column=0)

        self.graph = tk.Canvas(main_frame_center_bot, width=450, height=250,bg= "black",highlightbackground="black")
        self.graph.grid(row=2,column=0)

        self.graph.bind("<Motion>",self.motion)

        x = 5
        x_old = None
        y_old = None
        self.plotted_values = []
        for v in data.iterrows():
            y = v[1]["value"]
            #graph.create_oval(x,y,x+5,y+5,fill="white")
            if x_old:
                self.graph.create_line(x_old,y_old,x,y,fill="white",width=2)
                self.plotted_values.append((x,y))
            y_old = y
            x_old = x
            x += 5
        self.pos = self.graph.create_oval(255,27,260,32,fill="red")


        display = tk.Label(main_frame_right_top,text="Display ", bg = "black", fg = "white",highlightbackground="black")
        display.grid(row=0,column=0,sticky="w")

        stocks = tk.OptionMenu(main_frame_right_top,"one","two","three")
        stocks.config(highlightbackground="black",bg="black")
        stocks.grid(row=0,column=1)

        stocks_label = tk.Label(main_frame_right_bot,text="Stocks", bg = "black", fg = "white")
        stocks_label.grid(row=0,column=0,sticky="w")

        stock_dict = {}
        row = 1
        for stock in stocks_list:
            stock_dict[stock] =  tk.Label(main_frame_right_bot,text = stock + ":", bg = "black", fg = "white",highlightbackground="black")
            stock_dict[stock].grid(row=row,column=0,sticky="w")
            row += 1


        value_dict = {}
        row = 1
        for value in value_list:
            value_dict[value] = tk.Label(main_frame_right_bot,text = value, bg = "black", fg = "white")
            value_dict[value].grid(row=row,column=1,sticky="w")
            row += 1

        main_window.geometry("700x320")
        main_window.config(background = "black")

        main_window.mainloop()



if __name__ == "__main__":
    stock = stock_monitor()
