import requests
# res = requests.get("https://github.com/timeline.json")
# print(res.json())


# ip, port = ("122.72.18.35", "80")
# url = 'http://www.baidu.com/'
# proxy_url = "http://{0}:{1}".format(ip, port)
#
# print(proxy_url)
#
# proxy_dict = {
#     "http": proxy_url
# }
#
# response = requests.get(url, proxies=proxy_dict)
#
# html_doc = str(response.content, 'utf-8')
# print(html_doc)
#


from http.server import BaseHTTPRequestHandler, HTTPServer
from os import path
from urllib.parse import urlparse
import json

curdir = path.dirname(path.realpath(__file__))
sep = '/'

# MIME-TYPE
mimedic = [
    ('.html', 'text/html'),
    ('.htm', 'text/html'),
    ('.js', 'application/javascript'),
    ('.css', 'text/css'),
    ('.json', 'application/json'),
    ('.png', 'image/png'),
    ('.jpg', 'image/jpeg'),
    ('.gif', 'image/gif'),
    ('.txt', 'text/plain'),
    ('.avi', 'video/x-msvideo'),
]


class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        sendReply = True
        querypath = urlparse(self.path)
        print(querypath)
        # self.send_response(200)
        # self.send_header('Content-type', mimedic[1][1])
        # self.end_headers()
        # self.wfile.write("ok")
        filepath, query = querypath.path, querypath.query

        # if filepath.endswith('/'):
        #     filepath += 'index.html'
        # filename, fileext = path.splitext(filepath)
        # for e in mimedic:
        #     if e[0] == fileext:
        #         mimetype = e[1]
        #         sendReply = True
        #         break

        if sendReply == True:
            try:
                content = "<html><body>ok</body></html>"
                jsonObj = json.loads(getmockjson())
                jsonNewObj = dict(code='RT000',
                                  data=jsonObj,
                                  path=filepath,
                                  query=query)
                content = json.dumps(jsonNewObj)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(content.encode())
                # self.send_response(200, content.encode())
                # self.send_error(404, 'File Not Found: %s' % self.path)
            except IOError:
                self.send_error(404, 'File Not Found: %s' % self.path)


def getmockjson():
    srl = '{"test":"123x", "number":123}'
    return srl


def run():
    port = 8000
    print('starting server, port', port)

    # Server settings
    server_address = ('', port)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
