import tkinter
from tkinter import messagebox
from starting_window import StartWindow

BACKGROUND_COLOR = "#f1faee"
equation_img = None


class VanTonderEquation(StartWindow):
    def __init__(self):
        super().__init__(400, 300)
        self.q_max = tkinter.Label(master=self, text="Q_max ", bg=BACKGROUND_COLOR, fg="black", font=20)
        self.s_test_entry = tkinter.Entry(master=self, bg="white", fg="black", width=25)
        self.s_max_entry = tkinter.Entry(master=self, bg="white", fg="black", width=25)
        self.q_test_entry = tkinter.Entry(master=self, bg="white", fg="black", width=25)
        self.title("Van Tonder Equation")
        self.config(bg=BACKGROUND_COLOR)


    def labels(self):
        # Van Equation Label
        van_equation = tkinter.Label(master=self, text="Van Tonder Equation = ", bg=BACKGROUND_COLOR, fg="black")
        van_equation.grid(row=0, column=1)

        # Setting up S test Label
        s_test = tkinter.Label(master=self, text="S_test: ", bg=BACKGROUND_COLOR, fg="black")
        s_test.grid(row=1, column=1, pady=10)

        # Setting up S max Label
        s_max = tkinter.Label(master=self, text="S_max: ", bg=BACKGROUND_COLOR, fg="black")
        s_max.grid(row=2, column=1, pady=10)

        # Setting up q test Label
        q_test = tkinter.Label(master=self, text="Q_test: ", bg=BACKGROUND_COLOR, fg="black")
        q_test.grid(row=3, column=1, pady=10)

        # Setting up S test Label
        self.q_max.grid(row=4, column=2)

    def entries(self):
        # S_test Entry
        self.s_test_entry.grid(row=1, column=2)
        self.s_test_entry.focus()

        # S_max Entry
        self.s_max_entry.grid(row=2, column=2)

        # S_test Entry
        self.q_test_entry.grid(row=3, column=2)

    def calculate_button(self):
        # Calculating Qmax
        calculate_button = tkinter.Button(master=self,
                                          text="Calculate Qm",
                                          bg=BACKGROUND_COLOR,
                                          fg="black",
                                          command=self.calculate_qm
                                          )
        calculate_button.grid(row=5, column=2)

    def van_equation(self):
        global equation_img
        canvas = tkinter.Canvas(master=self, width=91, height=52, highlightthickness=0)
        equation_img = tkinter.PhotoImage(master=self, file="images/ksnip_20210816-160851.png")
        canvas.create_image(45, 26, image=equation_img)
        canvas.grid(row=0, column=2)

    def calculate_qm(self):
        if self.s_test_entry.get() == "" or self.q_test_entry.get() == "" or self.s_max_entry == "":
            messagebox.showerror(master=self, title="ERROR", message="Please Fill all the fields")
        else:
            try:
                s_test = float(self.s_test_entry.get())
                s_max = float(self.s_max_entry.get())
                q_test = float(self.q_test_entry.get())
            except ValueError:
                messagebox.showerror(master=self, title="ERROR", message="Please fields should be numbers only")
            else:
                q_max = (s_max / s_test) * q_test
                self.q_max.config(text=f"Qm = {round(q_max, 4)}")
