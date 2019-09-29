import datetime
import logging
import os

from page_object.logs.properties_utils import Properties


class UserLog:
    def __init__(self):
        pro = Properties("log.properties").get_properties()
        # log_config = {
        #     "filename": pro["filename"],
        #     "level": pro["level"],
        #     "format": pro["format"],
        #     "datefmt": pro["datefmt"]
        # }
        # logging.basicConfig(**log_config)
        self.logger = logging.getLogger()
        self.logger.setLevel(pro["level"])

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_dir = os.path.join(base_dir, 'logs')
        log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        info_log_name = log_dir + '/' + 'info-' + log_file
        error_log_name = log_dir + '/' + 'error-' + log_file
        # 设置文件的handler 这个设置将内容输出到文件中
        file_handler = logging.FileHandler(info_log_name, mode='a', encoding="UTF-8")

        # 流处理器，输入到控制台
        stream_handler = logging.StreamHandler()

        # 将error信息打印到一个专属的日志文件中
        error_handler = logging.FileHandler(error_log_name, mode='a', encoding="UTF-8")
        error_handler.setLevel(logging.ERROR)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)
        self.logger.addHandler(error_handler)

        # 日志的格式化
        formatter = logging.Formatter(datefmt=pro['datefmt'], fmt=pro["format"])

        file_handler.setFormatter(formatter)
        error_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)
        # self.logger = logging.getLogger()
        # self.logger.setLevel("INFO")
        #
        # base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # log_dir = os.path.join(base_dir, 'logs')
        # log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        # info_log_name = log_dir + '/' + 'info-' + log_file
        # error_log_name = log_dir + '/' + 'error-' + log_file
        # # 设置文件的handler 这个设置将内容输出到文件中
        # file_handler = logging.FileHandler(info_log_name, mode='a', encoding="UTF-8")
        #
        # # 流处理器，输入到控制台
        # stream_handler = logging.StreamHandler()
        #
        # # 将error信息打印到一个专属的日志文件中
        # error_handler = logging.FileHandler(error_log_name, mode='a', encoding="UTF-8")
        # error_handler.setLevel(logging.ERROR)
        #
        # self.logger.addHandler(file_handler)
        # self.logger.addHandler(stream_handler)
        # self.logger.addHandler(error_handler)
        #
        # # 日志的格式化
        #
        # formatter = logging.Formatter(fmt=
        #                               '%(asctime)s %(filename)s- %(funcName)s %(lineno)d %(levelname)s - %(message)s')
        #
        # file_handler.setFormatter(formatter)
        # error_handler.setFormatter(formatter)
        # stream_handler.setFormatter(formatter)
        # self.logger.info("this is info logs 和额呵呵额")
        # self.logger.info("this is error 级别的日志")
        # self.logger.error("this is info  和额呵呵额")

    def get_log(self):
        return self.logger


if __name__ == '__main__':
    log = UserLog()
    log.get_log().info('大家好')
