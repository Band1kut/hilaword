# import socket
#
# # Создание сокета
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # Привязка сокета к адресу и порту
# server_address = ('0.0.0.0', 12345)
# server_socket.bind(server_address)
#
# # Ожидание подключения клиента
# server_socket.listen(1)
# print('Сервер запущен и ожидает подключения клиента...')
#
# while True:
#     # Принятие подключения от клиента
#     client_socket, client_address = server_socket.accept()
#     print('Подключение от клиента:', client_address)
#
#     try:
#         while True:
#             # Получение данных от клиента
#             data = client_socket.recv(1024)
#             if data:
#                 # Отправка обратно полученных данных
#                 client_socket.sendall(data)
#             else:
#                 # Если данные не получены, завершение соединения
#                 break
#     finally:
#         # Закрытие соединения с клиентом
#         client_socket.close()
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'hilaword')

def run_server(host, port):
    server_address = (host, port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f'Starting server on {host}:{port}')
    httpd.serve_forever()

# Replace <host> and <port> with your desired host and port number
host = '0.0.0.0'
port = 12345
run_server(host, port)
