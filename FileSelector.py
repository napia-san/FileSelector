import wx

global button_exe
global frame
global files

#####################################################################################
#  ＧＵＩと処理の呼び出し                                                             #
#####################################################################################
"""ファイル指定と判定"""
class FileDropTarget(wx.FileDropTarget):

    global files

    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, files): # 'files'がファイルパスのリスト
        global button_exe
        # print(files)
        
        # データ形式判定
        for p in files:
            if 'csv' not in p:
                wx.MessageBox(u'csv形式ファイルのみ対応しています．', u'ERROR', wx.ICON_ERROR)
            else:
                self.window.list_entry.SetItems(files)
                button_exe.Enable()
        return 0


"""GUIと処理の呼び出し"""
# 基礎
class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, 'Data detector', size=(700, 600))
        root_panel = wx.Panel(self, wx.ID_ANY)
        io_panel = IoPanel(root_panel)
        ctrl_panel = CtrlPanel(root_panel)

        root_layout = wx.BoxSizer(wx.VERTICAL)
        root_layout.Add(io_panel, 0, wx.GROW | wx.ALL, border=5)
        root_layout.Add(ctrl_panel, 0, wx.GROW | wx.ALL, border=5)
        root_panel.SetSizer(root_layout)
        root_layout.Fit(root_panel)

# DDエリアとデータリスト表示
class IoPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, wx.ID_ANY)

        # DDエリア
        label = wx.StaticText(self, wx.ID_ANY, '\nDrop files here.\nOnly csv files are available.', style=wx.SIMPLE_BORDER | wx.TE_CENTER, size=(690,110))
        label.SetBackgroundColour('#4169e1')
        label.SetForegroundColour('#f5f5f5')
        font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        label.SetFont(font)

        # ドロップ対象の設定
        label.SetDropTarget(FileDropTarget(self))

        # 読み込みデータリスト
        initial = ('-Drag and drop files-','')
        self.list_entry = wx.ListBox(self, wx.ID_ANY, size=(690,340), choices=initial, style=wx.LB_HSCROLL | wx.LB_NEEDED_SB)
        font_list = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.list_entry.SetFont(font_list)

        # レイアウト
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(label, flag=wx.EXPAND | wx.ALL, border=10, proportion=1)
        layout.Add(self.list_entry, flag=wx.EXPAND | wx.ALL, border=10)
        self.SetSizer(layout)

#ボタン
class CtrlPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, wx.ID_ANY)
        global button_exe

        # Executeボタン
        button_exe = wx.Button(self, wx.ID_ANY, 'Execute', size=(100,30))
        button_exe.Disable() # 何も入力がなければグレーアウト

        # Cancelボタン
        button_cl = wx.Button(self, wx.ID_ANY, 'Cancel', size=(100,30))

        # レイアウト
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(button_exe, flag=wx.GROW)
        layout.Add(button_cl, flag=wx.GROW)
        self.SetSizer(layout)

        # ボタン押下イベント(関数呼び出し)
        button_exe.Bind(wx.EVT_BUTTON, self.click_exe)
        button_cl.Bind(wx.EVT_BUTTON, self.click_cl)

    # ボタン押下イベント(関数)
    def click_exe(self, event):
        global frame
        DataOpener
        frame.Close()
    
    def click_cl(self, event):
        global frame
        frame.Close()

app = wx.App()
frame = MainFrame()
frame.Show()
app.MainLoop()
