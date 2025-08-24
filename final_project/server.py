"""
server.py

Flask application for detecting emotions from user-submitted text.
Uses the EmotionDetection package to analyze statements and return
the emotion scores and dominant emotion.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """
    Analyze the emotion of a user-submitted statement.

    Reads the raw POST data, calls the emotion_detector function, and
    returns a formatted string with all emotion scores and the dominant
    emotion. If the input is blank, returns an error message.

    Returns:
        str: Formatted string with emotion scores and dominant emotion,
             or error message if input is invalid.
    """
    text_to_analyze = request.data.decode("utf-8").strip()

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    dominant_emotion = response["dominant_emotion"]
    response_string = (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is <strong>{dominant_emotion}</strong>."
    )

    return response_string


@app.route("/")
def index():
    """
    Render the main HTML page for the application.

    Returns:
        str: Rendered HTML page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    # Run the Flask app on localhost port 5000 in debug mode
    app.run(host="localhost", port=5000, debug=True)
