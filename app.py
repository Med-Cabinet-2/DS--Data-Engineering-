"""Code for the Intuitive Medical Marijuana App"""
from dotenv import load_dotenv
from flask import Flask, request
from .predict import Advisor

# Initialize .env file
load_dotenv()


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'Welcome to the Intuitive Medical Marijuana App!'

    @app.route('/advise', methods=['POST'])
    def advise():
        """Generate strain advise from user input as JSON"""
        input = request.get_json(force=True)
        advisor = Advisor()
        advise = advisor.strain_advisor(input["input"])
        string_advise = " ".join(str(i) for i in advise)

        return string_advise

    @app.route('/test')
    def test():
        """test page for baseline API"""
        return 'Congrats!'
    
    return app

if __name__ == "__main__":
    app.run(debug=True)