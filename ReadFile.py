import os,datetime

month = ['','January','Febuary','March','April','May','June','July','August','September','October','November','December']
strWeekday = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def readFile(fileName):
    # read from file
    # return all info as a dictionary
    # if file is believed to be wrong, call FileError and raise Exception()
    dic = {}
    f = open(fileName,'r')
    txt = f.read()
    f.close()
    elem = txt.split('\n')
    for e in elem:
        if e == '':
            continue
        thing = e.split(': ')
        try:
            dic[thing[0]] = thing[1]
        except:
            FileError(fileName)
            raise Exception("FILE_ERROR_INCORRECT_FORMAT")
    for BoolList in ["AutoReload","AutoStart","ConfirmBooking"]:
        if BoolList in dic:
            if dic[BoolList] == "True":
                dic[BoolList] = True
            elif dic[BoolList] == "False":
                dic[BoolList] = False
            else:
                FileError(fileName)
                raise Exception("FILE_ERROR_TYPE_BOOLEAN")
    if "BookingDate" in dic:
        try:
            dic["StartTime"] = [int(i) for i in dic["BookingDate"].split("/")]
        except Exception as e:
            FileError(fileName)
            raise e
        if len(dic["StartTime"]) != 3:
            FileError(fileName)
            raise Exception("FILE_ERROR_DATE_ERROR")
        targetDateTime = datetime.datetime(dic["StartTime"][0],dic["StartTime"][1],dic["StartTime"][2])
        dic["BookingDate"] = strWeekday[targetDateTime.weekday()]+', '+month[dic["StartTime"][1]]+' '+str(dic["StartTime"][2])+', '+str(dic["StartTime"][0])
        specificTime = dic['BookingTime'].split(' - ')
        t = specificTime[0]
        type = t[-2:]
        t = t[:-3]
        t = [int(i) for i in t.split(':')]
        if type != "AM" and type != "PM":
            FileError(fileName)
            raise Exception("FILE_ERROR_TIME_AM/PM_TYPE_MISSING")
        if type == "PM" and t[0] != 12:
            t[0] += 12
        if t[1] != 15:
            outputError("START_MINUTE_NOT_15",warning=True)
        dic["StartTime"].append(t[0])
        dic["StartTime"].append(t[1])
    return dic

def reloadFile(fileName, dic):
    # advance time by 7 days and change confirm to False
    StartTime = []
    BookingTime = ''
    try:
        StartTime = dic["StartTime"]
        BookingTime = dic["BookingTime"]
    except:
        outputError("FILE_NOT_RELOADED")
        return
    curTime = datetime.datetime(StartTime[0],StartTime[1],StartTime[2],StartTime[3],StartTime[4])
    nextTime = curTime + datetime.timedelta(days=7)
    TOWRITE = "BookingDate: "+nextTime.strftime('%Y/%m/%d')+"\nBookingTime: "+BookingTime+"\nConfirmBooking: False"
    f = open(fileName,'w')
    f.write(TOWRITE)
    f.close()

def FileError(fileName):
    # re-locate the errornous file to fileName_old, and create a template file at fileName
    print(fileName)

def CheckFile(files):
    try:
        for fileName in files:
            print(readFile(fileName))
        print('All files look okay')
    except Exception as e:
        outputError(str(e))
        FileError(fileName)
        print('Error found, error code:',str(e))

def outputError(errorCode, warning=False):
    path = str(os.path.dirname(os.path.realpath(__file__)))
    if not os.path.exists(path+"\\ErrorLog.txt"):  # prepare the error log
        open(path+"\\ErrorLog.txt","x").close()
    f = open(path+"\\ErrorLog.txt",'a')
    if warning:
        f.write('\nWARNING: '+str(datetime.datetime.now())+'  '+errorCode+'\n')
    else:
        f.write('\nERROR:   '+str(datetime.datetime.now())+'  '+errorCode+'\n')
    f.close()

if __name__ == "__main__":
    CheckFile(['_BookingInfo.txt','_ConfirmBookingTime.txt'])