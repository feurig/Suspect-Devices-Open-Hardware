#!/usr/bin/env python
"""
    Copyright 2013 Donald Delmar Davis, Suspect Devices, All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
        notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
        notice, this list of conditions and the following disclaimer in the
        documentation and/or other materials provided with the distribution.
    * Neither the name of the <organization> nor the
        names of its contributors may be used to endorse or promote products
        derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import wx
import wx.lib.buttons

[wxID_FRAME1, wxID_FRAME1BLAH1, wxID_FRAME1BLAH2, wxID_FRAME1RACER1, 
 wxID_FRAME1RACER1SPEED, wxID_FRAME1RACER1STATUS, wxID_FRAME1RACER1STATUS, 
 wxID_FRAME1RACER2, wxID_FRAME1SLIDER2, wxID_FRAME1STARTBUTTON, 
 wxID_FRAME1STOPBUTTON, 
] = [wx.NewId() for _init_ctrls in range(11)]

class Frame1(wx.Frame):

    #def create(parent):
    #    return Frame1(parent)
    

    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer0 = wx.BoxSizer(orient=wx.VERTICAL)
        self.boxSizer1 = wx.BoxSizer(orient=wx.HORIZONTAL)
        self.boxSizer0.AddSizer(self.boxSizer1)

        self.boxSizer2 = wx.BoxSizer(orient=wx.VERTICAL)
        self.boxSizer1.AddSizer(self.boxSizer2,border=1,flag=wx.EXPAND)
        
        self.boxSizer2.AddWindow(self.racer1, 0, border=0, flag=0)
        self.boxSizer2.AddWindow(self.racer1Speed, 0, border=0, flag=0)
        self.boxSizer2.AddWindow(self.racer1Status, 0, border=0, flag=0)
        self.boxSizer3 = wx.BoxSizer(orient=wx.VERTICAL)
        self.boxSizer1.AddSizer(self.boxSizer3)
        self.boxSizer3.AddWindow(self.racer2, 0, border=0, flag=0)
        self.boxSizer3.AddWindow(self.racer2Speed, 0, border=0, flag=0)
        self.boxSizer3.AddWindow(self.racer2Status, 0, border=0, flag=0)
        self.boxSizer4 = wx.BoxSizer(orient=wx.HORIZONTAL)
        self.boxSizer0.AddSizer(self.boxSizer4)
        self.boxSizer4.AddWindow(self.startButton, 0, border=10, flag=wx.EXPAND|wx.ALL)
        self.boxSizer4.AddWindow(self.stopButton, 0, border=10, flag=wx.EXPAND|wx.ALL)
        self.SetAutoLayout(True)
        self.SetSizer(self.boxSizer0)
        self.Layout()
        self.Fit()


    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=None,
              pos=wx.Point(535, 23), size=wx.Size(960, 527),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self.panel=wx.Panel(self)
        self.SetClientSize(wx.Size(960, 505))

        self.racer1 = wx.StaticText(id=wxID_FRAME1RACER1, label=u'racer #1',
              name=u'racer1', parent=self, pos=wx.Point(0, 0), size=wx.Size(57,
              17), style=0)
        self.racer1.SetLabelText(u'racer #1')

        self.racer2 = wx.StaticText(id=wxID_FRAME1RACER2, label=u'racer #2',
              name=u'racer2', parent=self, pos=wx.Point(0, 17), size=wx.Size(75,
              17), style=0)

        self.racer1Speed = wx.Slider(id=wxID_FRAME1RACER1SPEED, maxValue=100,
              minValue=0, name=u'racer1Speed', parent=self, pos=wx.Point(0, 34),
              size=wx.Size(21, 150), style=wx.SL_HORIZONTAL, value=0)
        self.racer1Speed.SetLabel(u'')
        self.racer1Speed.Bind(wx.EVT_SCROLL_THUMBRELEASE,
              self.OnRacer1SpeedScrollThumbrelease)
        self.racer1Speed.Bind(wx.EVT_SCROLL_PAGEDOWN,
              self.OnRacer1SpeedScrollPagedown)
        self.racer1Speed.Bind(wx.EVT_SCROLL_PAGEUP,
              self.OnRacer1SpeedScrollPageup)
        self.racer1Speed.Bind(wx.EVT_SCROLL_THUMBTRACK,
              self.OnRacer1SpeedScrollThumbtrack)
        self.racer1Speed.Bind(wx.EVT_KEY_UP, self.OnRacer1SpeedKeyUp)
        self.racer1Speed.Bind(wx.EVT_KEY_DOWN, self.OnRacer1SpeedKeyDown)

        self.racer2Speed = wx.Slider(id=wxID_FRAME1SLIDER2, maxValue=100,
              minValue=0, name='racer2Speed', parent=self, pos=wx.Point(0, 184),
              size=wx.Size(21, 150), style=wx.SL_HORIZONTAL, value=14)
        self.racer2Speed.SetLabel(u'')
        self.racer2Speed.Bind(wx.EVT_SCROLL_THUMBRELEASE,
              self.OnRacer2speedScrollThumbrelease)
        self.racer2Speed.Bind(wx.EVT_SCROLL_THUMBTRACK,
              self.OnRacer2speedScrollThumbtrack)
        self.racer2Speed.Bind(wx.EVT_SCROLL_PAGEDOWN, self.OnRacer2speedScrollPagedown)
        self.racer2Speed.Bind(wx.EVT_SCROLL_PAGEUP, self.OnRacer2speedScrollPageup)
        self.racer2Speed.Bind(wx.EVT_KEY_UP, self.OnRacer2speedKeyUp)
        self.racer2Speed.Bind(wx.EVT_KEY_DOWN, self.OnRacer2speedKeyDown)

        self.racer1Status = wx.Gauge(id=wxID_FRAME1RACER1STATUS,
              name=u'racer1Status', parent=self, pos=wx.Point(0, 334),
              range=100, size=wx.Size(200, 16), style=wx.GA_HORIZONTAL)
        self.racer1Status.SetInitialSize(wx.Size(200, 16))
        self.racer1Status.SetToolTipString(u'racer1Status')

        self.racer2Status = wx.Gauge(id=wxID_FRAME1RACER1STATUS,
              name=u'racer2Status', parent=self, pos=wx.Point(0, 350),
              range=100, size=wx.Size(200, 16), style=wx.GA_HORIZONTAL)
        self.racer2Status.SetInitialSize(wx.Size(200, 16))
        self.racer2Status.SetToolTipString(u'racer2Status')

        self.startButton = wx.lib.buttons.GenButton(id=wxID_FRAME1STARTBUTTON,
              label=u'start', name=u'startButton', parent=self, pos=wx.Point(0,
              366), size=wx.Size(86, 27), style=0)
        self.startButton.SetToolTipString(u'Start Button')

        self.stopButton = wx.lib.buttons.GenButton(id=wxID_FRAME1STOPBUTTON,
              label=u'stop', name=u'stopButton', parent=self, pos=wx.Point(0,
              393), size=wx.Size(86, 27), style=0)
        self.stopButton.SetLabelText(u'stopButton')
        self.stopButton.SetHelpText(u'stop it!')
        self.stopButton.SetToolTipString(u'Stop Button')
        self.stopButton.Bind(wx.EVT_BUTTON, self.OnStopButtonButton,
              id=wxID_FRAME1STOPBUTTON)

        self.blah1 = wx.StaticText(id=wxID_FRAME1BLAH1, label=u'blah',
              name=u'blah1', parent=self, pos=wx.Point(0, 0), size=wx.Size(57,
              17), style=0)
        self.blah1.SetLabelText(u'racer #1')

        self.blah2 = wx.StaticText(id=wxID_FRAME1BLAH2, label=u'blah',
              name=u'blah2', parent=self, pos=wx.Point(0, 0), size=wx.Size(57,
              17), style=0)
        self.blah2.SetLabelText(u'racer #1')

        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)
        

    def OnRacer1SpeedScrollThumbrelease(self, event):
        
        event.Skip()

    def OnRacer1SpeedScrollPagedown(self, event):
        event.Skip()

    def OnRacer1SpeedScrollPageup(self, event):
        event.Skip()

    def OnRacer1SpeedScrollThumbtrack(self, event):
        event.Skip()

    def OnRacer1SpeedKeyUp(self, event):
        event.Skip()

    def OnRacer1SpeedKeyDown(self, event):
        event.Skip()

    def OnRacer2speedScrollThumbrelease(self, event):
        event.Skip()

    def OnRacer2speedScrollThumbtrack(self, event):
        event.Skip()

    def OnRacer2speedScrollPagedown(self, event):
        event.Skip()

    def OnRacer2speedScrollPageup(self, event):
        event.Skip()

    def OnRacer2speedKeyUp(self, event):
        event.Skip()

    def OnRacer2speedKeyDown(self, event):
        event.Skip()

    def OnStopButtonButton(self, event):
        event.Skip()

class MyApp(wx.App):
    def OnInit(self):
        self.main = Frame1(parent=self)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    global application
    application = MyApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()

