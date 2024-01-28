import os
import unittest
import sqlite3

from main import App

class TestApp(unittest.TestCase):

    def setUp(self):
        self.db = sqlite3.connect('test.db')
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE test(id INTEGER PRIMARY KEY, temp TEXT)
        ''')
        self.db.commit()

    def test_ingest_data(self):
        app = App(self.db)
        app.ingest_data('test.csv')
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM test')
        result = cursor.fetchall()
        self.assertEqual(result, [(1, 'test'),(2, 'test2')])
        

    def tearDown(self):
        if self.db.conn:
            self.db.conn.close()
        os.remove('test.db')