from socket import socket, AF_INET, SOCK_STREAM
import os
import urllib.parse

def main():
    port = 1727
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(1)
    
    print("Server listening on port:", port)

    while True:
        client_socket, address = server_socket.accept()
        print("Client connected from:", address)

        request = client_socket.recv(1024).decode()
        start = request.find('/')
        end = request.find(' ', start)
        if end != -1:
            request_path = request[start:end]
        else:
            request_path = request[start:]
        
        print("Request path:", request_path)

        handle_request(request_path, client_socket)

        client_socket.close()
        print("Connection closed")

def handle_request(request_path, client_socket):
    base_directory = 'C:/Users/halaa/Desktop/NetworksProject'
    content_type = "text/html"

    if request_path.startswith('/image'):
        # Extract image_name from query parameters
        parsed_url = urllib.parse.urlparse(request_path)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        image_name = query_params.get('image_name', [None])[0]

        if image_name:
            file_path = os.path.join(base_directory, image_name)
            if os.path.exists(file_path):
                # Determine content type
                if file_path.lower().endswith('.png'):
                    content_type = 'image/png'
                elif file_path.lower().endswith('.jpg') or file_path.lower().endswith('.jpeg'):
                    content_type = 'image/jpeg'
                else:
                    content_type = 'application/octet-stream'

                with open(file_path, 'rb') as file:
                    data = file.read()
                    client_socket.sendall(
                        b"HTTP/1.1 200 OK\r\n"
                        b"Content-Type: " + content_type.encode() + b"\r\n"
                        b"Content-Length: " + str(len(data)).encode() + b"\r\n\r\n" + data
                    )
                return
        send_not_found(client_socket)
    else:
        # Handle other types of requests
        if request_path in ['/','/main_en.html', '/en']:
            file_path = os.path.join(base_directory, 'main_en.html')
        elif request_path in ['/ar', '/main_ar.html']:
            file_path = os.path.join(base_directory, 'main_ar.html')
        elif request_path.endswith('.html'):
            file_path = os.path.join(base_directory, request_path.lstrip('/'))
            if not os.path.exists(file_path):
                file_path = os.path.join(base_directory, 'main_en.html')
        elif request_path.endswith('.css'):
            file_path = os.path.join(base_directory, request_path.lstrip('/'))
            if not os.path.exists(file_path):
                file_path = os.path.join(base_directory, 'style.css')
            content_type = 'text/css'
        else:
            file_path = os.path.join(base_directory, request_path.lstrip('/'))
            if not os.path.exists(file_path):
                send_not_found(client_socket)
                return

        if file_path:
            try:
                with open(file_path, 'rb') as file:
                    data = file.read()
                    client_socket.sendall(
                        b"HTTP/1.1 200 OK\r\n"
                        b"Content-Type: " + content_type.encode() + b"\r\n"
                        b"Content-Length: " + str(len(data)).encode() + b"\r\n\r\n" + data
                    )
            except IOError:
                send_not_found(client_socket)
def send_not_found(client_socket):
    html_response = (
        b"<html>"
        b"<head><title>Error 404</title></head>"
        b"<body>"
        b"<h1>Error 404</h1>"
        b"<p style=\"color: blue;\">The file is not found</p>"
        b"<p><strong>Hala Mohammed - 1210312</strong></p>"
        b"<p><strong>Diana Naseer - 1210363</strong></p>"
        b"<p><strong>Rua Srour - 1221727</strong></p>"
        b"<p><strong>Client IP and Port:</strong> " + client_socket.getpeername()[0].encode() + b" : " + str(client_socket.getpeername()[1]).encode() + b"</p>"
        b"</body>"
        b"</html>"
    )

    client_socket.sendall(
        b"HTTP/1.1 404 Not Found\r\n"
        b"Content-Type: text/html\r\n"
        b"Content-Length: " + str(len(html_response)).encode() + b"\r\n\r\n" + html_response
    )

if __name__ == "__main__":
    main()