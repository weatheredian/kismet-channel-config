import tkinter as tk
from tkinter import *
from tkinter import OptionMenu, Button, Label, ttk
from tkinter.filedialog import askopenfilename
from unittest import result
import sv_ttk
import subprocess

root = tk.Tk()
root.title("Kismet Channel Configurator")

root.geometry("600x400")
root.resizable(False, False)

tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Kismet Config')
tabControl.add(tab2, text ='Kismet to PCAP')
tabControl.pack(expand=1, fill="both")

lbl = Label(tab1, text="Select a channel to configure Kismet.").pack(pady=10)
channel_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
channel_sel = StringVar(value="1")

dropdownMenu = ttk.OptionMenu(tab1, channel_sel, *channel_options).pack(pady=10)

def save_function():
    selected_channel = channel_sel.get()
    print(f"Channel {selected_channel} selected for Kismet configuration.")
    #subprocess.call(["sh", "../shell/selector.sh", selected_channel], shell=True)
    result = subprocess.run(['../shell/selector.sh', selected_channel], capture_output=True, text=True)
    print(result.stdout)

save_button = ttk.Button(tab1, text="Save Channel Config", command=save_function).pack(pady=10)

def my_tracer(a, b, c):
   new_text = file_sel.get()
   label_text.set(new_text)

file_sel = StringVar()
file_sel.trace('w', my_tracer)

def select_file():
    filetypes = (("Kismet files", "*.kismet"), ("All files", "*.*"))
    filepath = askopenfilename(
        title="Open Kismet File", 
        initialdir="~/",
        filetypes=filetypes
    )
    if filepath:
        file_sel.set(filepath)
        print(f"Selected file: {file_sel.get()}")
        toggle_convert_visible()
    else:
        file_sel.set("no file selected")
        print("No file selected.")

open_file_button = ttk.Button(
    tab2,
    text = "open a kismet file to convert", 
    command = select_file
).pack(pady=10)

label_text = StringVar()
select_header = Label(tab2, text="Selected file:")
selected_file_label = Label(tab2, textvariable=label_text)

def toggle_convert_visible():
    if selected_file_label.winfo_viewable():
        select_header.pack_forget()
        selected_file_label.pack_forget()

    else:
        select_header.pack(pady=5)
        selected_file_label.pack(pady=5)
        convert_button.pack(pady=10)

def convert_file():
    #convert files using ../shell/convert.sh
    result = subprocess.run(['../shell/convert.sh'], capture_output=True, text=True)
    print(result.stdout)

convert_button = ttk.Button(
    tab2,
    text = "convert kismet file to pcapng",
    command = convert_file
)

sv_ttk.set_theme("dark")
root.mainloop()