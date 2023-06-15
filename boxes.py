import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("775,775")
app.title("Sudoku")


mainframe = customtkinter.CTkFrame(master=app)
mainframe.pack(pady=80, padx=40)
boxes = customtkinter.CTkFrame(mainframe)
mainframe.grid_columnconfigure(1, weight=1)
mainframe.grid_columnconfigure((2, 3), weight=0)
mainframe.grid_rowconfigure((0, 1, 2), weight=1)


class Boxes(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        blocks = []
        for r in range(3):
            row = []
            for c in range(3):
                self.frame_1 = customtkinter.CTkFrame(
                    mainframe, border_width=10, border_color="#5D5D5D")
                self.frame_1.grid(row=r, column=c, sticky="nesw")
                row.append(self.frame_1)
            blocks.append(row)

        cells = [[None for x in range(9)] for x in range(9)]
        for i in range(9):
            for j in range(9):
                self.b_cell = customtkinter.CTkFrame(
                    blocks[i // 3][j // 3], width=75, height=75)
                self.b_cell.grid(row=(i % 3), column=(j % 3), sticky="wens")
                # forces button into squares i think?
                self.b_cell.grid_propagate(False)
                self.b_cell.rowconfigure(0, minsize=50, weight=1)
                self.b_cell.columnconfigure(0, minsize=50, weight=1)
                cells[i][j] = customtkinter.CTkEntry(
                    self.b_cell, corner_radius=0)
                cells[i][j].grid(sticky="nsew")


app.mainloop()


'''i dont know what to do
        
goals:
2. add elapsed timer 
3. figure out how to create a sudoku board with numbers in it
4. solve sudoku board and recieve 
5. make it playable'''
