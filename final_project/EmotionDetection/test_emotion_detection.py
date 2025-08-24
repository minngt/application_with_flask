import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotions(self):
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]

        for statement, expected in test_cases:
            with self.subTest(statement=statement): 
                emotions = emotion_detector(statement)
                self.assertEqual(emotions['dominant_emotion'], expected)

if __name__ == '__main__':
    unittest.main()
