import datetime
import os
import sqlite3
import tkinter
import xml.etree.ElementTree
import xml.parsers.expat
import xml.sax.saxutils
from tkinter import messagebox, ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename


class AbrirWindow(tkinter.Toplevel):

    def __init__(self, parent, name=None):
        super().__init__(parent)
        self.title("Localizar Paciente")
        self.parent = parent
        self.accepted = False
        self.nameVar = tkinter.StringVar()
        if name is not None:
            self.nameVar.set(name)

        frame = tkinter.Frame(self)
        nameLabel = tkinter.Label(frame, text="Nome:", underline=0)
        nameEntry = tkinter.Entry(frame, textvariable=self.nameVar)
        nameEntry.focus_set()
        okButton = tkinter.Button(frame, text="Localizar", command=self.ok)
        cancelButton = tkinter.Button(
            frame, text="Cancelar", command=self.close)
        nameLabel.grid(row=0, column=0, sticky=tkinter.W, pady=3, padx=3)
        nameEntry.grid(row=0, column=1, columnspan=3,
                       sticky=tkinter.EW, pady=3, padx=3)
        okButton.grid(row=2, column=2, sticky=tkinter.EW, pady=3, padx=3)
        cancelButton.grid(row=2, column=3, sticky=tkinter.EW, pady=3, padx=3)
        frame.grid(row=0, column=0, sticky=tkinter.NSEW)
        frame.columnconfigure(1, weight=1)
        window = self.winfo_toplevel()
        window.columnconfigure(0, weight=1)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.close)

        self.protocol("WM_DELETE_WINDOW", self.close)
        self.grab_set()
        self.wait_window(self)

    def ok(self, event=None):
        self.name = self.nameVar.get()
        self.accepted = True
        self.close()

    def close(self, event=None):
        self.parent.focus_set()
        self.destroy()
