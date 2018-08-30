import os

folder_1 = '/home/westwell/Documents/wellocean/dist/release/'
folder_2 = '/home/westwell/Documents/wellocean_ori/dist/release/'

count_size_diff = 0
count_no_found = 0
total_file = 0
for file_1 in os.listdir(folder_1):
    print 'new ~~~~~~~~~~~~~~~~~~~~~~\n'
    total_file += 1
    find_flag = False
    size_flag = False
    # print file_1
    fsize_1 = os.path.getsize(folder_1 + file_1)
    fsize_1 = fsize_1/float(1024*1024)
    # print round(fsize_1,2)
    for file_2 in os.listdir(folder_2):
        if file_1 == file_2:
            find_flag = True
            # print 'find'
            fsize_2 = os.path.getsize(folder_2 + file_2)
            fsize_2 = fsize_2/float(1024*1024)
            if fsize_1 == fsize_2:
                size_flag = True
                # print 'size same'
    if not find_flag:
        count_no_found += 1
        print file_1,'------- in',folder_1,' no found in ',folder_2


    if not size_flag:
        count_size_diff += 1
        print file_1,'^^^^^^^ found in folder,but size different'
    # elif not find_flag:
    #     count_no_found += 1
    #     print file_1,'------- in folder_1 no found in folder_2'

print 'total_file : ',total_file
print 'count_size_diff : ',count_size_diff    
print 'count_no_found : ',count_no_found          
      
                
