from Gui import *  # Importa a interface gráfica
import Backend as core  # Importa o backend que manipula o banco de dados

app = None  # Inicializa a variável da interface
selected = None  # Inicializa a variável para armazenar o item selecionado


def view_command():
    """Exibe todos os registros no Listbox"""
    rows = core.view()
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)


def search_command():
    """Busca registros com base nos dados fornecidos"""
    app.listClientes.delete(0, END)
    rows = core.search(
        app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get()
    )
    for r in rows:
        app.listClientes.insert(END, r)


def insert_command():
    """Insere um novo registro no banco de dados"""
    core.insert(
        app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get()
    )
    view_command()


def update_command():
    """Atualiza o registro selecionado"""
    global selected
    if selected is not None:
        core.update(
            selected[0],
            app.txtNome.get(),
            app.txtSobrenome.get(),
            app.txtEmail.get(),
            app.txtCPF.get(),
        )
        view_command()


def del_command():
    """Deleta o registro selecionado"""
    global selected
    if selected is not None:
        core.delete(selected[0])
        view_command()


def getSelectedRow(event):
    """Obtém o item selecionado no Listbox e preenche os campos de entrada"""
    global selected
    try:
        index = app.listClientes.curselection()[0]
        selected = app.listClientes.get(index)
        app.entNome.delete(0, END)
        app.entNome.insert(END, selected[1])
        app.entSobrenome.delete(0, END)
        app.entSobrenome.insert(END, selected[2])
        app.entEmail.delete(0, END)
        app.entEmail.insert(END, selected[3])
        app.entCPF.delete(0, END)
        app.entCPF.insert(END, selected[4])
    except IndexError:
        selected = None


if __name__ == "__main__":
    app = Gui()  # Inicializa a interface gráfica

    # Associa eventos e comandos aos botões e ao Listbox
    app.listClientes.bind("<<ListboxSelect>>", getSelectedRow)
    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)

    app.run()  # Inicia o loop principal da interface gráfica