echo on
echo "started"
schtasks /create /tn UTCB /tr %0\..\Run.bat /sc monthly /st 11:08 /d 8 /sd 2021/12/08 /ed 2021/12/08 /et 11:10 /z /ri 0
set /p exitkey= "Press any key to exit..."