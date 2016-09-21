import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.add_header("Login")
        self.render("index.html")

class AppHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world2")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/app", AppHandler),
    ])

if __name__ == "__main__":
    # app = make_app()
    # app.listen(80)
    # tornado.ioloop.IOLoop.current().start()
    l = srv.LikesHandler()

