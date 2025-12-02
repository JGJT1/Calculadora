"""GUI da calculadora usando Tkinter (substitui PySimpleGUI).

Usa a função `eval_expr` de `calculator.py` para avaliar expressões com segurança.
"""
import tkinter as tk
from tkinter import messagebox

from calculator import eval_expr


class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.resizable(False, False)

        self.entry_var = tk.StringVar()
        entry = tk.Entry(self, textvariable=self.entry_var, justify='right', font=('Segoe UI', 16), width=20)
        entry.grid(row=0, column=0, columnspan=4, padx=8, pady=8)
        entry.focus()

        buttons = [
            ('7','8','9','/'),
            ('4','5','6','*'),
            ('1','2','3','-'),
            ('0','.','%','+'),
        ]

        for r, row in enumerate(buttons, start=1):
            for c, ch in enumerate(row):
                b = tk.Button(self, text=ch, width=5, height=2, command=lambda ch=ch: self._append(ch))
                b.grid(row=r, column=c, padx=2, pady=2)

        btn_clear = tk.Button(self, text='C', width=5, height=2, command=self.clear)
        btn_clear.grid(row=5, column=0, padx=2, pady=2)

        btn_back = tk.Button(self, text='⌫', width=5, height=2, command=self.back)
        btn_back.grid(row=5, column=1, padx=2, pady=2)

        btn_l = tk.Button(self, text='(', width=5, height=2, command=lambda: self._append('('))
        btn_l.grid(row=5, column=2, padx=2, pady=2)

        btn_r = tk.Button(self, text=')', width=5, height=2, command=lambda: self._append(')'))
        btn_r.grid(row=5, column=3, padx=2, pady=2)

        btn_eq = tk.Button(self, text='=', width=22, height=2, command=self.calculate)
        btn_eq.grid(row=6, column=0, columnspan=4, padx=2, pady=8)

        # Bind keys
        self.bind('<Return>', lambda e: self.calculate())
        self.bind('<BackSpace>', lambda e: self.back())

    def _append(self, ch: str):
        cur = self.entry_var.get() or ''
        self.entry_var.set(cur + str(ch))

    def clear(self):
        self.entry_var.set('')

    def back(self):
        cur = self.entry_var.get() or ''
        self.entry_var.set(cur[:-1])

    def calculate(self):
        expr = self.entry_var.get() or ''
        try:
            result = eval_expr(expr)
            self.entry_var.set(str(result))
        except Exception as e:
            messagebox.showerror('Erro', str(e))


def main():
    app = CalculatorApp()
    app.mainloop()


if __name__ == '__main__':
    main()
