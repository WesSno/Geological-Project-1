import time
import tkinter
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
from sympy import Symbol, solve, Eq
from starting_window import StartWindow
from tkinter import *

BACKGROUND_COLOR = "#f1faee"
FOREGROUND = "black"
TITLE = "Cooper Jacob Equation"
equation_img = None


def fxn(x, a, b):
    return a * x ** 2 + b * x


class CooperJacobEquation(StartWindow):
    def __init__(self):
        super().__init__(550, 350)
        self.file_name_entry = Entry(master=self, bg="white", fg="black", width=30)
        self.sheet_name_entry = Entry(master=self, bg="white", fg="black", width=30)
        self.s_max_entry = Entry(master=self, bg="white", fg="black", width=30)
        self.q_label = Label(master=self, text="", bg=BACKGROUND_COLOR, fg=FOREGROUND, font=10)
        self.qm_label = Label(master=self, text="", bg=BACKGROUND_COLOR, fg=FOREGROUND, font=10)
        self.success_label = Label(master=self, text="", bg=BACKGROUND_COLOR, fg=FOREGROUND, font=10)
        self.title("Van Tonder Equation")
        self.config(bg=BACKGROUND_COLOR)
        self.title(TITLE)

    def labels(self):
        """Setting up the labels for the cooper jacob window"""
        cooper_label = Label(master=self, text="Cooper Jacobs Equation:", bg=BACKGROUND_COLOR, fg=FOREGROUND)
        cooper_label.grid(row=0, column=0, padx=10, pady=10)

        s_max = Label(master=self, text="S_max:", bg=BACKGROUND_COLOR, fg=FOREGROUND)
        s_max.grid(row=1, column=0, padx=10, pady=10)

        sheet_name = Label(master=self, text="Sheet Name:", bg=BACKGROUND_COLOR, fg=FOREGROUND)
        sheet_name.grid(row=2, column=0, padx=10, pady=10)

        file_name = Label(master=self, text="File:", bg=BACKGROUND_COLOR, fg=FOREGROUND)
        file_name.grid(row=3, column=0, padx=10, pady=10)

        self.success_label.grid(row=4, column=1, pady=10)
        self.q_label.grid(row=5, column=1)
        self.qm_label.grid(row=6, column=1)

    def cooper_equation(self):
        """Setting up the cooper equation as an image on the window"""
        global equation_img
        canvas = Canvas(master=self, width=109, height=25, highlightthickness=0)
        equation_img = PhotoImage(master=self, file="images/ksnip_20210817-100553.png")
        canvas.create_image(54, 12, image=equation_img)
        canvas.grid(row=0, column=1, padx=10, pady=10)

    def entries(self):
        """Setting up the entries on the cooper window"""
        self.s_max_entry.grid(row=1, column=1)

        self.sheet_name_entry.grid(row=2, column=1, pady=10)

        self.file_name_entry.grid(row=3, column=1, pady=10)

    def buttons(self):
        """Setting up all the buttons on the window"""
        select_btn = Button(master=self, text="Select", bg=BACKGROUND_COLOR, fg="black",
                            command=self.select_file)
        select_btn.grid(row=3, column=2)

        calculate_btn = Button(master=self, text="Calculate", bg=BACKGROUND_COLOR, fg="black", command=self.calculate)
        calculate_btn.grid(row=7, column=0)

        reset_btn = Button(master=self, text="Reset", bg=BACKGROUND_COLOR, fg="black", command=self.reset)
        reset_btn.grid(row=7, column=2)

    def select_file(self):
        """Function for selecting the file"""
        # Opening the file dialog box
        filename = filedialog.askopenfilename(master=self, filetypes=[("Excel", "*xlsx"), ("Excel", "*xls")])
        # Loading the progress bar
        if filename:
            is_ok = messagebox.askokcancel(master=self, title="File", message="Please is this the file you want")
            if is_ok:
                pb1 = Progressbar(
                    master=self,
                    orient="horizontal",
                    length=400,
                    mode='determinate'
                )
                pb1.grid(row=4, columnspan=4, pady=20)
                for i in range(11):
                    self.update_idletasks()
                    pb1['value'] += 10
                    time.sleep(1)
                pb1.destroy()
                self.success_label.config(text='File Uploaded Successfully!',
                                          bg=BACKGROUND_COLOR, fg="black", font=10)

                self.file_name_entry.insert(index=0, string=filename)

    def calculate(self):
        """Function for plotting the graph and calculating the Q and Q_m"""
        try:
            s_max = float(self.s_max_entry.get())
        except ValueError:
            messagebox.showerror(master=self, title="error", message="S_max field should be a number")
        else:

            if len(self.s_max_entry.get()) > 0 and len(self.file_name_entry.get()) > 0 and len(
                    self.sheet_name_entry.get()):
                sheet_name = self.sheet_name_entry.get()
                filename = self.file_name_entry.get()

                try:
                    data = pd.read_excel(filename, sheet_name=sheet_name)
                except ValueError as error:
                    messagebox.showerror(master=self, title="Error", message=error)
                else:
                    df = data.dropna(subset=(["s", "Q"]))
                    q_values = np.array(df["Q"].tolist())
                    s_values = np.array(df["s"].tolist())

                    # Plotting the graph
                    plt.scatter(q_values, s_values)
                    plt.xlabel("Q(L/min)")
                    plt.ylabel("s(m)")


                    # Plotting The TrendLine
                    popt, popc = curve_fit(fxn, q_values, s_values)
                    s_hat = fxn(q_values, *popt)
                    plt.plot(q_values, s_hat, "r--", lw=1)
                    text = f"$y={popt[0]:0.4f}\;x^2{popt[1]:+0.4f}\;x$\n$R^2 = {r2_score(s_values, s_hat):0.3f}$"
                    plt.gca().text(0.05, 0.95, text, transform=plt.gca().transAxes,
                                   fontsize=14, verticalalignment='top')
                    plt.grid()


                    #Calculating for Qm using the symbols module
                    Qm = Symbol("Qm")
                    equation = Eq(s_max, popt[0] * Qm ** 2 + popt[1] * Qm)
                    roots = solve(equation, Qm)
                    positive_roots = roots[1]

                    self.q_label.config(text=f"Q = {round(positive_roots, 1)}L/mins")

                    q_max = positive_roots * 1.44

                    self.qm_label.config(text=f"Qm = {round(q_max, 1)}m\u00b3/day")
                    plt.show()

            else:
                messagebox.showerror(title="Error", message="All fields should not be empty")

    def reset(self):
        """Function for resetting every label and entry value on the window"""
        self.qm_label.config(text="")
        self.q_label.config(text="")
        self.success_label.config(text="")

        self.s_max_entry.delete(first=0, last=tkinter.END)
        self.sheet_name_entry.delete(first=0, last=tkinter.END)
        self.file_name_entry.delete(first=0, last=tkinter.END)
        self.s_max_entry.focus()
