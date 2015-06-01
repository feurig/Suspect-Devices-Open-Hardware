#!/usr/bin/env python

"""------------------------------------------------------------------------bikewedge.py
    
    DESCRIPTION: This code intercepts both sides of opensprints/goldsprintsfx 
    "conversation" to control a visual indication of progress using something 
    like a phsical clock or a race tree.
    This makes it possible to not have a projector that costs more than your rollers.
    It also makes it possible to do outdoor or mobile events.
    
    TECHNICAL: This is a basic combination of the client and server software from the 
    python in a nutshell book. It makes a lot of assumtions and should do a better 
    job of recovering when the pile of flash or the serial proxy crashes (which 
    happens). 
    It creates a server on 5331 (the only port gold sprints checks) and expects 
    to listen to serproxy on 5330 it talks to the clock on 5332
    it should eventually check and start serproxy and the goldsprints programs.
    it should also do a better job of recovering from issues created by externals.
    
    It has a lot of number foo (hard coding) in it that should be cleaned up
    
    Copyright 2013 (c) Donald Delmar Davis, Suspect Devices, 
    All rights reserved.

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
import socket
import re
import time
from subprocess import Popen

#TODO: get rid of the foo
#      * (constants for bike ticks / clock ticks)
#      * hardcoded paths


#start up serproxy.
#TODO: ERROR HANDLING in here. 
p1=Popen('./serproxy')
time.sleep(.5)
isocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
osocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
csocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
isocket.connect(('localhost',5330))
isocket.settimeout(0.2)
print "Connected to serproxy"
csocket.connect(('localhost',5332))
csocket.settimeout(0.2)
print "Connected to clock"
osocket.bind(('',5331))
osocket.listen(1)
#open goldsprints
p2=Popen('/Applications/GoldsprintsFX_b2.2.app/Contents/MacOS/GoldsprintsFX_b2.2')

try:
    while True:
        connection,address=osocket.accept()
        if not connection: break
        print "Connected From", address
        #connection.setblocking(0)
        connection.settimeout(0.2)
        while True:
            try:
                receivedData = connection.recv(8192)
            except socket.error:
                receivedData=None
            if receivedData is not None:
                #print ">"+re.escape(str(receivedData))+">"+str(len(receivedData))
                isocket.sendall(receivedData)
                for chunk in receivedData.split('\x00'):
                    if len(chunk)>0 and chunk[0] == 's':
                        print "(RE)SET RACE !!!"
                        csocket.sendall("s\n");
                    if len(chunk)>0 and chunk[0] == 'g':
                        print "GO!!!!!!!!!!"
                        csocket.sendall("g\n");
                if len(receivedData)==0:
                    print "ISSUE WITH GOLDSPRINTSFX"
                    #TODO kill/restart goldsprintsfx
                
            try:
                sentData = isocket.recv(8192)
            except socket.error:
                sentData=None
            if sentData is not None:
                #print "<"+re.escape(str(sentData))+"<"+str(len(sentData))
                connection.sendall(sentData)
                for chunk in sentData.split('\x00'):
                    #if len(chunk.rstrip('\r')):
                    #    print "<",re.escape(chunk),len(chunk)
                    if len(chunk) > 4 and chunk[0]=='0' :
                        done1=(float(chunk[3:])/1566.0) * 100.00
                        if done1>100.00 :
                            done1=100.00
                        print "Bike # 1 is ", str(int(done1)), "percent done"
                        csocket.sendall("d1:"+str((int(10.66*(done1)))+0.9)+"\n")
                    if len(chunk) > 4 and chunk[0]=='1' :
                        done2=(float(chunk[3:])/1566.0) * 100.00
                        if done2>100.00 :
                            done2=100.00
                        print "Bike # 2 is ", str(int(done2)), "percent done"
                        csocket.sendall("d2:"+str(int((10.66*(done2)))+0.9)+"\n")
                    
                if len(sentData)==0:
                    print "ISSUE WITH SERPROXY"
                    try:
                        isocket.sendall("\rv\r\x00")
                    except socket.error:
                        #TODO kill/restart serproxy
                        isocket.close()
                        isocket.connect(('localhost',5330))                        
                    break

except KeyboardInterrupt:
    print "Killed by user.\n"

except Exception as e:
    print "HRRM didn't see this coming..", str(e), "\n"

finally:
    p1.kill()
    p2.kill()
    print "...killing any straglers..."
    
    if connection is not None:
            connection.close()
            
    csocket.close()
    osocket.close()
    isocket.close()
    # serproxy leaves connected children so kill them.
    p=Popen(['killall', 'serproxy'])
    time.sleep(.2)
    p=Popen(['killall', 'serproxy'])
    p=Popen(['killall', 'serproxy'])
    time.sleep(.2)
    print ""

