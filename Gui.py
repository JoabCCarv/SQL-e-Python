from tkinter import *

class Gui:
    """Classe da Interface"""
    def __init__(self):
        # Configurações gerais
        self.x_pad = 5
        self.y_pad = 3
        self.width_entry = 30

        # Criação da Janela
        self.window = Tk()
        self.window.wm_title("PYSQL versão 1.0")

        # Definição das variáveis que recebem os dados inseridos pelo usuário
        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        # Criação dos widgets
        self._create_widgets()

    def _create_widgets(self):
        """Método para criar os widgets da interface"""

        # Labels
        lblnome = Label(self.window, text='Nome')
        lblsobrenome = Label(self.window, text='Sobrenome')
        lblemail = Label(self.window, text='Email')
        lblcpf = Label(self.window, text='CPF')

        # Campos de entrada
        entNome = Entry(self.window, textvariable=self.txtNome, width=self.width_entry)
        entSobrenome = Entry(self.window, textvariable=self.txtSobrenome, width=self.width_entry)
        entEmail = Entry(self.window, textvariable=self.txtEmail, width=self.width_entry)
        entCPF = Entry(self.window, textvariable=self.txtCPF, width=self.width_entry)

        # Listbox e Scrollbar
        self.listClientes = Listbox(self.window, width=100)
        self.scrollClientes = Scrollbar(self.window)

        # Botões
        self.btnViewAll = Button(self.window, text="View All")
        self.btnBuscar = Button(self.window, text="Buscar")
        self.btnInserir = Button(self.window, text="Inserir")
        self.btnUpdate = Button(self.window, text="Update")
        self.btnDel = Button(self.window, text="Del")
        self.btnClose = Button(self.window, text="Fechar", command=self.window.destroy)

        # Layout dos widgets
        lblnome.grid(row=0, column=0)
        lblsobrenome.grid(row=1, column=0)
        lblemail.grid(row=2, column=0)
        lblcpf.grid(row=3, column=0)

        entNome.grid(row=0, column=1)
        entSobrenome.grid(row=1, column=1)
        entEmail.grid(row=2, column=1)
        entCPF.grid(row=3, column=1)

        self.listClientes.grid(row=0, column=2, rowspan=10)
        self.scrollClientes.grid(row=0, column=6, rowspan=10)

        self.btnViewAll.grid(row=4, column=0, columnspan=2)
        self.btnBuscar.grid(row=5, column=0, columnspan=2)
        self.btnInserir.grid(row=6, column=0, columnspan=2)
        self.btnUpdate.grid(row=7, column=0, columnspan=2)
        self.btnDel.grid(row=8, column=0, columnspan=2)
        self.btnClose.grid(row=9, column=0, columnspan=2)

        # Configuração do Scrollbar
        self.listClientes.configure(yscrollcommand=self.scrollClientes.set)
        self.scrollClientes.configure(command=self.listClientes.yview)

        # Aparência (SWAG)
        for child in self.window.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == 'Button':
                child.grid_configure(sticky='WE', padx=self.x_pad, pady=self.y_pad)
            elif widget_class == 'Listbox':
                child.grid_configure(padx=0, pady=0, sticky='NS')
            elif widget_class == 'Scrollbar':
                child.grid_configure(padx=0, pady=0, sticky='NS')
            else:
                child.grid_configure(padx=self.x_pad, pady=self.y_pad, sticky='N')

    def run(self):
        """Inicia o loop principal da interface"""
        self.window.mainloop()


# Executando a interface
if __name__ == "__main__":
    gui = Gui()
    gui.run()
