import tkinter as tk
from tkinter import filedialog

from DataStructures import ERDiagram, Entity, Attribute, Relationship


class SquareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ER-diagram")
        self.er_diagram = ERDiagram([], [])

        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.figure_id_to_info = {}
        self.current_figure_id = None

        self.create_menu()

        self.canvas.bind("<Button-1>", self.select_figure)
        self.canvas.bind("<B1-Motion>", self.move_figure)

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Load from", command=self.load_from_file)
        file_menu.add_command(label="Save", command=self.save_current_file)
        menu_bar.add_cascade(label="File", menu=file_menu)

        menu_bar.add_command(label="Add entity", command=self.add_entity)
        menu_bar.add_command(label="Add relationship", command=self.add_relationship)

        self.root.config(menu=menu_bar)

    def select_figure(self, event):
        x, y = event.x, event.y
        item = self.canvas.find_closest(x, y)
        if item:
            self.current_figure_id = item[0]
            self.canvas.tag_raise(self.current_figure_id)

    def move_figure(self, event):
        if self.current_figure_id:
            x, y = event.x, event.y
            self.canvas.coords(self.current_figure_id, x, y, x + 50, y + 50)
            figure_info = self.figure_id_to_info[self.current_figure_id]
            text_id = figure_info[2]
            print(text_id)
            self.canvas.coords(text_id, x + 25, y + 25)

    def load_from_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.canvas.delete("all")
            self.figure_id_to_info = {}
            with open(file_path, "r") as file:
                pass

    def save_current_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                for figure_id in self.figure_id_to_info:
                    return

    def add_entity(self):
        x1, y1 = 50, 50
        x2, y2 = x1 + 50, y1 + 50
        figure_id = self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="blue")
        entity = Entity("Entity", Attribute("attr1"), Attribute("attr2"))
        text_id = self.canvas.create_text(x1 + 25, y1 + 25, text=entity.name, fill="white")
        self.figure_id_to_info[figure_id] = [entity, (x1, y1, x2, y2), text_id]

    def add_relationship(self):
        x1, y1 = 50, 50
        x2, y2 = x1 + 50, y1 + 50
        figure_id = self.canvas.create_oval(x1, y1, x2, y2, outline="black", fill="red")
        relationship = Relationship("Relation", [])
        text_id = self.canvas.create_text(x1 + 25, y1 + 25, text=relationship.name, fill="white")
        self.figure_id_to_info[figure_id] = [relationship, (x1, y1, x2, y2), text_id]


def main():
    root = tk.Tk()
    app = SquareApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()