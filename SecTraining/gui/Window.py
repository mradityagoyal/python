import tkinter as tk
from PIL import Image, ImageTk
import DataReader

class Window(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.mappings = DataReader.getMapping()




    def init_window(self):
        # changing the title of our master widget
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=tk.BOTH, expand=1)

        # # creating a button instance
        # quitButton = tk.Button(self, text="Quit", command = lambda : print('Hi'))
        #
        # # placing the button on my window
        # quitButton.place(x=0, y=0)

        # creating a menu instance
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = tk.Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)


        # create the file object)
        edit = tk.Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        # edit.add_command(label="Show Img", command=self.showImg())
        edit.add_command(label="Show Text", command=self.showText)

        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)

        label = tk.Label(self, text="FilterWords").grid(row=0)
        entry = tk.Entry(self)
        self.entry = entry
        entry.grid(row=0, column=1)
        entry.bind('<Key>',self.filter_by_input)

    def filter_by_input(self,  key):
        words = self.entry.get().strip().lower().split()
        print('words : %r'%words)
        files = DataReader.files_with_words(words, self.mappings)
        print(files)
        x = 0
        y = 100
        for file in files:
            self.showImg(file, x, y)
            y+=500


    def showImg(self, filename, x, y):
        load = Image.open(filename)
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=x, y=y)


    def showText(self):
        text = tk.Label(self, text="Hey there good lookin!")
        text.pack()


    def client_exit(self):
        exit()




root = tk.Tk()
root.geometry("2000x1200")
app = Window(root)
root.mainloop()