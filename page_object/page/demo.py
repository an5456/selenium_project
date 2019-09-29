from page_object.logs.getlog import UserLog


class Demo:
    def demo(self):
        logger = UserLog().get_log()
        logger.info("hehfehfhehfhe")


s = Demo()
s.demo()