# -*- coding: utf-8 -*-
"""
@File   : events.py
@Date   : 2020-09-19
@Desc   : python 使用events实现事件监听的案例
"""
import socket
import _thread

"""
我们定义一个Event类,一般需要确定定义事件的类型,和event传递的数据
"""

class Event(object):
    """
    Generic event to use with EventDispatcher.
    用于事件分发
    """

    def __init__(self, event_type, data=None):
        """
        The constructor accepts an event type as string and a custom data
        定义event的类型和数据
        """
        self._type = event_type
        self._data = data

    @property
    def type(self):
        """
        Returns the event type
        返回event类型
        """
        return self._type

    @property
    def data(self):
        """
        Returns the data associated to the event
        返回event传递的数据
        """
        return self._data


class EventDispatcher(object):
    """
    Generic event dispatcher which listen and dispatch events
    event分发类 监听和分发event事件
    """

    def __init__(self):
        """
        初始化类
        """
        self._events = dict()

    def __del__(self):
        """
        清空所有event
        """
        self._events = None

    def has_listener(self, event_type, listener):
        """
        Return true if listener is register to event_type
        返回注册到event_type的listener
        """
        # Check for event type and for the listener
        if event_type in self._events.keys():
            return listener in self._events[ event_type ]
        else:
            return False

    def dispatch_event(self, event):
        """
        Dispatch an instance of Event class
        """
        # 分发event到所有关联的listener
        if event.type in self._events.keys():
            listeners = self._events[ event.type ]

            for listener in listeners:
                listener( event )

    def add_event_listener(self, event_type, listener):
        """
        Add an event listener for an event type
        给某种事件类型添加listener
        """
        # Add listener to the event type
        if not self.has_listener( event_type, listener ):
            listeners = self._events.get( event_type, [] )

            listeners.append( listener )

            self._events[ event_type ] = listeners

    def remove_event_listener(self, event_type, listener):
        """
        移出某种事件类型的所以listener
        """
        # Remove the listener from the event type
        if self.has_listener( event_type, listener ):
            listeners = self._events[ event_type ]

            if len( listeners ) == 1:
                # Only this listener remains so remove the key
                del self._events[ event_type ]

            else:
                # Update listeners chain
                listeners.remove( listener )

                self._events[ event_type ] = listeners


class SocketDataEvent(Event):
    Connected = "SocketConnected"
    Disconnected = "SocketDisconnected"
    Received = "SocketDataReceived"
    SentSuccessful = "SocketDataSentSuccessful"
    SentFailed = "SocketDataSentFailed"


class SocketServerHelper:

    def __init__(self,server_ip, server_port, backlog=4, receive_action=True, send_action=True):
        self.server_ip = server_ip
        self.server_port = server_port
        self.event_dispatcher = EventDispatcher()
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listener.bind((self.server_ip, self.server_port))
        self.listener.listen(backlog)
        self.receive_action = receive_action
        self.send_action = send_action
        self.__listening = False

    def __write_data(self, client_socket, client_addr):
        pass

    def __read_data(self, client_socket, client_addr):
        pass

    def accept_clients(self):
        pass

    def __accept_clients(self):
        pass


class CmdService:
    started = False
    socket_server = None
    socket_server_4_receive_cmd = None
    # ……

    @staticmethod
    def start_service(ip='127.0.0.1', port=55555):
        if CmdService.started:
            return
        try:
            CmdService.socket_server = SocketServerHelper(ip, port)
            CmdService.socket_server.event_dispatcher.add_event_listener(SocketDataEvent.Received, CmdService.__data_received)
            CmdService.socket_server.event_dispatcher.add_event_listener(SocketDataEvent.Disconnected, CmdService.__disconnected)
            CmdService.socket_server.event_dispatcher.add_event_listener(SocketDataEvent.Connected, CmdService.__connected)
            CmdService.socket_server.event_dispatcher.add_event_listener(SocketDataEvent.SentSuccessful, CmdService.__data_sent_successful)
            CmdService.socket_server.event_dispatcher.add_event_listener(SocketDataEvent.SentFailed, CmdService.__data_sent_failed)
            CmdService.socket_server.accept_clients()
            CmdService.started = True
            print('服务已启动！')
            _thread.start_new_thread(CmdService.__check_thread, ())
        except Exception as e:
            print('开启服务出错：' + str(e))
            pass

    @staticmethod
    def __check_thread():
        pass

    @staticmethod
    def __data_received():
        pass

    @staticmethod
    def __disconnected():
        pass

    @staticmethod
    def __connected():
        pass

    @staticmethod
    def __data_sent_successful():
        pass

    @staticmethod
    def __data_sent_failed():
        pass


if __name__ == '__main__':
    CmdService.start_service('0.0.0.0', 55555)
    print('started')