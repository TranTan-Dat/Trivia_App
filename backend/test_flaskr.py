import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.database_name = "trivia"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        
        self.app = create_app({
            "SQLALCHEMY_DATABASE_URI": self.database_path
        })

        self.client = self.app.test_client

    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_categories(self):
        """Test for getting categories"""
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['categories']) > 0)
        
    def test_delete_question(self):
        """Test for deleting a question"""
        res = self.client().delete('/questions/19')  # Ensure questionId 19 exists in our db
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted'], 19)
        
    def test_get_questions(self):
        """Test for getting questions"""
        res = self.client().get('/questions?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['questions']) > 0)
        
    def test_delete_question_not_found(self):
        """Test for deleting a question that does not exist"""
        res = self.client().delete('/questions/9999')  # Not exist this id on our db
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        
    def test_create_question(self):
        """Test for creating a new question"""
        new_question = {
            'question': 'What is the capital of France?',
            'answer': 'Paris',
            'category': 1,
            'difficulty': 1
        }
        res = self.client().post('/questions', json=new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertTrue(data['success'])
        self.assertTrue(data['created'])
        
    def test_create_question_bad_request(self):
        """Test for creating a question with missing fields"""
        new_question = {
            'question': 'What is the capital of France?'
            # Missing answer, category, and difficulty
        }
        res = self.client().post('/questions', json=new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])

    def test_search_question(self):
        """Test for searching a question"""
        search_term = {'searchTerm': 'France'}
        res = self.client().post('/questions/search', json=search_term)
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['questions']) > 0)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()