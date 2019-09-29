from page_object.logs.getlog import UserLog


class Demo:
    logger = UserLog().get_log()

    def he(self):
        self.logger.info('呵呵呵呵')
        print("hello world")


Demo().he()
