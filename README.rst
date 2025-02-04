====================================
AsyncWeRoBot
====================================

.. image:: https://github.com/wxw-matt/AsyncWeRoBot/workflows/tests/badge.svg
    :target: https://github.com/wxw-matt/AsyncWeRoBot/actions
.. image:: https://codecov.io/gh/wxw-matt/AsyncWeRoBot/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/wxw-matt/AsyncWeRoBot
.. image:: https://img.shields.io/badge/QQ%20Group-283206829-brightgreen.svg?logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB3aWR0aD0iMTc5MiIgaGVpZ2h0PSIxNzkyIiB2aWV3Qm94PSIwIDAgMTc5MiAxNzkyIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Ik0yNzAgODA2cS04LTE5LTgtNTIgMC0yMCAxMS00OXQyNC00NXEtMS0yMiA3LjUtNTN0MjIuNS00M3EwLTEzOSA5Mi41LTI4OC41dDIxNy41LTIwOS41cTEzOS02NiAzMjQtNjYgMTMzIDAgMjY2IDU1IDQ5IDIxIDkwIDQ4dDcxIDU2IDU1IDY4IDQyIDc0IDMyLjUgODQuNSAyNS41IDg5LjUgMjIgOThsMSA1cTU1IDgzIDU1IDE1MCAwIDE0LTkgNDB0LTkgMzhxMCAxIDEuNSAzLjV0My41IDUgMiAzLjVxNzcgMTE0IDEyMC41IDIxNC41dDQzLjUgMjA4LjVxMCA0My0xOS41IDEwMHQtNTUuNSA1N3EtOSAwLTE5LjUtNy41dC0xOS0xNy41LTE5LTI2LTE2LTI2LjUtMTMuNS0yNi05LTE3LjVxLTEtMS0zLTFsLTUgNHEtNTkgMTU0LTEzMiAyMjMgMjAgMjAgNjEuNSAzOC41dDY5IDQxLjUgMzUuNSA2NXEtMiA0LTQgMTZ0LTcgMThxLTY0IDk3LTMwMiA5Ny01MyAwLTExMC41LTl0LTk4LTIwLTEwNC41LTMwcS0xNS01LTIzLTctMTQtNC00Ni00LjV0LTQwLTEuNXEtNDEgNDUtMTI3LjUgNjV0LTE2OC41IDIwcS0zNSAwLTY5LTEuNXQtOTMtOS0xMDEtMjAuNS03NC41LTQwLTMyLjUtNjRxMC00MCAxMC01OS41dDQxLTQ4LjVxMTEtMiA0MC41LTEzdDQ5LjUtMTJxNCAwIDE0LTIgMi0yIDItNGwtMi0zcS00OC0xMS0xMDgtMTA1LjV0LTczLTE1Ni41bC01LTNxLTQgMC0xMiAyMC0xOCA0MS01NC41IDc0LjV0LTc3LjUgMzcuNWgtMXEtNCAwLTYtNC41dC01LTUuNXEtMjMtNTQtMjMtMTAwIDAtMjc1IDI1Mi00NjZ6IiBmaWxsPSIjZmZmIi8%2BPC9zdmc%2B
    :target: https://jq.qq.com/?_wv=1027&k=449sXsV

AsyncWeRoBot 是一个微信公众号后台开发框架，采用MIT协议发布。由WeRoBot改编而来，感谢原作者的良好设计。

文档在这里： https://async-werobot.readthedocs.org/zh_CN/latest/

安装
========

推荐使用 pip 进行安装 ::

    pip install async-werobot

Hello World
=============

一个非常简单的 Hello World 微信公众号，会对收到的所有文本消息回复 Hello World ::

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

Credits
=======
Contributors
-----------------
Thank you to all the people who have already contributed.
|occontributorimage|

.. |occontributorimage| image:: https://opencollective.com/werobot/contributors.svg?width=890&button=false
    :target: https://opencollective.com/werobot
    :alt: Repo Contributors
