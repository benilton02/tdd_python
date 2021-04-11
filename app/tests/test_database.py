from unittest import TestCase, main, mock
from app.database import select_task
import pprint

tasks =[
    {'id': 0 ,'task_name': 'sleep', 'date':'?', 'status': 'TODO' },
    {'id': 1 ,'task_name': 'sleep', 'date':'?', 'status': 'TODO' },
    {'id': 2 ,'task_name': 'wakeup', 'date':'?', 'status': 'TODO' },
    {'id': 3 ,'task_name': 'wakeup', 'date':'?', 'status': 'TODO' },
    {'id': 4 ,'task_name': 'wakeup', 'date':'?', 'status': 'TODO' },
]

class TestaDatabase(TestCase):
 

    @mock.patch("app.database.db", new = tasks)
    def test_select_task_wake_up(self):
        results = select_task('wakeup', None)                            
        
        for result in results:
            with self.subTest(f'wakeup in {result}'):
                self.assertEqual('wakeup', result['task_name'])

        # list(map(lambda restul: self.subTest(self.assertEqual('wake', restul['task_name'])), results))


if __name__ == "__main__":
    main