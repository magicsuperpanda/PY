import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('vill',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('bat',), name='Thread-B')
t3 = threading.Thread(target= process_thread, args=('zed',), name='Thread-C')
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()