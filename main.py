import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("1920x1020")
root.state('zoomed')
root.title("Training App")

label = tk.Label(root, text="Training app")
label.pack()

exercises = {"Place 1": [], "Place 2": [], "Place 3": []}

def add_training():
    add_window = tk.Toplevel(root)
    add_window.title("Add exercises")
    add_window.geometry("1920x1020")
    add_window.state("zoomed")
    add_window.title("Add exercises")

    selected_place = tk.StringVar()
    selected_place.set("Place 1")

    def add_exercise():
        exercise = add_text.get()
        place = selected_place.get()
        exercises[place].append(exercise)
        what_you_add = tk.Label(add_window, text=exercise)
        what_you_add.pack()
        add_text.delete(0, 'end')

    def save_exercises():
        place = selected_place.get()
        with open(f"{place}.txt", "w") as file:
            for exercise in exercises[place]:
                file.write(exercise + "\n")
        add_window.destroy()

    def open_saved_exercises():
        open_window = tk.Toplevel(root)
        open_window.title("Open exercises")
        open_window.geometry("1920x1020")
        open_window.state("zoomed")

        place = selected_place.get()
        with open(f"{place}.txt", "r") as file:
            saved_exercises = file.read()
        exercises_label = tk.Label(open_window, text=saved_exercises)
        exercises_label.pack()

    def delete_selected_exercises():
        delete_window = tk.Toplevel(root)
        delete_window.title("Delete exercises")
        delete_window.geometry("1920x1020")
        delete_window.state("zoomed")

        place = selected_place.get()
        selected_exercises = exercises[place]

        def delete_selected():
            selected_indices = list(exercise_listbox.curselection())
            for index in selected_indices:
                selected_exercises.pop(index)
            update_exercise_list()

        def update_exercise_list():
            exercise_listbox.delete(0, 'end')
            for exercise in selected_exercises:
                exercise_listbox.insert('end', exercise)

        exercise_listbox = tk.Listbox(delete_window, selectmode=tk.MULTIPLE)
        update_exercise_list()
        exercise_listbox.pack()

        delete_button = tk.Button(delete_window, text="Delete selected exercises", command=delete_selected)
        delete_button.pack()

    label_add_training = tk.Label(add_window, text="Exercises")
    label_add_training.pack()

    add_text = tk.Entry(add_window, width=100)
    add_text.pack()

    add_btn = tk.Button(add_window, text="Add exercise", command=add_exercise)
    add_btn.pack()

    save_btn = tk.Button(add_window, text="Save exercises", command=save_exercises)
    save_btn.pack()

    open_btn = tk.Button(add_window, text="Open saved exercises", command=open_saved_exercises)
    open_btn.pack()

    delete_btn = tk.Button(add_window, text="Delete selected exercises", command=delete_selected_exercises)
    delete_btn.pack()

    place_combobox = ttk.Combobox(add_window, textvariable=selected_place, values=list(exercises.keys()))
    place_combobox.pack()

btn = tk.Button(root, text="Add training", command=add_training)
btn.pack()

root.mainloop()
