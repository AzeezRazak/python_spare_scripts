# Generate a unique list of the Server/Client interactions over Port 443
# Python 2.7.x
#
# Main Program
# a. Sets up network interface (NIC) in promiscious mode
# b. Opens a raw socket
# c. Listens and reads packets from the raw socket
# d. Calls the PacketExtractor() function to decode the packet
# e. Updates a list with packets that meet our port criteria
# f. Once maximum number of packets are collected, a unique list is generated
# Packet Extractor() function
# a. Extracts the IP Header
# b. Extracts the TCP Header
# c. Obtains the Source and Destination IP Address
# d. Obtains the Source and Destinations Port Numbers
# e. Makes an educated guess as to the Server VS Client
# f. Returns a list containing ServerIP, ClientIP, ServerPort
# Run only in linux, with super user privilege

import socket           # Network interface library used for raw sockets
import os               # Operating system functions
import sys              # System level functions
from struct import *    # Handle Strings as Binary Data

# Constants

PROTOCOL_TCP = 6

# PacketExtractor
# Purpose : Extracts fields from the IP and TCP Header
# Input:    packet: buffer from socket.recvfrom() method
# Output:   list:   serverIP, clientIP, serverPort

def PacketExtractor(packet):

    stripPacket = packet[0:20] # Strip off the first 20 characters for the ip header

    ipHeaderTuple = unpack('!BBHHHBBH4s4s', stripPacket)

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

        stripTCPHeader  = packet[ipHdrLength:ipHdrLength+20]

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

        if sourcePort < 1024:
            serverIP = sourceAddress
            clientIP = destinationAddress
            serverPort = sourcePort
        elif destinationPort < 1024:
            serverIP = destinationAddress
            clientIP = sourceAddress
            serverPort = destinationPort
        else:
            serverIP = "Filter"
            clientIP = "Filter"
            serverPort = "Filter"

        return([serverIP, clientIP, serverPort], [SYN, serverIP, TOS, timeToLive, DF, windowSize])

    else:
        return(["Filter", "Filter", "Filter"], [Null, Null, Null, Null])

#----------------------------- MAIN SCRIPT -----------------------------

if __name__ == '__main__':

    # Ensure Superuser mode in linux, a system call and promiscious mode on the Port

    ret = os.system("if config eth0 promisc")

    if ret == 0:

        print "eth0 configured in promiscious mode"

        # Create a socket using the python socket module
        # AF_INET   :   Address Family Internet
        # SOCK_RAW  :   A new protocol at the network layer
        # IPPROTO_TCP   Specifies the socket transport layer is TCP

        try:
            mySocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            print "Raw Socket Open"

        except:
            print "Raw Socket Open Failed"
            sys.exit()

        ipObservations = []     # Create a list to hold results from the packet capture
        osObservations = []     # Save Server IP, Client IP, Server Port

        maxObservations = 500

        portValue = 443

        try:
            while maxObservations > 0:
                content, fingerPrint = PacketExtractor(recvBuffer)

                if content[0] != "Filter":
                    if content[2] == portValue:
                        ipObservations.append(content)
                        maxObservations = maxObservations - 1

                        if fingerPrint[0] == 1:
                            osObservations.append([fingerPrint[1], fingerPrint[2], fingerPrint[3], fingerPrint[4], fingerPrint[5]])
                    else:
                        continue

                else:
                    continue

        except:
            print "Socket Failure"
            exit()

        # ----------------------------- Capture Complete -----------------------------

        ret = os.system("ifconfig eth0 -promisc")   # Disable Promiscous Mode

        mySocket.close()                            # Close the socket

        # Create unique sorted list, before converting to a set, eliminating duplication
        # and finally converting to a list for sorting

        uniqueSrc = set(map(tuple, ipObservations))
        finalList = list(uniqueSrc)
        finalList.sort()

        uniqueFingerprints = set(map(tuple, osObservations))
        finalFingerPrintList = list(uniqueFingerprints)
        finalFingerPrintList.sort()

        # Print out the unique combinations

        print "Unique packets"

        for packet in finalList:
            print packet

        print "Unique Fingerprints"

        for osFinger in finalFingerPrintList:
            print osFinger

    else:
        print "Promiscous Mode not set"
