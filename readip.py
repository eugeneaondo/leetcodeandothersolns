logfile = "file.txt"

def read_ip_log(logfile):
     logfile_dict ={}

     with open(logfile , "r") as iplog:
          for line in iplog:
               entry = line.strip().split(',')
               timestamp = entry[0]
               method = entry[1]
               url = entry[2]
               ip_add = entry[3]


            
               logfile_dict['ip_add'] =  ip_add
               logfile_dict['timestamp']=timestamp
               logfile_dict['method']=method
               logfile_dict['URL']=url

               
     
     return logfile_dict       
                    
               
def calc_count(logfile_dict): 
    count = 1
    count_dict = {}
    for ip_add in logfile_dict:
        if ip_add not in count_dict:
            count_dict[ip_add] = count
        else:
            count += ip_add.value
            count_dict[ip_add].append(count)

    return count_dict

     
               
          
                   
  
     
x=read_ip_log(logfile)
print( x)
print(calc_count(x))


          
          

          
          
     
     
     
        




               


            

