import wx

class Programe(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Cota Modificada", 
                        size=(1300,670), style= wx.MINIMIZE_BOX | wx.SYSTEM_MENU |
                         wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)
                        
        # BackGround Color
        self.SetBackgroundColour(wx.Colour(255,255,255))

        # Add menu
        self.creat_menu()

        # Add Panel
        self.window = Window(self)

        # Creat Values window
        self.valuesWindow = ValuesWindow()

        # Close Bind
        self.Bind(
            event=wx.EVT_CLOSE,
            handler=self.on_close
        )

        # Show app
        self.Center()
        self.Show()

    def on_close(self, event):
        self.valuesWindow.Destroy()
        self.Destroy()

    def creat_menu(self):
        menuBar = wx.MenuBar()


        # Add Ficheiro tab
        ficheiro_menu = wx.Menu()

        sair_ficheiro_menu = ficheiro_menu.Append(wx.ID_ANY, 'Sair')

        menuBar.Append(ficheiro_menu, 'Ficheiro')



        # Add Inserir tab
        inserir_menu = wx.Menu()

        valores_inserir_menu = inserir_menu.Append(wx.ID_ANY, 'Valores')
        self.Bind(
            event=wx.EVT_MENU,
            handler=self.on_valores_inserir_menu,
            source=valores_inserir_menu
        )

        menuBar.Append(inserir_menu, 'Inserir')



        # Show the menu bar
        self.SetMenuBar(menuBar)

    def on_valores_inserir_menu(self, event):
        self.valuesWindow.ShowModal()
        self.valuesWindow.Hide()

class Window(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        # BackGround Color
        self.SetBackgroundColour(wx.Colour(255,255,255))

        # Fonts
        self.font_A = wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')

class ValuesWindow(wx.Dialog):
    def __init__(self):
        super().__init__(parent=None, title='Valores', size=(655,130),
        style=wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX|wx.CLIP_CHILDREN)

        # Set the BackGroud Color
        self.SetBackgroundColour(wx.Colour(255,255,255))

class Row:
    def __init__(self, id):
        self.id = id

        self.label_1 = LabelValue(self.id, 1)
        self.label_2 = LabelValue(self.id, 2)
        self.label_3 = LabelValue(self.id, 3)
        self.label_4 = LabelValue(self.id, 4)
        self.label_5 = LabelValue(self.id, 5)
        self.label_6 = LabelValue(self.id, 6)
        self.label_7 = LabelValue(self.id, 7)
        self.label_8 = LabelValue(self.id, 8)
        self.label_9 = LabelValue(self.id, 9)
        self.label_10 = LabelValue(self.id, 10)
        self.label_11 = LabelValue(self.id, 11)
        self.label_12 = LabelValue(self.id, 12)
        self.label_13 = LabelValue(self.id, 13)
        self.label_14 = LabelValue(self.id, 14)
        self.label_15 = LabelValue(self.id, 15)
        self.label_16 = LabelValue(self.id, 16)
        self.label_17 = LabelValue(self.id, 17)
        self.label_18 = LabelValue(self.id, 18)

        self.textBox = TextBox(self.id)
        self.textBox.textBox.Bind(
            event=wx.EVT_TEXT,
            handler=self.value_update
        )

        self.value1 = 0.0
        self.value2 = 0.0
        self.value3 = 0.0
        self.value4 = 0.0
        self.value5 = 0.0
        self.value6 = 0.0
        self.value7 = 0.0
        self.value8 = 0.0
        self.value9 = 0.0
        self.value10 = 0.0
        self.value11 = 0.0
        self.value12 = 0.0
        self.value13 = 0.0
        self.value14 = 0.0
        self.value15 = 0.0
        self.value16 = 0.0
        self.value17 = 0.0
        self.value18 = 0.0

    def get_values(self):
        return {self.label_1: self.value1,
                self.label_2: self.value2,
                self.label_3: self.value3,
                self.label_4: self.value4,
                self.label_5: self.value5,
                self.label_6: self.value6,
                self.label_7: self.value7,
                self.label_8: self.value8,
                self.label_9: self.value9,
                self.label_10: self.value10,
                self.label_11: self.value11,
                self.label_12: self.value12,
                self.label_13: self.value13,
                self.label_14: self.value14,
                self.label_15: self.value15,
                self.label_16: self.value16,
                self.label_17: self.value17,
                self.label_18: self.value18}

    def clear_values(self):
        self.value1 = 0
        self.value2 = 0
        self.value3 = 0
        self.value4 = 0
        self.value5 = 0
        self.value6 = 0
        self.value7 = 0
        self.value8 = 0
        self.value9 = 0
        self.value10 = 0
        self.value11 = 0
        self.value12 = 0
        self.value13 = 0
        self.value14 = 0
        self.value15 = 0
        self.value16 = 0
        self.value17 = 0
        self.value18 = 0

    def value_update(self, event):
        try:
            self.value1 = float(self.textBox.getValue())
            self.value_cal()
            self.value_to_label()
            Extra.identify_selected()
        except:
            self.clear_values()
            Extra.identify_selected()
            if not self.textBox.getValue():
                self.clear_labels()

    def value_cal(self):
        self.value2 = round(self.value1 / 2, 3)
        self.value3 = round(self.value1 / 3, 3)
        self.value4 = round(self.value1 / 4, 3)
        self.value5 = round(self.value1 / 5, 3)
        self.value6 = round(self.value1 / 6, 3)
        self.value7 = round(self.value1 / 7, 3)
        self.value8 = round(self.value1 / 8, 3)
        self.value9 = round(self.value1 / 9, 3)
        self.value10 = round(self.value1 /10, 3)
        self.value11 = round(self.value1 /11, 3)
        self.value12 = round(self.value1 /12, 3)
        self.value13 = round(self.value1 /13, 3)
        self.value14 = round(self.value1 /14, 3)
        self.value15 = round(self.value1 /15, 3)
        self.value16 = round(self.value1 /16, 3)
        self.value17 = round(self.value1 /17, 3)
        self.value18 = round(self.value1 /18, 3)

        if self.value1.is_integer():
            self.value1 = int(self.value1)
        if self.value2.is_integer():
            self.value2 = int(self.value2)        
        if self.value3.is_integer():
            self.value3 = int(self.value3)
        if self.value4.is_integer():
            self.value4 = int(self.value4)
        if self.value5.is_integer():
            self.value5 = int(self.value5)
        if self.value6.is_integer():
            self.value6 = int(self.value6)
        if self.value7.is_integer():
            self.value7 = int(self.value7)
        if self.value8.is_integer():
            self.value8 = int(self.value8)
        if self.value9.is_integer():
            self.value9 = int(self.value9)
        if self.value10.is_integer():
            self.value10 = int(self.value10)
        if self.value11.is_integer():
            self.value11 = int(self.value11)
        if self.value12.is_integer():
            self.value12 = int(self.value12)
        if self.value13.is_integer():
            self.value13 = int(self.value13)
        if self.value14.is_integer():
            self.value14 = int(self.value14)
        if self.value15.is_integer():
            self.value15 = int(self.value15)
        if self.value16.is_integer():
            self.value16 = int(self.value16)
        if self.value17.is_integer():
            self.value17 = int(self.value17)
        if self.value18.is_integer():
            self.value18 = int(self.value18)

    def clear_labels(self):
        self.label_1.setlabel('')
        self.label_2.setlabel('')
        self.label_3.setlabel('')
        self.label_4.setlabel('')
        self.label_5.setlabel('')
        self.label_6.setlabel('')
        self.label_7.setlabel('')
        self.label_8.setlabel('')
        self.label_9.setlabel('')
        self.label_10.setlabel('')
        self.label_11.setlabel('')
        self.label_12.setlabel('')
        self.label_13.setlabel('')
        self.label_14.setlabel('')
        self.label_15.setlabel('')
        self.label_16.setlabel('')
        self.label_17.setlabel('')
        self.label_18.setlabel('')

    def value_to_label(self):
        if self.value1:
            self.label_1.setlabel(Extra.limit7(self.value1))
            self.label_2.setlabel(Extra.limit7(self.value2))
            self.label_3.setlabel(Extra.limit7(self.value3))
            self.label_4.setlabel(Extra.limit7(self.value4))
            self.label_5.setlabel(Extra.limit7(self.value5))
            self.label_6.setlabel(Extra.limit7(self.value6))
            self.label_7.setlabel(Extra.limit7(self.value7))
            self.label_8.setlabel(Extra.limit7(self.value8))
            self.label_9.setlabel(Extra.limit7(self.value9))
            self.label_10.setlabel(Extra.limit7(self.value10))
            self.label_11.setlabel(Extra.limit7(self.value11))
            self.label_12.setlabel(Extra.limit7(self.value12))
            self.label_13.setlabel(Extra.limit7(self.value13))
            self.label_14.setlabel(Extra.limit7(self.value14))
            self.label_15.setlabel(Extra.limit7(self.value15))
            self.label_16.setlabel(Extra.limit7(self.value16))
            self.label_17.setlabel(Extra.limit7(self.value17))
            self.label_18.setlabel(Extra.limit7(self.value18))

class LabelValue:
    def __init__(self, row_id, label_id):
        self.rowID = row_id
        self.labelID = label_id

        self.label = wx.StaticText(
            programe.window, label='',
            pos=(100 * self.rowID - 100, 30 * self.labelID - 15),
            size=(90,30),
            style=wx.ALIGN_CENTER
        )
        self.label.SetFont(programe.window.font_A)

    def setlabel(self, labelToInsert):
        self.label.SetLabel(str(labelToInsert))

    def purple(self):
        self.label.SetForegroundColour(wx.Colour(255,0,255))

    def white(self):
        self.label.SetForegroundColour(wx.Colour(0,0,0))

class TextBox:
    def __init__(self, row_id):
        self.rowID = row_id

        if self.rowID < 8:
            self.textBox = wx.TextCtrl(
                programe.valuesWindow,
                pos=(80 * (self.rowID - 1) + 10 * self.rowID, 10), size=(80,30)
            )
            self.textBox.SetFont(programe.window.font_A)
        else:
            self.textBox = wx.TextCtrl(
                programe.valuesWindow,
                pos=(80 * (self.rowID - 8) + 10 * (self.rowID - 7) + 50, 50), size=(80,30)
            )
            self.textBox.SetFont(programe.window.font_A)

    def getValue(self):
        return self.textBox.GetValue()

class Quantidade:
    def __init__(self):
        
        self.label = wx.StaticText(
            programe.window, label='Quantidade:',
            pos=(10,575), size=(10,20),
            style= wx.ALIGN_LEFT
        )
        self.label.SetFont(programe.window.font_A)

        self.textBox = wx.TextCtrl(
            programe.window, value='1',
            pos=(135,573), size=(80,30)
        )
        self.textBox.SetFont(programe.window.font_A)

        self.textBox.Bind(
            event=wx.EVT_TEXT,
            handler=Extra.quantidade_evt
        )

    def getValue(self):
        return self.textBox.GetValue()

class Extra:
    def __init__(self):
        self.row1 = Row(1)
        self.row2 = Row(2)
        self.row3 = Row(3)
        self.row4 = Row(4)
        self.row5 = Row(5)
        self.row6 = Row(6)
        self.row7 = Row(7)
        self.row8 = Row(8)
        self.row9 = Row(9)
        self.row10 = Row(10)
        self.row11 = Row(11)
        self.row12 = Row(12)
        self.row13 = Row(13)

        self.quantidade = Quantidade()
    
    def get_rows(self):
        return [self.row1, self.row2, self.row3, self.row4, self.row5, self.row6, self.row7, self.row8, self.row9, self.row10, self.row11, self.row12, self.row13]

    @staticmethod
    def creat_dict():
        list_rows = variables.get_rows()
        list_values = []
        for x in list_rows:
            list_values.append(x.get_values())

        return [list_rows, list_values]

    @staticmethod
    def identify_selected():
        # Get values
        temp = Extra.creat_dict()
        list_rows = temp[0]
        list_values = temp[1]

        # Clear previous
        for y in list_values:
            for x in y:
                x.white()

        # Get Biggests
        done = 0
        while done < int(variables.quantidade.getValue()):
            biggest = 0
            for y in list_values:
                for x in y:
                    if y[x] > biggest:
                        biggest = y[x]

            for y in list_values:
                for x in y:
                    if y[x] == biggest:
                        y[x] = 0
                        x.purple()
            done += 1

        for x in list_rows:
            x.clear_labels()
            x.value_to_label()

    @staticmethod
    def limit7(given):
        all = [char for char in str(given)]
        only7 = ''
        for x in range(7):
            try:
                only7 += all[x]
            except:
                pass
        return str(only7)

    @staticmethod
    def quantidade_evt(event):
        Extra.identify_selected()

if __name__ == '__main__':
    app = wx.App(False)
    programe = Programe()
    variables = Extra()
    app.MainLoop()