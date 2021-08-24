import unittest
from survey import AnonymousSurvey

class TestAnonumousSurvey(unittest.TestCase):
    """针对AnonumousSurvey类的测试"""

    # def test_store_single_response(self):
    #     """测试单个答案会被妥善存储"""
    #     question = "What language did you first learn to speak?"
    #     my_survey = AnonymousSurvey(question)
    #     my_survey.store_response('English')
    #
    #     self.assertIn('English', my_survey.responses)
    #
    # def test_store_three_response(self):
    #     """测试三个答案会被妥善存储"""
    #     question = "What language did you first learn to speak?"
    #     my_survey = AnonymousSurvey(question)
    #     responses = ['English', 'Spanish', 'Mandarin']
    #     for response in responses:
    #         my_survey.store_response(response)
    #
    #     for response in responses:
    #         self.assertIn(response, my_survey.responses)


    #使用setUp()方法：可以只创建一次对象
    def setUp(self):
        """创建一个调查对象和一组答案 供测试方法使用"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn('English', self.my_survey.responses)

    def test_store_three_response(self):
        """测试三个答案会被妥善存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()