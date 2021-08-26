import wx

class ProgramFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Cota Modificada", 
                        size=(1300,670), style= wx.MINIMIZE_BOX | wx.SYSTEM_MENU |
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


        # Add the Info Part to the menu
        inserir_menu = wx.Menu()

        values_inserir_menu = inserir_menu.Append(wx.ID_ANY, 'Valores')
        self.Bind(
            event=wx.EVT_MENU,
            handler=self.on_values_menu_item,
            source=values_inserir_menu
        )


        menu_bar.Append(inserir_menu, 'Inserir')

        self.SetMenuBar(menu_bar)

    # When novo button is pressed
    def on_new_menu_item(self, event):
        print('hello world')
        # TODO

    # When sair button is pressed
    def on_sair_menu_item(self, event):
        self.Destroy()

    # When values button is pressed
    def on_values_menu_item(self, event):
        dlg = ValuesWindow()
        dlg.ShowModal()
        dlg.Destroy()

class ProgramPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        # Fonts
        self.font_D = wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        font_A = wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        font_B = wx.Font(20, wx.FONTFAMILY_SWISS, wx.NORMAL, wx.FONTWEIGHT_SEMIBOLD, False, u'Consolas')
        font_C = wx.Font(15, wx.MODERN, wx.NORMAL, wx.FONTWEIGHT_LIGHT, False, u'Consolas')

        # Generate Rows
        self.Row1 = Row(0, 1)
        self.Row2 = Row(0, 2)
        self.Row3 = Row(0, 3)
        self.Row4 = Row(0, 4)
        self.Row5 = Row(0, 5)
        self.Row6 = Row(0, 6)
        self.Row7 = Row(0, 7)
        self.Row8 = Row(0, 8)
        self.Row9 = Row(0, 9)
        self.Row10 = Row(0, 10)
        self.Row11 = Row(0, 11)
        self.Row12 = Row(0, 12)
        self.Row13 = Row(0, 13)


        # Add Label

        label_quantidade = wx.StaticText(
            self, label='Quantidade: ',
            pos=(10,575), size=(10,20), style= wx.ALIGN_LEFT
        )
        label_quantidade.SetFont(font_A)

        # Add TextBox


        # Temp
        self.textBox_quantidade = wx.TextCtrl(
            self, pos=(150,575), size=(80,30),
            style=wx.TE_RICH
        )
        self.textBox_quantidade.SetFont(font_A)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.evt_textBox_quantidade_handler,
            source=self.textBox_quantidade
        )

    def evt_textBox_quantidade_handler(self, event):
        try:
            self.Row1.update_value(self.textBox_quantidade.GetValue())
            self.Row2.update_value(self.textBox_quantidade.GetValue())
            self.Row3.update_value(self.textBox_quantidade.GetValue())
            self.Row4.update_value(self.textBox_quantidade.GetValue())
            self.Row5.update_value(self.textBox_quantidade.GetValue())
            self.Row6.update_value(self.textBox_quantidade.GetValue())
            self.Row7.update_value(self.textBox_quantidade.GetValue())
            self.Row8.update_value(self.textBox_quantidade.GetValue())
            self.Row9.update_value(self.textBox_quantidade.GetValue())
            self.Row10.update_value(self.textBox_quantidade.GetValue())
            self.Row11.update_value(self.textBox_quantidade.GetValue())
            self.Row12.update_value(self.textBox_quantidade.GetValue())
            self.Row13.update_value(self.textBox_quantidade.GetValue())
        except:
            pass

class ValuesWindow(wx.Dialog):
    def __init__(self):
        super().__init__(parent=None, title='Valores', size=(655,130),
        style=wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX|wx.CLIP_CHILDREN)

        # Set the BackGroud Color
        self.SetBackgroundColour(wx.Colour(255,255,255))

        # Add TextBoxes
        self.textBox_1 = wx.TextCtrl(
            self, pos=(10,10), size=(80,30),
            style=wx.TE_RICH
        )
        self.textBox_1.SetFont(frame.panel.font_D)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.textBox1_evt_handler,
            source=self.textBox_1
        )


        self.textBox_2 = wx.TextCtrl(
            self, pos=(100,10), size=(80,30),
            style=wx.TE_RICH
        )
        self.textBox_2.SetFont(frame.panel.font_D)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.textBox2_evt_handler,
            source=self.textBox_2
        )


        self.textBox_3 = wx.TextCtrl(
            self, pos=(190,10), size=(80,30),
            style=wx.TE_RICH
        )
        self.textBox_3.SetFont(frame.panel.font_D)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.textBox3_evt_handler,
            source=self.textBox_3
        )


        self.textBox_4 = wx.TextCtrl(
            self, pos=(280,10), size=(80,30),
            style=wx.TE_RICH
        )
        self.textBox_4.SetFont(frame.panel.font_D)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.textBox4_evt_handler,
            source=self.textBox_4
        )


        self.textBox_5 = wx.TextCtrl(
            self, pos=(370,10), size=(80,30),
            style=wx.TE_RICH
        )
        self.textBox_5.SetFont(frame.panel.font_D)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.textBox5_evt_handler,
            source=self.textBox_5
        )


        self.textBox_6 = wx.TextCtrl(
            self, pos=(460,10), size=(80,30),
            style=wx.TE_RICH
        )
        self.textBox_6.SetFont(frame.panel.font_D)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.textBox6_evt_handler,
            source=self.textBox_6
        )


        self.textBox_7 = wx.TextCtrl(
            self, pos=(550,10), size=(80,30),
            style=wx.TE_RICH
        )
        self.textBox_7.SetFont(frame.panel.font_D)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.textBox7_evt_handler,
            source=self.textBox_7
        )
        

        self.textBox_8 = wx.TextCtrl(
            self, pos=(10,50), size=(80,30),
            style=wx.TE_RICH
        )
        self.textBox_8.SetFont(frame.panel.font_D)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.textBox8_evt_handler,
            source=self.textBox_8
        )


        self.textBox_9 = wx.TextCtrl(
            self, pos=(100,50), size=(80,30),
            style=wx.TE_RICH
        )
        self.textBox_9.SetFont(frame.panel.font_D)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.textBox9_evt_handler,
            source=self.textBox_9
        )


        self.textBox_10 = wx.TextCtrl(
            self, pos=(190,50), size=(80,30),
            style=wx.TE_RICH
        )
        self.textBox_10.SetFont(frame.panel.font_D)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.textBox10_evt_handler,
            source=self.textBox_10
        )


        self.textBox_11 = wx.TextCtrl(
            self, pos=(280,50), size=(80,30),
            style=wx.TE_RICH
        )
        self.textBox_11.SetFont(frame.panel.font_D)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.textBox11_evt_handler,
            source=self.textBox_11
        )


        self.textBox_12 = wx.TextCtrl(
            self, pos=(370,50), size=(80,30),
            style=wx.TE_RICH
        )
        self.textBox_12.SetFont(frame.panel.font_D)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.textBox12_evt_handler,
            source=self.textBox_12
        )


        self.textBox_13 = wx.TextCtrl(
            self, pos=(460,50), size=(80,30),
            style=wx.TE_RICH
        )
        self.textBox_13.SetFont(frame.panel.font_D)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.textBox13_evt_handler,
            source=self.textBox_13
        )


        # Fill them
        try:
            if not frame.panel.Row1.get_value1() == 0:
                self.textBox_1.SetValue(str(frame.panel.Row1.get_value1()))
        except:
            pass


        try:
            if not frame.panel.Row2.get_value1() == 0:
                self.textBox_2.SetValue(str(frame.panel.Row2.get_value1()))
        except:
            pass


        try:
            if not frame.panel.Row3.get_value1() == 0:
                self.textBox_3.SetValue(str(frame.panel.Row3.get_value1()))
        except:
            pass


        try:
            if not frame.panel.Row4.get_value1() == 0:
                self.textBox_4.SetValue(str(frame.panel.Row4.get_value1()))
        except:
            pass


        try:
            if not frame.panel.Row5.get_value1() == 0:
                self.textBox_5.SetValue(str(frame.panel.Row5.get_value1()))
        except:
            pass

        
        try:
            if not frame.panel.Row6.get_value1() == 0:
                self.textBox_6.SetValue(str(frame.panel.Row6.get_value1()))
        except:
            pass


        try:
            if not frame.panel.Row7.get_value1() == 0:
                self.textBox_7.SetValue(str(frame.panel.Row7.get_value1()))
        except:
            pass


        try:
            if not frame.panel.Row8.get_value1() == 0:
                self.textBox_8.SetValue(str(frame.panel.Row8.get_value1()))
        except:
            pass


        try:
            if not frame.panel.Row9.get_value1() == 0:
                self.textBox_9.SetValue(str(frame.panel.Row9.get_value1()))
        except:
            pass


        try:
            if not frame.panel.Row10.get_value1() == 0:
                self.textBox_10.SetValue(str(frame.panel.Row10.get_value1()))
        except:
            pass


        try:
            if not frame.panel.Row11.get_value1() == 0:
                self.textBox_11.SetValue(str(frame.panel.Row11.get_value1()))
        except:
            pass


        try:
            if not frame.panel.Row12.get_value1() == 0:
                self.textBox_12.SetValue(str(frame.panel.Row12.get_value1()))
        except:
            pass


        try:
            if not frame.panel.Row13.get_value1() == 0:
                self.textBox_13.SetValue(str(frame.panel.Row13.get_value1()))
        except:
            pass

    def textBox1_evt_handler(self, event):
        frame.panel.Row1.update_value(self.textBox_1.GetValue())

    def textBox2_evt_handler(self, event):
        frame.panel.Row2.update_value(self.textBox_2.GetValue())

    def textBox3_evt_handler(self, event):
        frame.panel.Row3.update_value(self.textBox_3.GetValue())

    def textBox4_evt_handler(self, event):
        frame.panel.Row4.update_value(self.textBox_4.GetValue())

    def textBox5_evt_handler(self, event):
        frame.panel.Row5.update_value(self.textBox_5.GetValue())

    def textBox6_evt_handler(self, event):
        frame.panel.Row6.update_value(self.textBox_6.GetValue())

    def textBox7_evt_handler(self, event):
        frame.panel.Row7.update_value(self.textBox_7.GetValue())

    def textBox8_evt_handler(self, event):
        frame.panel.Row8.update_value(self.textBox_8.GetValue())

    def textBox9_evt_handler(self, event):
        frame.panel.Row9.update_value(self.textBox_9.GetValue())

    def textBox10_evt_handler(self, event):
        frame.panel.Row10.update_value(self.textBox_10.GetValue())

    def textBox11_evt_handler(self, event):
        frame.panel.Row11.update_value(self.textBox_11.GetValue())

    def textBox12_evt_handler(self, event):
        frame.panel.Row12.update_value(self.textBox_12.GetValue())

    def textBox13_evt_handler(self, event):
        frame.panel.Row13.update_value(self.textBox_13.GetValue())

class Row:
    def __init__(self, main_value, id):
        self.id = id
        self.main_value = main_value
        self.valueBy2 = 0.0
        self.valueBy3 = 0.0
        self.valueBy4 = 0.0
        self.valueBy5 = 0.0
        self.valueBy6 = 0.0
        self.valueBy7 = 0.0
        self.valueBy8 = 0.0
        self.valueBy9 = 0.0
        self.valueBy10 = 0.0
        self.valueBy11 = 0.0
        self.valueBy12 = 0.0
        self.valueBy13 = 0.0
        self.valueBy14 = 0.0
        self.valueBy15 = 0.0
        self.valueBy16 = 0.0
        self.valueBy17 = 0.0
        self.valueBy18 = 0.0
        self.labels_exist = False
        
    def generate_labels(self):
        if not self.labels_exist:
            # Generate the labels
            self.label_main_value = wx.StaticText(
                frame.panel, label='1',
                pos=(100 * self.id - 100,15), size=(90,30), style=wx.ALIGN_CENTER
            )

            self.label_valueBy2 = wx.StaticText(
                frame.panel, label='2',
                pos=(100 * self.id - 100,45), size=(90,30), style=wx.ALIGN_CENTER
            )

            self.label_valueBy3 = wx.StaticText(
                frame.panel, label='3',
                pos=(100 * self.id - 100,75), size=(90,30), style=wx.ALIGN_CENTER
            )

            self.label_valueBy4 = wx.StaticText(
                frame.panel, label='4',
                pos=(100 * self.id - 100,105), size=(90,30), style=wx.ALIGN_CENTER
            )

            self.label_valueBy5 = wx.StaticText(
                frame.panel, label='5',
                pos=(100 * self.id - 100,135), size=(90,30), style=wx.ALIGN_CENTER
            )

            self.label_valueBy6 = wx.StaticText(
                frame.panel, label='6',
                pos=(100 * self.id - 100,165), size=(90,30), style=wx.ALIGN_CENTER
            )

            self.label_valueBy7 = wx.StaticText(
                frame.panel, label='7',
                pos=(100 * self.id - 100,195), size=(90,30), style=wx.ALIGN_CENTER
            )

            self.label_valueBy8 = wx.StaticText(
                frame.panel, label='8',
                pos=(100 * self.id - 100,225), size=(90,30), style=wx.ALIGN_CENTER
            )

            self.label_valueBy9 = wx.StaticText(
                frame.panel, label='9',
                pos=(100 * self.id - 100,255), size=(90,30), style=wx.ALIGN_CENTER
            )

            self.label_valueBy10 = wx.StaticText(
                frame.panel, label='10',
                pos=(100 * self.id - 100,285), size=(90,30), style=wx.ALIGN_CENTER
            )

            self.label_valueBy11 = wx.StaticText(
                frame.panel, label='11',
                pos=(100 * self.id - 100,315), size=(90,30), style=wx.ALIGN_CENTER
            )

            self.label_valueBy12 = wx.StaticText(
                frame.panel, label='12',
                pos=(100 * self.id - 100,345), size=(90,30), style=wx.ALIGN_CENTER
            )

            self.label_valueBy13 = wx.StaticText(
                frame.panel, label='13',
                pos=(100 * self.id - 100,375), size=(90,30), style=wx.ALIGN_CENTER
            )

            self.label_valueBy14 = wx.StaticText(
                frame.panel, label='14',
                pos=(100 * self.id - 100,405), size=(90,30), style=wx.ALIGN_CENTER
            )

            self.label_valueBy15 = wx.StaticText(
                frame.panel, label='15',
                pos=(100 * self.id - 100,435), size=(90,30), style=wx.ALIGN_CENTER
            )

            self.label_valueBy16 = wx.StaticText(
                frame.panel, label='16',
                pos=(100 * self.id - 100,465), size=(90,30), style=wx.ALIGN_CENTER
            )

            self.label_valueBy17 = wx.StaticText(
                frame.panel, label='17',
                pos=(100 * self.id - 100,495), size=(90,30), style=wx.ALIGN_CENTER
            )

            self.label_valueBy18 = wx.StaticText(
                frame.panel, label='18',
                pos=(100 * self.id - 100,525), size=(90,30), style=wx.ALIGN_CENTER
            )

            # Set Fonts
            self.label_main_value.SetFont(frame.panel.font_D)
            self.label_valueBy2.SetFont(frame.panel.font_D)
            self.label_valueBy3.SetFont(frame.panel.font_D)
            self.label_valueBy4.SetFont(frame.panel.font_D)
            self.label_valueBy5.SetFont(frame.panel.font_D)
            self.label_valueBy6.SetFont(frame.panel.font_D)
            self.label_valueBy7.SetFont(frame.panel.font_D)
            self.label_valueBy8.SetFont(frame.panel.font_D)
            self.label_valueBy9.SetFont(frame.panel.font_D)
            self.label_valueBy10.SetFont(frame.panel.font_D)
            self.label_valueBy11.SetFont(frame.panel.font_D)
            self.label_valueBy12.SetFont(frame.panel.font_D)
            self.label_valueBy13.SetFont(frame.panel.font_D)
            self.label_valueBy14.SetFont(frame.panel.font_D)
            self.label_valueBy15.SetFont(frame.panel.font_D)
            self.label_valueBy16.SetFont(frame.panel.font_D)
            self.label_valueBy17.SetFont(frame.panel.font_D)
            self.label_valueBy18.SetFont(frame.panel.font_D)

        self.labels_exist = True

    def update_value(self, main_value):
        try:
            float(main_value)
            self.main_value = float(main_value)
        except:
            self.main_value = 0

        if self.main_value == 0:
            self.generate_labels()
            self.clear_labels()
        else:
            self.generate_labels()
            self.clear_labels()
            self.calValues()
            self.to_label_values()

    def clear_labels(self):
        self.label_main_value.SetLabel('')
        self.label_valueBy2.SetLabel('')
        self.label_valueBy3.SetLabel('')
        self.label_valueBy4.SetLabel('')
        self.label_valueBy5.SetLabel('')
        self.label_valueBy6.SetLabel('')
        self.label_valueBy7.SetLabel('')
        self.label_valueBy8.SetLabel('')
        self.label_valueBy9.SetLabel('')
        self.label_valueBy10.SetLabel('')
        self.label_valueBy11.SetLabel('')
        self.label_valueBy12.SetLabel('')
        self.label_valueBy13.SetLabel('')
        self.label_valueBy14.SetLabel('')
        self.label_valueBy15.SetLabel('')
        self.label_valueBy16.SetLabel('')
        self.label_valueBy17.SetLabel('')
        self.label_valueBy18.SetLabel('')

        self.label_main_value.SetBackgroundColour(wx.Colour(255,255,255))
        self.label_valueBy2.SetBackgroundColour(wx.Colour(255,255,255))
        self.label_valueBy3.SetBackgroundColour(wx.Colour(255,255,255))
        self.label_valueBy4.SetBackgroundColour(wx.Colour(255,255,255))
        self.label_valueBy5.SetBackgroundColour(wx.Colour(255,255,255))
        self.label_valueBy6.SetBackgroundColour(wx.Colour(255,255,255))
        self.label_valueBy7.SetBackgroundColour(wx.Colour(255,255,255))
        self.label_valueBy8.SetBackgroundColour(wx.Colour(255,255,255))
        self.label_valueBy9.SetBackgroundColour(wx.Colour(255,255,255))
        self.label_valueBy10.SetBackgroundColour(wx.Colour(255,255,255))
        self.label_valueBy11.SetBackgroundColour(wx.Colour(255,255,255))
        self.label_valueBy12.SetBackgroundColour(wx.Colour(255,255,255))
        self.label_valueBy13.SetBackgroundColour(wx.Colour(255,255,255))
        self.label_valueBy14.SetBackgroundColour(wx.Colour(255,255,255))
        self.label_valueBy15.SetBackgroundColour(wx.Colour(255,255,255))
        self.label_valueBy16.SetBackgroundColour(wx.Colour(255,255,255))
        self.label_valueBy17.SetBackgroundColour(wx.Colour(255,255,255))
        self.label_valueBy18.SetBackgroundColour(wx.Colour(255,255,255))

    def to_label_values(self):
        # 1
        temp = [char for char in str(round(self.main_value,3))]
        temp1 = ''
        for x in range(7):
            try:
                temp1 += temp[x]
            except:
                pass
        self.label_main_value.SetLabel(str(temp1))


        # 2
        temp = [char for char in str(round(self.valueBy2,3))]
        temp1 = ''
        for x in range(7):
            try:
                temp1 += temp[x]
            except:
                pass
        self.label_valueBy2.SetLabel(str(temp1))


        # 3
        temp = [char for char in str(round(self.valueBy3,3))]
        temp1 = ''
        for x in range(7):
            try:
                temp1 += temp[x]
            except:
                pass
        self.label_valueBy3.SetLabel(str(temp1))


        # 4
        temp = [char for char in str(round(self.valueBy4,3))]
        temp1 = ''
        for x in range(7):
            try:
                temp1 += temp[x]
            except:
                pass
        self.label_valueBy4.SetLabel(str(temp1))


        # 5
        temp = [char for char in str(round(self.valueBy5,3))]
        temp1 = ''
        for x in range(7):
            try:
                temp1 += temp[x]
            except:
                pass
        self.label_valueBy5.SetLabel(str(temp1))

        # 6
        temp = [char for char in str(round(self.valueBy6,3))]
        temp1 = ''
        for x in range(7):
            try:
                temp1 += temp[x]
            except:
                pass
        self.label_valueBy6.SetLabel(str(temp1))

        # 7
        temp = [char for char in str(round(self.valueBy7,3))]
        temp1 = ''
        for x in range(7):
            try:
                temp1 += temp[x]
            except:
                pass
        self.label_valueBy7.SetLabel(str(temp1))

        # 8
        temp = [char for char in str(round(self.valueBy8,3))]
        temp1 = ''
        for x in range(7):
            try:
                temp1 += temp[x]
            except:
                pass
        self.label_valueBy8.SetLabel(str(temp1))

        # 9
        temp = [char for char in str(round(self.valueBy9,3))]
        temp1 = ''
        for x in range(7):
            try:
                temp1 += temp[x]
            except:
                pass
        self.label_valueBy9.SetLabel(str(temp1))

        # 10
        temp = [char for char in str(round(self.valueBy10,3))]
        temp1 = ''
        for x in range(7):
            try:
                temp1 += temp[x]
            except:
                pass
        self.label_valueBy10.SetLabel(str(temp1))

        # 11
        temp = [char for char in str(round(self.valueBy11,3))]
        temp1 = ''
        for x in range(7):
            try:
                temp1 += temp[x]
            except:
                pass
        self.label_valueBy11.SetLabel(str(temp1))

        # 12
        temp = [char for char in str(round(self.valueBy12,3))]
        temp1 = ''
        for x in range(7):
            try:
                temp1 += temp[x]
            except:
                pass
        self.label_valueBy12.SetLabel(str(temp1))

        # 13
        temp = [char for char in str(round(self.valueBy13,3))]
        temp1 = ''
        for x in range(7):
            try:
                temp1 += temp[x]
            except:
                pass
        self.label_valueBy13.SetLabel(str(temp1))

        # 14
        temp = [char for char in str(round(self.valueBy14,3))]
        temp1 = ''
        for x in range(7):
            try:
                temp1 += temp[x]
            except:
                pass
        self.label_valueBy14.SetLabel(str(temp1))

        # 15
        temp = [char for char in str(round(self.valueBy15,3))]
        temp1 = ''
        for x in range(7):
            try:
                temp1 += temp[x]
            except:
                pass
        self.label_valueBy15.SetLabel(str(temp1))

        # 16
        temp = [char for char in str(round(self.valueBy16,3))]
        temp1 = ''
        for x in range(7):
            try:
                temp1 += temp[x]
            except:
                pass
        self.label_valueBy16.SetLabel(str(temp1))

        # 17
        temp = [char for char in str(round(self.valueBy17,3))]
        temp1 = ''
        for x in range(7):
            try:
                temp1 += temp[x]
            except:
                pass
        self.label_valueBy17.SetLabel(str(temp1))

        # 18
        temp = [char for char in str(round(self.valueBy18,3))]
        temp1 = ''
        for x in range(7):
            try:
                temp1 += temp[x]
            except:
                pass
        self.label_valueBy18.SetLabel(str(temp1))

    def calValues(self):
        self.valueBy2 = self.main_value / 2
        self.valueBy3 = self.main_value / 3
        self.valueBy4 = self.main_value / 4
        self.valueBy5 = self.main_value / 5
        self.valueBy6 = self.main_value / 6
        self.valueBy7 = self.main_value / 7
        self.valueBy8 = self.main_value / 8
        self.valueBy9 = self.main_value / 9
        self.valueBy10 = self.main_value / 10
        self.valueBy11 = self.main_value / 11
        self.valueBy12 = self.main_value / 12
        self.valueBy13 = self.main_value / 13
        self.valueBy14 = self.main_value / 14
        self.valueBy15 = self.main_value / 15
        self.valueBy16 = self.main_value / 16
        self.valueBy17 = self.main_value / 17
        self.valueBy18 = self.main_value / 18

        if self.main_value.is_integer():
            self.main_value = int(self.main_value)

        if self.valueBy2.is_integer():
            self.valueBy2 = int(self.valueBy2)

        if self.valueBy3.is_integer():
            self.valueBy3 = int(self.valueBy3)

        if self.valueBy4.is_integer():
            self.valueBy4 = int(self.valueBy4)

        if self.valueBy5.is_integer():
            self.valueBy5 = int(self.valueBy5)

        if self.valueBy6.is_integer():
            self.valueBy6 = int(self.valueBy6)

        if self.valueBy7.is_integer():
            self.valueBy7 = int(self.valueBy7)

        if self.valueBy8.is_integer():
            self.valueBy8 = int(self.valueBy8)

        if self.valueBy9.is_integer():
            self.valueBy9 = int(self.valueBy9)

        if self.valueBy10.is_integer():
            self.valueBy10 = int(self.valueBy10)

        if self.valueBy11.is_integer():
            self.valueBy11 = int(self.valueBy11)

        if self.valueBy12.is_integer():
            self.valueBy12 = int(self.valueBy12)

        if self.valueBy13.is_integer():
            self.valueBy13 = int(self.valueBy13)

        if self.valueBy14.is_integer():
            self.valueBy14 = int(self.valueBy14)

        if self.valueBy15.is_integer():
            self.valueBy15 = int(self.valueBy15)

        if self.valueBy16.is_integer():
            self.valueBy16 = int(self.valueBy16)

        if self.valueBy17.is_integer():
            self.valueBy17 = int(self.valueBy17)

        if self.valueBy18.is_integer():
            self.valueBy18 = int(self.valueBy18)

    def get_value1(self):
        return self.main_value

    def get_value2(self):
        return self.valueBy2

    def get_value3(self):
        return self.valueBy3

    def get_value4(self):
        return self.valueBy4

    def get_value5(self):
        return self.valueBy5

    def get_value6(self):
        return self.valueBy6

    def get_value7(self):
        return self.valueBy7
        
    def get_value8(self):
        return self.valueBy8

    def get_value9(self):
        return self.valueBy9

    def get_value10(self):
        return self.valueBy10

    def get_value11(self):
        return self.valueBy11

    def get_value12(self):
        return self.valueBy12

    def get_value13(self):
        return self.valueBy13

    def get_value14(self):
        return self.valueBy14

    def get_value15(self):
        return self.valueBy15

    def get_value16(self):
        return self.valueBy16

    def get_value17(self):
        return self.valueBy17

    def get_value18(self):
        return self.valueBy18

if __name__ == "__main__":
    app = wx.App(False)
    frame = ProgramFrame()
    app.MainLoop()