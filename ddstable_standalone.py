########## #!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://github.com/anntzer/redeal/blob/master/redeal/dds.py
# https://github.com/Afwas/python-dds/blob/master/examples/dds.py

import ctypes
from ctypes import POINTER, Structure, byref, c_char, c_int, c_uint
import os
import sys

DDS_HANDS = 4
DDS_SUITS = 5
DDS_STRAINS = 5

dcardSuit = ["S", "H", "D", "C", "NT"]

class ddTableDeal(Structure):
    _fields_ = [("cards", c_uint * DDS_HANDS * DDS_SUITS)]

class ddTableResults(Structure):
#    _fields_ = [("resTable", c_int * DDS_STRAINS * DDS_HANDS)]
    _fields_ = [("resTable", c_int * DDS_HANDS * DDS_STRAINS)]

class ddTableDealPBN(Structure):
    _fields_ = [("cards", c_char * 80)]

class ddTableResults(Structure):
#    _fields_ = [("resTable", c_int * DDS_STRAINS * DDS_HANDS)]
    _fields_ = [("resTable", c_int * DDS_HANDS * DDS_STRAINS)]
    
tableDealPBN = ddTableDealPBN()
table = ddTableResults()

def errorMessage(res):
    msg = ctypes.create_string_buffer(80)
    dll.ErrorMessage(res, msg)
    result_len = ctypes.c_size_t(len(msg))
    return msg[:result_len.value]

def calcDDtablePBN(tableDealPBN):
    myTable = ctypes.pointer(table)
    res = dll.CalcDDtablePBN(tableDealPBN, myTable)
    if res != 1:
        line = errorMessage(res)
        raise Exception("DDS error: {}".format(line.decode("utf-8")))
    return myTable

dll_name = DLL = None
if os.name == "posix":
    dll_name = "libdds.so"
    DLL = ctypes.CDLL
elif os.name == "nt":
    dll_name = "dds-64.dll" if sys.maxsize > 2 ** 32 else "dds-32.dll"
    DLL = ctypes.WinDLL

if dll_name:
    dll_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            dll_name)

if dll_name and os.path.exists(dll_path):
    dll = DLL(dll_path)
    dll.CalcDDtable.argtypes = [ddTableDeal, POINTER(ddTableResults)]
    dll.ErrorMessage.argtypes = [c_int, POINTER(c_char)]

    if os.name == "posix":
        dll.SetMaxThreads(0)
    def _check_dll(name):
        return

else:
    def _check_dll(name):
        raise Exception(f"Unable to load DDS; {name} is not available")

def PrintTable(table):
    print("{:5} {:<5} {:<5} {:<5} {:<5}".format("", "North", "South", "East", "West"))
    for suit in range(0, DDS_SUITS):
        print("{:>5} {:5} {:5} {:5} {:5}".format(
            dcardSuit[suit],
            table.contents.resTable[suit][0],
            table.contents.resTable[suit][2],
            table.contents.resTable[suit][1],
            table.contents.resTable[suit][3]))
    print("")

def get_ddstable(pbn):
    tableDealPBN.cards = pbn
    table = calcDDtablePBN(tableDealPBN)
    all = { "N" : {}, "S" : {}, "E" : {}, "W" : {} }
    # below doesn't work, why?
    #all = dict.fromkeys(["N","S","E","W"], {})
    # print(all)
    for suit in range(0, DDS_SUITS):
        all["N"][dcardSuit[suit]] = table.contents.resTable[suit][0]
        all["S"][dcardSuit[suit]] = table.contents.resTable[suit][2]
        all["E"][dcardSuit[suit]] = table.contents.resTable[suit][1]
        all["W"][dcardSuit[suit]] = table.contents.resTable[suit][3]
    return all

def main():
    PBN = [b"N:QJ6.K652.J85.T98 873.J97.AT764.Q4 K5.T83.KQ9.A7652 AT942.AQ4.32.KJ3",
       b"N:T973.T852.AJ.JT5 Q.AQ.8764.AK7632 A654.7643.KT32.8 KJ82.KJ9.Q95.Q94",
       b"N:73.QJT.AQ54.T752 QT6.876.KJ9.AQ84 5.A95432.7632.K6 AKJ9842.K.T8.J93"]
    for i in range(len(PBN)):
        tableDealPBN.cards = PBN[i]
        myTable = calcDDtablePBN(tableDealPBN)
        PrintTable(myTable)
    print("let's compare:")
    tableDealPBN.cards = PBN[1]
    PrintTable(calcDDtablePBN(tableDealPBN))
    all = get_ddstable(PBN[1])
    print("{:>5} {:>5} {:>5} {:>5} {:>5} {:>5}".format("", "S", "H", "D", "C", "NT"))
    for each in all.keys():
        print("{:>5}".format(each),end='')
        for suit in dcardSuit:
            trick=all[each][suit]
            if trick>7:
                print(" {:5}".format(trick - 6),end='')
            else:
                print(" {:>5}".format("-"),end='')
        print("")
    #print(get_ddstable(PBN[1]))

if __name__ == '__main__':
    main()