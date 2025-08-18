import tkinter as tk
from tkinter import OptionMenu, Button, Label, ttk
from tkinter.filedialog import askopenfilename

import sv_ttk

root = tk.Tk()
root.title("Kismet Channel Configurator")

root.geometry("600x400")
root.resizable(False, False)

lbl = Label(root, text="Select a channel to configure Kismet.").pack(pady=10)
channel_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
channel_sel = tk.StringVar(value="1")

dropdownMenu = ttk.OptionMenu(root, channel_sel, *channel_options).pack(pady=10)

save_button = ttk.Button(root, text="Save", command=lambda: print(f"Selected channel: {channel_sel.get()}")).pack(pady=10)

def select_file():
    filetypes = (("Kismet files", "*.kismet"), ("All files", "*.*"))
    filename = askopenfilename(title="Open Kismet File", filetypes=filetypes)

def convert_file():
    #conversion logic goes here :)
    print("kismetdb_to_pcap --in some-kismet-log.kismet --out some-pcap-log.pcapng")

open_file_button = ttk.Button(
    root,
    text = "open a kismet file to convert", 
    command = select_file
)

open_file_button.pack(pady=10)

sv_ttk.set_theme("darK")
root.mainloop()