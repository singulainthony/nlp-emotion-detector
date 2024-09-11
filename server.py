from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detection")


@app.route('/')
def render_homepage():
    """ Render homepage """
    return render_template("index.html")


@app.route('/emotionDetector', methods=["GET"])
def emotion_analysis():
    """ Analyze text and return emotion detection (analysis result) """
    textToAnalyze = request.args["textToAnalyze"]
    analysisResult = emotion_detector(textToAnalyze)

    # Required output format:
    # For the given statement, the system response is '<emotion1>': <score1>,
    # '<emotion2>': <score2>, '<emotionN>': <scoreN>. The dominant emotion is <emotion>.
    #
    # Required output format when dominant_emotion == None:
    # Invalid text! Please try again.
    if analysisResult["dominant_emotion"] == None:
        response = "Invalid text! Please try again!"
    else:
        response = "For the given statement, the system response is"

        for key, value in analysisResult.items():
            # dominant emotion is mentioned separately as its own sentence.
            if key != "dominant_emotion":
                response += f" '{key}': {value},"
            
        # Replace last comma with point. If index is -1, no commas found.
        last_comma_index = response.rfind(",")
        if last_comma_index != -1:
            response = response[:last_comma_index] + '.' + response[last_comma_index + 1:]
        
        response += f" The dominant emotion is {analysisResult['dominant_emotion']}."

    return response


# To make sure that the server only runs when the script is executed
# directly (not imported as a module)
if __name__ == "__main__":
    app.run(debug = True)