
import datetime
import logging
import os

from logs.log_one.properties_utils import Properties


class GetLog:
    def set_log_config(self):
        pro = Properties("log.properties").get_properties()
        log_config = {
            "filename": pro["filename"],
            "level": pro["level"]
        }

        logging.basicConfig(**log_config)

        logging.debug("debug")

    @staticmethod
    def set_log_config_1():
        pro = Properties("/Users/anxiaodong/PycharmProjects/sty_env/page_object/logs/log.properties").get_properties()
        # log_config = {
        #     "filename": pro["filename"],
        #     "level": pro["level"],
        #     "format": pro["format"],
        #     "datefmt": pro["datefmt"]
        # }
        # logging.basicConfig(**log_config)
        logger = logging.getLogger()
        logger.setLevel(pro["level"])

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_dir = os.path.join(base_dir, 'logs')
        log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        info_log_name = log_dir + '/' + 'info-' + log_file
        error_log_name = log_dir + '/' + 'error-' + log_file
        # 设置文件的handler 这个设置将内容输出到文件中
        file_handler = logging.FileHandler(info_log_name, mode='a', encoding="UTF-8")

        # 流处理器，输入到控制台
        # stream_handler = logging.StreamHandler()

        # 将error信息打印到一个专属的日志文件中
        error_handler = logging.FileHandler(error_log_name, mode='a', encoding="UTF-8")
        error_handler.setLevel(logging.ERROR)

        logger.addHandler(file_handler)
        # logger.addHandler(stream_handler)
        logger.addHandler(error_handler)

        # 日志的格式化
        formatter = logging.Formatter(datefmt=pro['datefmt'], fmt=pro["format"])

        file_handler.setFormatter(formatter)
        error_handler.setFormatter(formatter)
        # stream_handler.setFormatter(formatter)


if __name__ == '__main__':
    # set_log_config()
    GetLog().set_log_config_1()
    logging.info("hehfdsafdsafdsafdsafdseh")