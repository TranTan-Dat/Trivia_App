import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category
from dotenv import load_dotenv

load_dotenv()


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.database_name = os.getenv('DB_NAME')
        self.database_path = "postgresql://{}/{}".format(
            os.getenv('DB_PATH'), self.database_name)
        
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
    
    # Category Endpoints
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

        
    def test_get_questions_success(self):
        """Test for getting questions"""
        """Test successful retrieval of paginated questions"""
        res = self.client().get('/questions?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['questions']) > 0)
        
    def test_get_questions_failure(self):
        """Test retrieval failure with invalid pagination"""
        res = self.client().get('/questions?page=1000')  # Out of range
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 500)
        self.assertEqual(data['message'], "Internal server error")
        
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
        
    def test_search_question_failure(self):
        """Test search failure when no results match the search term"""
        search_term = {'searchTerm': 'nonexistentword'}
        res = self.client().post('/questions/search', json=search_term)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['questions'], [])
        
    def test_play_quiz_success(self):
        quiz_data = {
            'previous_questions': [],
            'quiz_category': {'type': 'Science', 'id': 1}
        }
        res = self.client().post('/quizzes', json=quiz_data)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIn('question', data)

    def test_play_quiz_failure(self):
        """Test failure when playing quiz with an invalid category"""
        quiz_data = {
            'previous_questions': [],
            'quiz_category': {'type': 'Nonexistent', 'id': 999}
        }
        res = self.client().post('/quizzes', json=quiz_data)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsNone(data['question'])
        
    def test_get_categories_failure(self):
        # Assuming an empty database scenario
        Category.query.delete()
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertFalse(data['success'])
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()