import wx

app = wx.App()

frame = wx.Frame(None, title='python')

frame.Show()

pl = wx.Panel(frame)
pl.Show()
staticText = wx.StaticText(pl, label="huanying")
staticText.Show()

app.MainLoop()
