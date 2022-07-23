from tkinter import Tk


class StartWindow(Tk):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        super().__init__()
        self.minsize(width=self.width, height=self.height)

        # get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width / 2) - (self.width / 2)
        y = (screen_height / 2) - (self.height / 2)
        self.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))



# from sklearn.metrics import r2_score
#
# plt.plot(x,y,"+", ms=10, mec="k")
# z = np.polyfit(x, y, 1)
# y_hat = np.poly1d(z)(x)
#
# plt.plot(x, y_hat, "r--", lw=1)
# text = f"$y={z[0]:0.3f}\;x{z[1]:+0.3f}$\n$R^2 = {r2_score(y,y_hat):0.3f}$"
# plt.gca().text(0.05, 0.95, text,transform=plt.gca().transAxes,
#      fontsize=14, verticalalignment='top')