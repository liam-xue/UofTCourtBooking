import os

def readFile(fileName):
    # read from file
    # return all info as a dictionary
    # if file is believed to be wrong, call FileError and raise Exception()
    if fileName == 'BookingInfo.txt':
        dic = {
            'Webpage': 'https://recreation.utoronto.ca/Program/GetProgramDetails?courseId=ca92214b-0334-4e97-a60e-2144af28e435&semesterId=0ceb5a30-42f1-4069-a97b-5e015b379e14',
            'UTORid': 'username',
            'Password': 'password',
            'AutoReload': True,
            'AutoStart': False
        }  # note the AutoReload is a boolean not a string
    else:
        dic = {
            'BookingDate': 'Saturday, December 4, 2021',
            'BookingTime': '3:15 PM - 4:00 PM',
            'StartTime': [2021, 12, 8, 12, 15],  # in yyyy,mon,day,hr,min
            'ConfirmBooking': True
        }
    return dic

def reloadFile(fileName, dic):
    # advance time by 7 days and change confirm to False
    pass

def FileError(fileName):
    # re-locate the errornous file to fileName_old, and create a template file at fileName
    pass

def CheckFile(files):
    # make sure all the files are correct, and call outputError when error is met, warning when ConfirmBooking is False
    print('All files look okay')

def outputError(errorCode, warning=False):
    f = open("ErrorLog.txt",'a')
    if warning:
        f.write('\nWARNING: '+str(datetime.datetime.now())+'  '+errorCode+'\n')
    else:
        f.write('\nERROR:   '+str(datetime.datetime.now())+'  '+errorCode+'\n')
    f.close()

if __name__ == "__main__":
    CheckFile(['BookingInfo.txt','ConfirmBookingTime.txt'])