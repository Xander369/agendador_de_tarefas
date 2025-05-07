import tkinter as tk
from tkinter import messagebox
import json
import os

ARQUIVO_AGENDA = "agenda_diaria.json"
horarios = [f"{h:02d}:00" for h in range(6, 23)]
dados_agenda = {}
campos = {}

def carregar_agenda():
    global dados_agenda
    if os.path.exists(ARQUIVO_AGENDA):
        try:
            with open(ARQUIVO_AGENDA, "r", encoding="utf-8") as f:
                dados_agenda = json.load(f)
        except json.JSONDecodeError:
            messagebox.showwarning("Erro", "Arquivo corrompido. Criando novo.")
            dados_agenda = {}
    else:
        dados_agenda = {}

    for hora, entry in campos.items():
        entry.delete(0, tk.END)
        if hora in dados_agenda:
            entry.insert(0, dados_agenda[hora])

def salvar_agenda():
    for hora, entry in campos.items():
        dados_agenda[hora] = entry.get()
    try:
        with open(ARQUIVO_AGENDA, "w", encoding="utf-8") as f:
            json.dump(dados_agenda, f, ensure_ascii=False, indent=2)
        messagebox.showinfo("Sucesso", "Agenda salva com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar a agenda: {e}")

def limpar_agenda():
    for entry in campos.values():
        entry.delete(0, tk.END)
    if os.path.exists(ARQUIVO_AGENDA):
        try:
            os.remove(ARQUIVO_AGENDA)
            messagebox.showinfo("Limpeza", "Agenda limpa!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao limpar a agenda: {e}")

# Interface
janela = tk.Tk()
janela.title("Agenda Diária do Xander 💙")
janela.geometry("400x600")

frame = tk.Frame(janela)
frame.pack(pady=10)

for hora in horarios:
    tk.Label(frame, text=hora, width=8, anchor="w").grid(row=horarios.index(hora), column=0, padx=5, pady=2)
    entry = tk.Entry(frame, width=40)
    entry.grid(row=horarios.index(hora), column=1, padx=5, pady=2)
    campos[hora] = entry

tk.Button(janela, text="Salvar", command=salvar_agenda, width=15).pack(pady=10)
tk.Button(janela, text="Limpar Tudo", command=limpar_agenda, width=15).pack(pady=5)
tk.Button(janela, text="Fechar", command=janela.quit, width=15).pack(pady=5)

carregar_agenda()
janela.mainloop()
