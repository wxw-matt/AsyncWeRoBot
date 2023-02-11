# -*- coding: utf-8 -*-

from tornado.web import RequestHandler

import html


def make_handler(robot):
    """
    为一个 BaseRoBot 生成 Tornado Handler。

    Usage ::

        import tornado.ioloop
        import tornado.web
        from werobot import WeRoBot
        from werobot.contrib.tornado import make_handler

        robot = WeRoBot(token='token')


        @robot.text
        async def hello(message):
            return 'Hello World!'

        app = tornado.web.Application([
            (r"/", make_handler(robot)),
        ])

        if __name__ == "__main__":
            app.listen(8090)
            tornado.ioloop.IOLoop.current().start()


    :param robot: 一个 BaseRoBot 实例。
    :return: 一个标准的 Tornado Handler
    """
    class WeRoBotHandler(RequestHandler):
        def prepare(self):
            timestamp = self.get_argument('timestamp', '')
            nonce = self.get_argument('nonce', '')
            signature = self.get_argument('signature', '')

            if not robot.check_signature(
                timestamp=timestamp, nonce=nonce, signature=signature
            ):
                self.set_status(403)
                self.write(
                    robot.make_error_page(
                        html.escape(
                            self.request.protocol + "://" + self.request.host +
                            self.request.uri
                        )
                    )
                )
                return

        def get(self):
            echostr = self.get_argument('echostr', '')
            self.write(echostr)

        async def post(self):
            timestamp = self.get_argument('timestamp', '')
            nonce = self.get_argument('nonce', '')
            msg_signature = self.get_argument('msg_signature', '')
            message = robot.parse_message(
                self.request.body,
                timestamp=timestamp,
                nonce=nonce,
                msg_signature=msg_signature
            )
            self.set_header("Content-Type", "application/xml;charset=utf-8")
            self.write(await robot.get_encrypted_reply(message))

    return WeRoBotHandler
