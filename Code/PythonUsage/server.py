import socket
import socket
import threading        # 导入线程模块


def link_handler(link, client):     
    """
    该函数为线程需要执行的函数，负责具体的服务器和客户端之间的通信工作
    :param link: 当前线程处理的连接
    :param client: 客户端ip和端口信息，一个二元元组
    :return: None
    """
    print("Start receive message:[%s:%s]...." % (client[0], client[1]))
    while True:     # 利用一个死循环，保持和客户端的通信状态
        client_data = link.recv(1024).decode()
        if client_data == "exit":
            print("end [%s:%s]'s connection..." % (client[0], client[1]))
            break
        print("message from [%s:%s], message: %s" % (client[0], client[1], client_data))
        link.sendall('Received'.encode())
    link.close()


ip_port = ('127.0.0.1', 9999)
sk = socket.socket()            # 创建套接字
sk.bind(ip_port)                # 绑定服务地址
sk.listen(5)                    # 监听连接请求

print('Started socket..')

while True:     # 一个死循环，不断的接受客户端发来的连接请求
    conn, address = sk.accept()  # 等待连接，此处自动阻塞
    # 每当有新的连接过来，自动创建一个新的线程，
    # 并将连接对象和访问者的ip信息作为参数传递给线程的执行函数
    t = threading.Thread(target=link_handler, args=(conn, address))
    t.start()