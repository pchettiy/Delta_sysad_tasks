import sys, os, stat
from crontab import CronTab
i=0
for arg in sys.argv:
    if (i == 1):
        loc=arg
    i+=1
filepath = os.path.join(arg,'s1.py')
if not os.path.exists(loc):
    os.makedirs(loc)
f1=open(filepath, "w")
f1.write("import MySQLdb as mdb \n\
con=mdb.connect('localhost','prabakar','praba1110','timedb');\n\
with con: \n \
   \t cur=con.cursor()\n \
   \t cur.execute('DROP TABLE IF EXISTS timer')\n \
   \t cur.execute('CREATE TABLE timer(Time TIME)')\n \
   \t #cur.execute('INSERT INTO timer(Time) VALUES(CURRENT_TIMESTAMP)')\n")
f1.close()
st=os.stat(loc+'/'+'s1.py')
os.chmod(loc+'/'+'s1.py', st.st_mode | 0111)
filepath=os.path.join(loc,'s2.py')
if not os.path.exists(loc):
    os.makedirs(arg)
f2=open(filepath, "w")
f2.write("import MySQLdb as mdb\n\
con=mdb.connect('localhost','prabakar','praba1110','timedb');\n\
with con: \n \
    \t cur=con.cursor() \n \
    \t cur.execute('INSERT INTO timer(Time) VALUES(CURRENT_TIMESTAMP)') ")
f2.close()
st=os.stat(loc+'/'+'s2.py')
os.chmod(loc+'/'+'s2.py', st.st_mode | 0111)
cron= CronTab(user=True)
job=cron.new(command='/usr/bin/python2 '+filepath)
job.minute.every(10)
cron.write()
