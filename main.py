import wx

class ProgramFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Cota Modificada", 
                        size=(1000,670), style= wx.MINIMIZE_BOX | wx.SYSTEM_MENU |
                         wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)
        # Set BackGroud Color
        self.SetBackgroundColour("WHITE")
        
        # Add the menu
        self.creat_menu()

        # Add the main Panel
        self.panel = ProgramPanel(self)

        self.Centre()
        self.Show()

    # Create the menu
    def creat_menu(self):
        menu_bar = wx.MenuBar()

        # Add the Ficheiro Part to the menu
        ficheiro_menu = wx.Menu()

        new_menu_item = ficheiro_menu.Append(wx.ID_ANY, "Novo")
        self.Bind(
            event=wx.EVT_MENU,
            handler=self.on_new_menu_item,
            source=new_menu_item
        )

        sair_menu_item = ficheiro_menu.Append(wx.ID_ANY, "Sair")
        self.Bind(
            event=wx.EVT_MENU,
            handler=self.on_sair_menu_item,
            source=sair_menu_item
        )
        menu_bar.Append(ficheiro_menu, "Ficheiro")

        self.SetMenuBar(menu_bar)

    # When novo button is pressed
    def on_new_menu_item(self, event):
        print('hello world')
        # TODO

    # When sair button is pressed
    def on_sair_menu_item(self, event):
        self.Destroy()


class ProgramPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)


if __name__ == "__main__":
    app = wx.App(False)
    frame = ProgramFrame()
    app.MainLoop()