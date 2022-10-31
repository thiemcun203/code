import time
#print(dir(time))
['CLOCK_MONOTONIC', 'CLOCK_MONOTONIC_RAW', 'CLOCK_PROCESS_CPUTIME_ID', 
 'CLOCK_REALTIME', 'CLOCK_THREAD_CPUTIME_ID', 'CLOCK_UPTIME_RAW', '_STRUCT_TM_ITEMS',
 '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone', 'asctime', 
 'clock_getres', 'clock_gettime', 'clock_gettime_ns', 'clock_settime', 'clock_settime_ns',
 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 
 'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time', 'process_time_ns', 
 'sleep', 'strftime', 'strptime', 'struct_time', 'thread_time', 'thread_time_ns', 'time',
 'time_ns', 'timezone', 'tzname', 'tzset']
time.sleep(0)
#1. Time.time() returns current time in seconds since epoch of UTC 
print(time.time())
#2 Time.gmtime(0) gets the epoch January 1 1970 00:00:00 UTC
#daylight saving time
#timestructure, amount of time, time string , time tuple
print(time.gmtime(time.time()))
print(time.gmtime(0)) # convert time in UTC 00
print(time.localtime(time.time())) #convert time in local time 
print(time.ctime(time.time()))
print(time.asctime((time.localtime())))
print(time.strptime('Wed, 29 Jun 2022 23:51:37', '%a, %d %b %Y %H:%M:%S'))
time.struct_time((2019, 2, 26, 7, 6, 55, 1, 57, 0))
print(time.mktime((2019, 2, 26, 7, 6, 55, 1, 57, 0)))
print(time.CLOCK_PROCESS_CPUTIME_ID)