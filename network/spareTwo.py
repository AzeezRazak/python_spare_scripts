#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

import argparse
import socket
import signal
import os
from struct import *
import datetime
import time
import pickle
import platform
import sys

PROTOCOL_TCP = 6
PROTOCOL_UDP = 17

# ValDirWrite
# Function that will validate a directory path as existing and writable. Used for argument validation only
# Input     : A directory path string
# Actions   : If valid will return the Directory String
#           : If invalid will raise a ArgumentTypeError within argparse which will inturn be reported to the user

def ValueDirWrite(theDir):

    if not os.path.isdir(theDir):
        raise argparse.ArgumentTypeError('Directory does not exist')

    if os.access(theDir, os.W_OK):
        return theDir
    else:
        raise argparse.ArgumentTypeError('Directory is not writable')

# Create a timeout class to handle capture duration

class myTimeout(Exception):
    pass

# Create a signal handler that raises a timeout event when the capture duration is over

def handler(signum, frame):
    if VERBOSE:

        print 'Capture Complete', signum
        print

    raise myTimeout

# Class: IPObservationDictionary
# Desc: Handles all methods and properties relating to the ipObservations

class IPObservationDictionary:

    def __init__(self):

        self.dictionary = {}

    def AddOb(self, key):

        now = datetime.datetime.now()
        hour = now.hour

        # Check to see if key is already in the dictionary

        if key in self.Dictionary:

            curValue = self.Dictionary[key]             #Retrieve the current value
            curValue[hour-1] = curValue[hour-1] + 1     # Increment the count for the current hour
            self.Dictionary[key] = curValue             # Update the value associated with this key

        else:
                                                        # Create key if key doesnt exist
            curValue = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            curValue[hour-1] = curValue[hour-1] + 1     # Increment the count for the current hour
            self.Dictionary[key] = curValue

    # Function to retrieve an observation, IF no observation found return None

    def GetOb(self, key):

        if key in self.Dictionary[key]:

            curValue = self.Dictionary[key]
            return curValue

        else:
            return None

    # Function to print contents of the dictionary

    def PrintOb(self):

        print '\nIP Observations'
        print 'Unique Combinations:     ', str(len(self.Dictionary))
        print
        print '                         '
        print '|------------------------- Hourly Observations -------------------------|'
        print '%16s' % "Server",
        print '%16s' % "Client",
        print '%7s' % "Port",
        print '%5s' % "Type",

        for i in range(0, 24):

            print ' ',
            print '%02d' % i,

        print

        for keys, values in self.Dictionary.items():

            print '%16s' % keys[0],
            print '%16s' % keys[1],
            print '%7s' % str(keys[2]),
            print '%5s' % keys[3]

            for i in range(0, 24):
                print '%4s' % str(values[i]),
            print

    # Function to save the Current Observation Dictionary to the specified file

    def SaveOb(self, fileName):

        with open(filename, 'wb') as fp:
            pickle.dump(self.Dictionary, fp)

    # Load Observation Library from the specified file

    def LoadOb(self, fileName):

        with open(filename, 'rb') as fp:
            self.Dictionary = pickle.loads(fp.read())

    # Delete the object

    def __del__(self):
        if VERBOSE:
            print 'Closed'

# Class: OSObservationDictionary
# Desc: Handles all methods and properties relating to the osObservations

class OSObservationDictionary:

    def __init__(self):

        self.Dictionary = {}

    def AddOb(self, key):

        now = datetime.datetime.now()
        hour = now.hour

        # Check to see if key is already in the dictionary

        if key in self.Dictionary:

            curValue = self.Dictionary[key]             # Retrieve the current value
            curValue[hour-1] = curValue[hour-1] + 1     # Increment the count for the current hour
            self.Dictionary[key] = curValue             # Update the value associated with this key

        else:
                                                        # Create key if key doesnt exist
            curValue = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            curValue[hour-1] = curValue[hour-1] + 1     # Increment the count for the current hour
            self.Dictionary[key] = curValue

    # Function to retrieve an observation, IF no observation found return None

    def GetOb(self, key):

        if key in self.Dictionary[key]:

            curValue = self.Dictionary[key]
            return curValue

        else:
            return None

    # Function to print contents of the dictionary

    def PrintOb(self):

        print '\nOS Observations'
        print 'Unique Combinations:     ', str(len(self.Dictionary))
        print
        print '                         '
        print '|------------------------- Hourly Observations -------------------------|'
        print '%16s' % "Server",
        print '%4s' % "TOS",
        print '%4s' % "TTL",
        print '%6s' % "DF",
        print '%7s' % "Windows",

        for i in range(0, 24):

            print ' ',
            print '%02d' % i,

        print

        for keys, values in self.Dictionary.items():

            print '%16s' % keys[0],
            print '%4s' % str(keys[1]),
            print '%4s' % str(keys[2]),
            print '%6s' % str(keys[3]),
            print '%7s' % str(keys[4]),

            for i in range(0, 24):
                print '%4s' % str(values[i]),
            print

    # Function to save the Current Observation Dictionary to the specified file

    def SaveOb(self, fileName):

        with open(filename, 'wb') as fp:
            pickle.dump(self.Dictionary, fp)

    # Load Observation Library from the specified file

    def LoadOb(self, fileName):

        with open(filename, 'rb') as fp:
            self.Dictionary = pickle.loads(fp.read())

    # Delete the object

    def __del__(self):
        if VERBOSE:
            print 'Closed'

# Packet Extractor

def PacketExtractor(packet):

    if PLATFORM == "LINUX":

        ETH_LEN = 14        # ETHERNET HDR LENGTH
        IP_LEN  = 20        # IP HEADER LENGTH
        UDP_LEN = 8         # UDP HEADER LENGTH

    elif PLATFORM == "WINDOWS":

        ETH_LEN = 0         # ETHERNET HDR LENGTH
        IP_LEN  = 20        # IP HEADER LENGTH
        UDP_LEN = 8         # UDP HEADER LENGTH

    else:

        print "Platform not supported"
        quit()

    ethernetHeader = packet[0:IP_LEN]

    # Strip off the first 20 characters for the IP Header
    ipHeader = packet[ETH_LEN:ETH_LEN+IP_LEN]

    # Now Unpack them
    ipHeaderTuple = unpack('!BBHHHBBH4s4s', ipHeader)

    # unpack returns a tuple, for illustration, I will extract each individual value

    verLen          = ipHeaderTuple[0]          # Field 0: Version and Length
    TOS             = ipHeaderTuple[1]          # Field 1: Type of Service
    packetLength    = ipHeaderTuple[2]          # Field 2: Packet Length
    packetID        = ipHeaderTuple[3]          # Field 3: Identification
    flagFrag        = ipHeaderTuple[4]          # Field 4: Flags / Fragment Offset
    RES             = (flagFrag >> 15) & 0x01   # Reserved
    DF              = (flagFrag >> 14) & 0x01   # Don't Fragment
    MF              = (flagFrag >> 13) & 0x01   # More Fragments
    timeToLive      = ipHeaderTuple[5]          # Field 5: Time to Live (TTL)
    protocol        = ipHeaderTuple[6]          # Field 6: Protocol Number
    checkSum        = ipHeaderTuple[7]          # Field 7: Header checkSum
    sourceIP        = ipHeaderTuple[8]          # Field 8: Source IP
    destIP          = ipHeaderTuple[9]          # Field 9: Destination IP

    # Calculate / Convert extracted values

    version     = verLen >> 4       # Upper Nibble is the Version Number
    length      = verLen & 0x0F     # Lower Nibble represents the size
    ipHdrLength = length * 4        # Calculate the header length in bytes

    # Convert the source and destination address to dotted notation strings

    sourceAddress       = socket.inet_ntoa(sourceIP);
    destinationAddress  = socket.inet_ntoa(destIP);

    if protocol == PROTOCOL_TCP:

        stripTCPHeader = packet[ETH_LEN+ipHdrLength:ipHdrLength+ETH_LEN+IP_LEN]

        # unpack returns a tuple, for illustration I will extract each value using unpack() function

        tcpHeaderBuffer = unpack('!HHLLBBHHH', stripTCPHeader)

        sourcePort              = tcpHeaderBuffer[0]
        destinationPort         = tcpHeaderBuffer[1]
        sequenceNumber          = tcpHeaderBuffer[2]
        acknowledgement         = tcpHeaderBuffer[3]
        dataOffsetandReserve    = tcpHeaderBuffer[4]
        tcpHeaderLength         = (dataOffsetandReserve >> 4) * 4
        flags                   = tcpHeaderBuffer[5]
        FIN                     = flags & 0x01
        SYN                     = (flags >> 1) & 0x01
        RST                     = (flags >> 2) & 0x01
        PSH                     = (flags >> 3) & 0x01
        ACK                     = (flags >> 4) & 0x01
        URG                     = (flags >> 5) & 0x01
        ECE                     = (flags >> 6) & 0x01
        CWR                     = (flags >> 7) & 0x01
        windowSize              = tcpHeaderBuffer[6]
        tcpChecksum             = tcpHeaderBuffer[7]
        urgentPointer           = tcpHeaderBuffer[8]

        if sourcePort <= 1024:                  # Assume server IP is server

            serverIP    = sourceAddress
            clientIP    = destinationAddress
            serverPort  = sourcePort
            status      = True

        elif destinationPort <= 1024:           # Assume destination IP is server

            serverIP    = destinationAddress
            clientIP    = sourceAddress
            serverPort  = destinationPort
            status      = True

        elif sourcePort <= destinationPort:     # Assume server IP is server

            serverIP    = sourceAddress
            clientIP    = destinationAddress
            serverPort  = sourcePort
            status      = True

        elif sourcePort > destinationPort:      # Assume destination IP is server

            serverIP    = destinationAddress
            clientIP    = sourceAddress
            serverPort  = destinationPort
            status      = True

        else:                                   # Should never reach here

            serverIP    = "FILTER"
            clientIP    = "FILTER"
            serverPort  = "FILTER"
            status      = False

        return( status, (serverIP, clientIP, serverPort, "TCP"), [SYN, serverIP, TOS, timeToLive, DF, windowSize] )

    elif protocol == PROTOCOL_UDP:

        stripUDPHeader = packet[ETH_LEN+ipHdrLength:ETH_LEN+ipHdrLength+UDP_LEN]

        udpHeaderBuffer = unpack('!HHHH', stripUDPHeader)

        sourcePort      = udpHeaderBuffer[0]
        destinationPort = udpHeaderBuffer[1]
        udpLength       = udpHeaderBuffer[2]
        udpChecksum     = udpHeaderBuffer[3]

        if sourcePort <= 1024:                  # Assume server IP is server

            serverIP    = sourceAddress
            clientIP    = destinationAddress
            serverPort  = sourcePort
            status      = True

        elif destinationPort <= 1024:           # Assume destination IP is server

            serverIP    = destinationAddress
            clientIP    = sourceAddress
            serverPort  = destinationPort
            status      = True

        elif sourcePort <= destinationPort:     # Assume server IP is server

            serverIP    = sourceAddress
            clientIP    = destinationAddress
            serverPort  = sourcePort
            status      = True

        elif sourcePort > destinationPort:      # Assume destination IP is server

            serverIP    = destinationAddress
            clientIP    = sourceAddress
            serverPort  = destinationPort
            status      = True

        else:                                   # Should never reach here

            serverIP    = "FILTER"
            clientIP    = "FILTER"
            serverPort  = "FILTER"
            status      = False

        return( status, (serverIP, clientIP, serverPort, "UDP"), ["FILTER", "FILTER", "FILTER", "FILTER", "FILTER", "FILTER"] )

    else:

        return( False, ("FILTER", "FILTER", "FILTER", "FILTER"), ["FILTER", "FILTER", "FILTER", "FILTER", "FILTER", "FILTER"] )

# Class Spinner
# Used to display a spinning character on the screen to show Progress

class Spinner:

    def __init__(self):

        self.symbols = [' |', ' /', ' -', ' \\', ' |', ' \\', ' -', 'END']
        self.curSymbol = 0

        sys.stdout.write("\b\b\b%s " % self.symbols[self.curSymbol])
        sys.stdout.flush()

    def Spin(self):

        if self.symbols[self.curSymbol] == 'END':
            self.curSymbol

        sys.stdout.write("\b\b\b%s " % self.symbols[self.curSymbol])
        sys.stdout.flush()
        self.curSymbol += 1


# ======================================================
# Main Program Starts here
# ======================================================

if __name__ == '__main__':

    parser = argparse.ArgumentParser('P2NMAP-Capture')

    parser.add_argument('-v', '--verbose', help="Display packet details", action='store_true')
    parser.add_argument('-m', '--minutes', help='Capture Duration in minutes', type=int)
    parser.add_argument('-p', '--outPath', type=ValDirWrite, required=True, help="Output Directory")

    theArgs = parser.parse_args()

    VERBOSE = theArgs.verbose

captureDuration = theArgs.minutes * 60

try:

    if platform.system() == "Linux":

        PLATFORM = "LINUX"

        ret = os.system("ifconfig eth0 promisc")
        if ret != 0:
            print 'Promiscous Mode not set'
            quit()

        # Create a new socket using the python socket module
        # PF_PACKET     :   Specifies Protocol Family Packet Level
        # SOCK_RAW      :   Specifies A Raw Protocol at the network layer
        # socket.htons(0x0800) : Specifies all headers and packets, Ethernet and IP incld TCP/UDP etc

        rawSocket=socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

        # Set the signal handler to the duration specified by the user

        signal.signal(signal.SIGALRM, handler)
        signal.alarm(captureDuration)


    elif platform.system() == "Windows":

        PLATFORM = "WINDOWS"

        hostname = socket.gethostname()
        host = socket.gethostbyname(hostname)
        rawSocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        rawSocket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        rawSocket.bind( (host,0))
        rawSocket.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        startTime = time.time()
        endTime = startTime + captureDuration
    else:

        print "Platform not supported"
        quit()

except:

    print "Socket Error"
    quit()

if VERBOSE:

    print "Network      : Promiscous Mode"
    print "Sniffer      : Ready: \n"

    # Create a Spinner object for displaying progress
    obSPIN = Spinner()

# Create IP Observation Dictionary & OS Observation Dictionary

ipOB = IPObservationDictionary()
osOB = OSObservationDictionary()

# Create a perpetual loop, interupted by timeout value only

packetsCaptured = 0

try:
    while True:

        packetsCaptured += 1

        if VERBOSE:
            obSPIN.Spin()               # Update the Display

        # Decode the received packet, call the above local packet extract function

        status, osContent, fingerPrint = PacketExtractor(receivedPacket)

        # If status returns True, we can process the results

        if status:

            ipOB.AddOb(osContent)       # Add content to ipObservations

            if fingerPrint[0] == 1:

                osContent = tuple(fingerPrint[1:])
                osOB.AddOb(osContent)

        else:
            continue                    # Not a valid packet

        if PLATFORM == "WINDOWS":
            if time.time() > endTime:
                raise myTimeout

except myTimeout:
    pass

# =============== Capture Complete ===============

if VERBOSE:

    print "\nTotal Packets Captured: ", str(packetsCaptured)
    print

    ipOB.PrintOb()
    osOB.PrintOb()

    print "\nSaving Observations ext: .ipDict and .osDict"

ipOutFile = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+".ipDict"
osOutFile = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+".osDict"

ipOutput = os.path.join(theArgs.outPath, ipOutFile)
osOutput = os.path.join(theArgs.outPath, osOutFile)

ipOB.SaveOb(ipOutput)
osOB.SaveOb(osOutput)

if PLATFORM == "LINUX":
    ret = os.system("ifconfig eth0 -promisc")   # Disable Promiscous Mode

elif PLATFORM == "WINDOWS":
    rawSocket.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

else:
    print "Platform not supported"
    quit()

rawSocket.close()
