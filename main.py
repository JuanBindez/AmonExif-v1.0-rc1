# Release: v1.0.0-rc2
#
# Copyright (c) 2023  Juan Bindez  <juanbindez780@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#  
# repo: https://github.com/juanBindez


import tkinter as tk
from tkinter import *
import tkinter.filedialog
import exifread


def extract_exif():
    """extract exif file"""
    # Abrir diálogo de seleção de arquivo
    arquivo = tk.filedialog.askopenfilename()

    # Lendo informações Exif
    with open(arquivo, "rb") as f:
        tags = exifread.process_file(f)
        
    window.update_idletasks()
    # Mostrar informações Exif na tela
    resultado = ""
    for tag in tags.keys():
        if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
            resultado += "Key: %s, value %s\n" % (tag, tags[tag])
    window.update_idletasks()
    text_area.config(state=tk.NORMAL)
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, resultado + " ")
    text_area.config(state=tk.DISABLED)


window = tk.Tk()
window.title("Amon")
window.geometry("600x600")           
window.resizable(True, True)

botao = tk.Button(window, text="Selecionar Arquivo", command=extract_exif,state=NORMAL, relief=GROOVE, cursor="hand2")
botao.pack()

text_area = tk.Text(window, height=40, width=100, state=tk.DISABLED)
text_area.pack()

if __name__ == "__main__":
    window.mainloop()
