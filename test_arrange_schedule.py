import unittest
from arrange_schedule import *

class Arrange_Schedule(unittest.TestCase):
    def setUp(self):
        # test_read_system_setting
        keys = ['board_py_dir','shutdown','max_db_log','min_db_activity']
        system_setting = read_system_setting()
        for key in keys:
            assert key in system_setting
        self.system_setting = system_setting

    def test_read_arrange_mode(self):
        keys = ['arrange_sn','arrange_mode','condition']
        receive_msg = read_arrange_mode()
        for key in keys:
            assert key in receive_msg

    def test_crawler_cwb_img(self):
        send_msg = {}
        send_msg['server_dir'] = self.system_setting['board_py_dir']
        send_msg['user_id'] = 1

        receive_msg = crawler_cwb_img(send_msg)
        assert receive_msg['result'] == 'success'

    def test_crawler_inside_img(self):
        receive_msg = crawler_inside_news()
        assert receive_msg['result'] == 'success'

    def test_crawler_techorange_news(self):
        receive_msg = crawler_techorange_news()
        assert receive_msg['result'] == 'success'

    def test_crawler_medium_news(self):
        receive_msg = crawler_medium_news()
        assert receive_msg['result'] == 'success'

if __name__ == "__main__":
    unittest.main()
