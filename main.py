import random
import tkinter as tk
from tkinter import ttk, messagebox

class PassGen:
    def __init__(self, root):
        self.root = root
        self.root.title('Password Generator')
        self.root.geometry('350x200')

        self.label_site = tk.Label(root, text="Site/Software:")
        self.label_site.grid(row=0, column=0, padx=10, pady=5)
        self.entry_site = tk.Entry(root)
        self.entry_site.grid(row=0, column=1, padx=10, pady=5)

        self.label_user = tk.Label(root, text="E-mail/Usuário:")
        self.label_user.grid(row=1, column=0, padx=10, pady=5)
        self.entry_user = tk.Entry(root)
        self.entry_user.grid(row=1, column=1, padx=10, pady=5)

        self.label_chars = tk.Label(root, text="Quantidade de caracteres:")
        self.label_chars.grid(row=2, column=0, padx=10, pady=5)
        self.combo_chars = ttk.Combobox(root, values=list(range(1, 31)))
        self.combo_chars.grid(row=2, column=1, padx=10, pady=5)
        self.combo_chars.current(12)  

        self.btn_generate = tk.Button(root, text="Gerar Senha", command=self.gerar_senha)
        self.btn_generate.grid(row=3, column=0, padx=10, pady=5)

        self.btn_close = tk.Button(root, text="Fechar Programa", command=self.root.quit)
        self.btn_close.grid(row=3, column=1, padx=10, pady=5)

        self.output_text = tk.Text(root, height=5, width=32)
        self.output_text.grid(row=4, column=0, columnspan=2, padx=10, pady=5)