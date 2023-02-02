import tkinter as tk
import tkinter.filedialog
import exifread

def extrair_exif():
    # Abrir diálogo de seleção de arquivo
    arquivo = tk.filedialog.askopenfilename()

    # Lendo informações Exif
    with open(arquivo, "rb") as f:
        tags = exifread.process_file(f)
        
    root.update_idletasks()
    # Mostrar informações Exif na tela
    resultado = ""
    for tag in tags.keys():
        if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
            resultado += "Key: %s, value %s\n" % (tag, tags[tag])
    root.update_idletasks()
    text_area.config(state=tk.NORMAL)
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, resultado + " ")
    text_area.config(state=tk.DISABLED)

# Inicializando a janela principal
root = tk.Tk()
root.title("Extractor de Exif")

# Criando botão para selecionar arquivo
botao = tk.Button(root, text="Selecionar Arquivo", command=extrair_exif)
botao.pack()

# Criando área de texto para exibir informações Exif
text_area = tk.Text(root, height=40, width=100, state=tk.DISABLED)
text_area.pack()

# Iniciando o loop de eventos
root.mainloop()

