# UofTCourtBooking
UofTCourtBooking (UTCB) is written in collaboration between Liam and Evan. The entire script is open source, feel free to inspect and modify for other purposes. 

This code may require usename and password to complete the action, but the content will only be passed to the website specified by the user. However, UTCB comes with absolute NO WARRANTY, and may automatically install well-known python packages and alter Windows Task Scheduler. Use at your own risk. 

Most code comments are non-existance, and some (well, pretty much all) credits are not given. If this is any concern to you, please let us know!

## Prerequisite for the script
The script requires:
- Windows operating system;
- Google Chrome;
- Python 3 able to run in CMD;
- Pip available OR Selenium pacakage already installed.

## How to use to script
Files to pay attention to are: `_BookingInfo.txt`, `_ConfirmBookingTime.txt`, `Run.bat`, `Run_CheckFile.bat`, and `Run_ScheduleTask.bat`. 

Most item that you need to fill in the text file is pretty self-explanatory, all the format need to be followed to make the script run. Note that the "AutoReload", "AutoStart", and "ConfirmBooking" fields take boolean values only (True/False)

AutoReload
: if True, the script will automatically advance the date by 7 days after each successful execution. 

AutoStart
: if True, will automatically schedule with windows to run the script next time (7 days later).

ConfirmBooking
: the script will not attempt to run if is False. This field needs to be **mannually changed to True** everytime, even when AutoReload is set to True. 

---

The files ending with `.bat` is Windows batch file that will run the Python script with preset arguments. 

`Run.bat` runs the main program; `Run_CheckFile.bat` checks if the input text files are understandable by the script; `Run_ScheduleTask.bat` schedules the task with windows. 

**Fill in the correct date and time before running any of the scripts. Scheduled tasks cannot be cancelled by the script due to Windows premission issue. **

## Known bugs
1. ConfirmBooking not implemented correctly. 
2. Notify user when input text file is incorrect -- not yet implemented. 

For more issues and bugs please contact Liam. 
