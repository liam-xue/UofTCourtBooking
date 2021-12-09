# UofTCourtBooking
UofTCourtBooking is written in collaboration between Liam Xue and Evan Chan. The entire script is open source, feel free to inspect and modify for other purposes. 

This code may require usename and password to complete the action, but the content will only be passed to the website specified by the user. However, UTCB comes with absolute NO WARRANTY, and may automatically install well-known python packages and alter Windows Task Scheduler. Use at your own risk. 

## Prerequisite for the script
The script requires:
- Windows operating system;
- Google Chrome;
- Python 3 able to run in CMD;
- Pip available OR Selenium pacakage already installed.

## How to use to script
Files to pay attention to are: `_BookingInfo.txt`, `_ConfirmBookingTime.txt`, `Run.bat`, `Run_CheckFile.bat`, and `Run_ScheduleTask.bat`. 

Most item that you need to fill in the text file is pretty self-explanatory, all the format need to be followed to make the script run. Note that the "AutoReload", "AutoStart", and "ConfirmBooking" fields take boolean values only (True/False)
