logfile = "file1.txt"

def read_ip_log(logfile):
  logfile_dict = {}

  with open(logfile, "r") as iplog:
    for line in iplog:
      entry = line.strip().split(',')
      timestamp, method, url, ip_add = entry

      if ip_add not in logfile_dict:
        logfile_dict[ip_add] = []
      logfile_dict[ip_add].append({
        'timestamp': timestamp,
        'method': method,
        'URL': url
      })

  return logfile_dict

def calc_count(logfile_dict):
  count_dict = {}

  for ip_add, entries in logfile_dict.items():
    count_dict[ip_add] = len(entries)

  return count_dict

def top_ten(count_dict):
  def sort_by_count(pair):
    return pair[1]
  
  sorted_dict = sorted(count_dict.items(), key=sort_by_count , reverse=True)
  return sorted_dict[:10]
  

  

# Example usage:
log_data = read_ip_log(logfile)
print(read_ip_log(logfile))
count_result = calc_count(log_data)
print(count_result)
print("********************************************************************************************************")
print(top_ten(calc_count(log_data)))
