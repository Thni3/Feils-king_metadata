import tkinter as tk

from tkinter import colorchooser
import configparser

CONFIG_FILE= 'config.ini' 
def save_config (color):
    config= configparser.ConfigParser() 
    config[ 'Settings'] = { 'Background_Color': color}

    with open (CONFIG_FILE, 'w') as configfile:
        config.write(configfile)

def load_config():
    config = configparser.ConfigParser() 
    config.read(CONFIG_FILE)

    if 'Settings' in config and 'Background_Color' in config['Settings']:
        return config[ 'Settings']['Background_Color']

    else:

        return 'white'

def change_bg_color(root):
    color = colorchooser.askcolor() [1]
    if color:
        root.configure (bg=color)
        save_config(color)

def main():

    #Last inn konfigurasjon 
    bg_color = load_config()

    # Opprett Tkinter-vindu

    root = tk.Tk()
    root.title("Tkinter Config Example")
    root.geometry("300x200")
    root.configure (bg=bg_color)

    # Legg til en knapp for å endre bakgrunnsfarge 
    change_color_btn = tk.Button(root, text="Endre bakgrunns farge", command=lambda: change_bg_color(root))
    change_color_btn.pack(pady=20)

    root.mainloop()

main()