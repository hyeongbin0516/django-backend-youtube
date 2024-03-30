# db에 정상적으로 연결됬는지 확인
from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2OplError

from django.test import SimpleTestCase
from django.db.utils import OperationalError
from django.core.management import call_command

# db 연결 시뮬
@patch('django.db.utils.ConnectionHandler.__getitem__')
class CommandTests(SimpleTestCase):
    # 성공 했을때
    def test_wait_for_db_ready(self, patched_getitem):
        patched_getitem.return_value = True

        call_command('wait_for_db')

        self.assertEqual(patched_getitem.call_count, 1)

    # 실패 or 지연 됐을 때
    @patch('time.sleep', return_value=None)
    def test_wait_for_db_delay(self, patched_sleep,patched_getitem):
        patched_getitem.side_effect = [Psycopg2OplError] \
            + [OperationalError]*5 + [True]
        call_command('wait_for_db')

        self.assertEqual(patched_getitem.call_count, 7)