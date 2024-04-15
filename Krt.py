# Krt.py
import sys 
import time 
def jalan (s):
    for c in s + " ":
        sys.stdout.write (c)
        sys.stdout.flush()
        time.sleep(1. /40)
        
        
def pilihan_hek():
    print ("\33[31m[\33[37m01\33[31m]\33[1;32mFacebok    \33[31m[\33[37m04\33[31m]\33[1;32mTIKTOK" )
    print ("\33[31m[\33[37m02\33[31m]\33[1;32mWhastapp   \33[31m[\33[37m05\33[31m]\33[1;32mTELKGARAM"  )
    print ("\33[31m[\33[37m03\33[31m]\33[1;32mIG         \33[31m[\33[37m06\33[31m]\33[1;32mMOBILE")
    hack = str (input ("pilih cara hack > \33[1;34m"))
    if hack == "1":
        print ("FACEBOK")
    elif hack == "2":
        print ("whastapp")        
    elif hack == "3":
        print ("Ig")
    elif hack == "4":
        print ("TIKTOK")
    elif hack == "5":
        print ("TELEGRAM")
    elif hack == "6":
        print ("MOBILE ")
    else :
        print ("not foun ")     
    try :
        print ("\33[36m="*30)
        print ("\33[1;35mLOGO PERETAS  |")
        print ("\33[36m="*30)
    except :
        print ("not foun")        
    if hack == "1":
        jalan ('\33[1;34mLOGO FACEBOK')
    elif hack == "2":
        jalan ("\33[1;32mLOGO WHASSTAP")
    elif hack == "3":
        jalan ("\33[31mLOGO IG ")
    elif hack =="4":
        jalan ("\33[1;39mLOGO TIKTOK")
    elif hack =="5":
        jalan ("\33[1;34m LOGO TELEGRAM")
    elif hack == "6":
        jalan ("\33[1;40mLOGO MOBILE")
    else :
        print ("not foun")
        
    def facebok ():
        if hack == "1":
            hack1 = str (input ("/nmasukan nomor : "))
            print ("Y /T")
            hack1 = str (input ("masukan sandi tenga "))
            print (hack1+hack1)
        else :
            print ("not foun")
            
            
            
    facebok ()
    
    def whasstap ():
        if hack =="2":
           hack2= str (input ("masukan no wa :"))
           print (hack2)
        else :
           print (" tidak valit wa ")
    whasstap()
    
        
pilihan_hek()    

        
