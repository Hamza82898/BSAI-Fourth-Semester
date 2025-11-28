from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

admission_info = {
    "requirements": "You need: high school diploma, transcripts, English proficiency test (IELTS/TOEFL), and application form.",
    "deadlines": "Fall intake: June 1 • Spring intake: November 1.",
    "programs": "We offer programs in Computer Science, Business, Engineering, Psychology, and Arts.",
    "scholarships": "Merit-based and need-based scholarships are available. Deadlines follow admission deadlines."
}

def get_bot_response(user_msg):
    msg = user_msg.lower()

    if "requirements" in msg:
        return admission_info["requirements"]
    
    elif "deadlines" in msg:
        return admission_info["deadlines"]
    
    elif "program" in msg:
        return admission_info["programs"]
    
    elif "scholarship" in msg:
        return admission_info["scholarships"]
    
    elif "hello" in msg or "hi" in msg:
        return "Hello! How can I assist you with university admissions today?"
    else:
        return "I'm sorry, I don't have information on that topic. Please ask about admission requirements, deadlines, programs, or scholarships."
    
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_msg = request.form["message"]
    return jsonify({"response": get_bot_response(user_msg)})

if __name__ == "__main__":
    app.run(debug=True)
