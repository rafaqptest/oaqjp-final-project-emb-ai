import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
    
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1, 'joy')

    def test_anger(self):
    
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2, 'anger')

    def test_disgust(self):
    
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3, 'disgust')

    def test_sadness(self):
	
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4, 'sadness')

    def test_fear(self):
	
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5, 'fear')
	
unittest.main()
