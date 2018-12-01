# logfile = open("1000log.log", "r")
#
# get_page_log=[]
# res=[]
#
# for line in logfile:
#     try:
#         get_page_log.append(line)
#     except:
#         pass
#
#
# logfile.close()
#
# check = "Duration"
# for i in get_page_log:
#     if check in i:
#         res.append(i)
#
# print len(res)
import os

count = 5

os.environ['count'] = str(count)
os.system('echo $[count+1];for i in {1..$[count]};do echo $i;done')

output = os.popen('echo $[count+1]').read()
# os.system('echo $[count+1]')
