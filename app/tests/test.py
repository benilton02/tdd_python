from datetime import datetime
from unittest import(
    TestCase,
    main, 
    mock  
) 
from app.main import(
    new_task, 
    process_date,
    tasks_list    
)


"""
{
    id: int
    task_name: str
    date: datetime.datetime
    status = str['TODO', 'INPROGRESS', 'DONE']
}
"""


class Testapp(TestCase):


    def test_new_task(self):
        esperado= {
            'id': 0,
            'task_name': 'ligar pro will',
            'date': datetime(2019, 2, 19, 0, 0,0),
            'status': "TODO"
        }
        resultado = new_task('ligar pro will', '19/02/2019')
        self.assertEqual(esperado, resultado)


    @mock.patch('app.main.process_date')
    def test_process_date_value(self, mocked):
        new_task('', '19/02/2019')
        mocked.assert_called_with('19/02/2019')


    @mock.patch('app.main.insert_task')
    def test_insert_task(self, mocked):
        resultado = new_task('ligar pro will', '19/02/2019')
        mocked.assert_called_with(resultado)


class TestProcessDate(TestCase):
    

    def test_process_date(self):
        esperado = datetime(2019, 2, 19, 0, 0,0)
        resultado = process_date('19/02/2019')
        self.assertEqual(esperado, resultado)


class TestTasksList(TestCase):
    

    def test_tasks_list(self):
        tasks_list()

    
if __name__ == "__main__":
    main