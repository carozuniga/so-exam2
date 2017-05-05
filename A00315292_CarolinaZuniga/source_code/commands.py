from subprocess import Popen, PIPE

def memory():
 grep= Popen(["free","-m"], stdout=PIPE, stderr=PIPE)
 grep3= Popen(["awk",'/Mem/{print ($3/$2)*100}'],stdin=grep.stdout, stdout=PIPE, stderr=PIPE).communicate()[0]
 return grep3.strip()+'%'

def cpu():
 grep= Popen(["mpstat"], stdout=PIPE, stderr=PIPE) 
 grep3= Popen(["awk",'/all/{print $5}'],stdin=grep.stdout, stdout=PIPE, stderr=PIPE).communicate()[0]
 return grep3.strip()+'%'

def disk():
 grep= Popen(["df","-h"], stdout=PIPE, stderr=PIPE) 
 grep3= Popen(["awk",'NR == 2{print $5}'],stdin=grep.stdout, stdout=PIPE, stderr=PIPE).communicate()[0]
 return grep3.strip()

def sshd():
 grep= Popen(["service","sshd","status"], stdout=PIPE, stderr=PIPE) 
 grep3= Popen(["awk",'/Active/{print $2}'],stdin=grep.stdout, stdout=PIPE, stderr=PIPE).communicate()[0]
 return grep3.strip()
