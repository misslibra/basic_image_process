# import logging    
import psutil  
import os  
  
  
# log_filename="logging.txt"  
  
# log_format='[%(asctime)s]  %(message)s'  
# logging.basicConfig (format=log_format,datafmt='%Y-%m-%d %H:%M:%S %p',level=logging.DEBUG,filename=log_filename,filemode='w')  
# logging.debug('log output!' )  
p1=psutil.Process(os.getpid())
while 1:
    # print ('memory used:'+(str)(psutil.virtual_memory))  
    # print ('memory rate:'+(str)(psutil.virtual_memory().percent)+'%')  
    print ('os cpu rate:'+(str)(psutil.cpu_percent(interval=1, percpu=True))+'%')
    # logging.debug('os cpu rate:'+(str)(psutil.cpu_percent(interval=1, percpu=True))+'%' )
    # logging.debug('/n' )  
    # print ("program CPU rate:"+(str)(p1.cpu_percent(None))+"%")  
    # print (p1.memory_percent)  
    # print "percent: %.2f%%" % (p1.memory_percent())