import sys,os,time

lg1="""
          lllll  ll   ll    ll   ll
          ll     ll   ll    ll l ll
          lllll  ll   ll    ll   ll  \033[0;35m
             ll  ll   ll    ll   ll 
          lllll   lllll     ll   ll 
  """
lg2="""
           ll   ll   ll  ll    ll
           ll l ll   ll  ll    ll   \033[0;36m
           ll   ll   ll  ll    ll
           ll   ll    llll     lllll 
 """
lg3="""
           lllll  ll   ll  llllll    
           ll     ll   ll   ll  ll
           lllll  ll   ll   lllll    \033[0;32m
              ll  ll   ll   ll  ll
           lllll   lllll   llllll
 """
lg4="""
           ll   ll    lll    lllll
           ll l ll   l   l    l  ll
           ll   ll   l   l    l  ll  \033[0;96m
           ll   ll    lll    lllll 
                      
 """
lg5="""
           lllll    llll   ll     ll
            l  ll    ll     ll   ll   \033[0;96m
            l  ll    ll      ll ll
           lllll    llll      lll  
 """
 
def anim(lgs):
    for i in range(0,3):
        os.system('clear')
        print(" \033[1;32m                     patientez: ",i)
        time.sleep(1)
        os.system('clear')
    for x in lgs:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.007)
        