import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        self.assertEqual(emotion_detector("I am happy")["dominant_emotion"], "joy")

    def test_anger(self):
        self.assertEqual(emotion_detector("I am angry")["dominant_emotion"], "anger")

    def test_sadness(self):
        self.assertEqual(emotion_detector("I am sad")["dominant_emotion"], "sadness")

    def test_fear(self):
        self.assertEqual(emotion_detector("I am scared")["dominant_emotion"], "fear")

    def test_disgust(self):
        self.assertEqual(emotion_detector("I feel disgusted")["dominant_emotion"], "disgust")

if __name__ == "__main__":
    unittest.main()