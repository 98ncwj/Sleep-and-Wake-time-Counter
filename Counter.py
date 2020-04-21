import copy
def convert_minutes(hours,minutes):
    answer=0
    answer+=hours*60
    answer+=minutes
    return answer

def diff_time(shour,smin,ehour,emin):
    hdiff=0
    mdiff=0
    
    if smin==0:
        if emin==0:
            mdiff=0
        else:
            mdiff=emin
    elif emin==0:
        if smin==0:
            mdiff==0
        else:
            mdiff=60-smin
            shour+=1
    else:
        mdiff=60-smin
        mdiff+=emin
        shour+=1
    
    if shour > ehour:
        hdiff=24-shour
        hdiff+=ehour
    elif shour==0:
        if ehour==0:
            hdiff=0
        else:
            hdiff=ehour
    elif ehour==0:
        if shour==0:
            hdiff=0
        else:
            hdiff=24-shour

    else:
        hdiff=ehour-shour

    
    return hdiff,mdiff

        

f = open("C:/Users/Nicholas/Desktop/New/test.txt", "r")
out=open("C:/Users/Nicholas/Desktop/New/output.txt","w")
awake=0
sleep=0
cases= 0
temp=list()

total=int(f.readline())
skip=f.readline()
while cases<total:
    number=f.readline()
    for i in range(int(number)):
        curr=f.readline() 
        times=curr.split(" ")
        time=times[0].split(":")
        time1=times[1].split(":")
        thour,tmin=diff_time(int(time[0]),int(time[1]),int(time1[0]),int(time1[1]))
        sleep+=convert_minutes(thour,tmin)
        if temp:
            thour,tmin=diff_time(int(temp[0]),int(temp[1]),int(time[0]),int(time[1]))
            awake+=convert_minutes(thour,tmin)
            temp=time1
        else:
            temp=time1
        
    temp=[]
    
    answer="Case "+str(cases+1)+":"+str(awake)+" "+str(sleep)+"\n"
    out.write(answer)
    awake=0
    sleep=0
    cases+=1
    skip=f.readline()  
     
f.close()
out.close()
        

        
    