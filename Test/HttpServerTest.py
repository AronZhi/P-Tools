from NetComponent.Http.Server import Server
from NetComponent.Http.Handler import Handler

class MyHandler(Handler):
    async def get(self):
        data = self.ParseRequest()
        print(data)
        if data.get('command', '') == 'stop':
            self.write('stop srver now')
            self.StopServer()
        else:
            self.write('can not handle this command')
    
    async def post(self):
        data = self.ParseRequest()
        print(data)
        if data.get('echo', ''):
            content = data['echo']
            self.write(content)


def main():
    server = Server()
    server.Run(8888, [(r'/', MyHandler)])

if __name__ == '__main__':
    main()