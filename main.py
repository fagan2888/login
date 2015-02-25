from login import Login
from apscheduler.schedulers.blocking import BlockingScheduler


def MooningSI():
    f = open('user.txt','r')
    lines = f.readlines()
    for line in lines:
        line = line.strip(' ').split(',')
        username = line[0].decode('utf-8')
        password = line[1]
        login = Login(username, password)
        login.monilogin()
        login.MorningSI()
    f.close()
    
def MooningSO():
    f = open('user.txt','r')
    lines = f.readlines()
    for line in lines:
        line = line.strip(' ').split(',')
        username = line[0].decode('utf-8')
        password = line[1]
        login = Login(username, password)
        login.monilogin()
        login.MorningSO()
    f.close()
    
def NoonSI():
    f = open('user.txt','r')
    lines = f.readlines()
    for line in lines:
        line = line.strip(' ').split(',')
        username = line[0].decode('utf-8')
        password = line[1]
        login = Login(username, password)
        login.monilogin()
        login.NoonSI()
    f.close()
    
def NoonSO():
    f = open('user.txt','r')
    lines = f.readlines()
    for line in lines:
        line = line.strip(' ').split(',')
        username = line[0].decode('utf-8')
        password = line[1]
        login = Login(username, password)
        login.monilogin()
        login.NoonSO()
    f.close()


if __name__ == '__main__':
   
    sched = BlockingScheduler()
    
    # Schedules job_function to be run on the third Friday
    # of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
    sched.add_job(MooningSI, 'cron', day_of_week='mon-fri', hour=7, minute=50)
    sched.add_job(MooningSO, 'cron', day_of_week='mon-fri', hour=11, minute=50)
    sched.add_job(NoonSI, 'cron', day_of_week='mon-fri', hour=1, minute=50)
    sched.add_job(NoonSO, 'cron', day_of_week='mon-fri', hour=5, minute=50)
    
    sched.start()
    

        
    