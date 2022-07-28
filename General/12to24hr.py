import os

def twelveto24(time):
    format12=time[-2:]
    twelveinAM="00"
    
    if len(time)==10:
        hrs=time[:1]
        constant=time[1:7]
        if format12=="am" or format12=="AM":
        #am calculations
            print(time[:8])
        else:
            if format12=="pm" or format12=="PM":
        #pm calculations
                hrs24=str(int(hrs)+12)
                print(hrs24+constant)
    else:
        hrs=time[:2]
        constant=time[2:8]
        if format12=="am" or format12=="AM":
        #am calculations
            if hrs=="12":
                print(twelveinAM+constant)
            else:
                print(time[:8])
        else:
            if format12=="pm" or format12=="PM":
        #pm calculations
                if hrs=="12":
                    print(time[:8])
                else:
                    hrs24=str(int(hrs)+12)
                    print(hrs24+constant)

time=input("Enter the time : ")
twelveto24(time)
