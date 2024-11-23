from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# Ensure the 'database' directory exists
if not os.path.exists("database"):
    os.makedirs("database")

# Create Flask app
app = Flask(__name__)

# Set database URI using absolute path
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir, 'database', 'data.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Database model
class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    reflections = db.Column(db.Text, nullable=True)

# Initialize database
@app.before_request
def init_db():
    if not hasattr(app, 'db_initialized'):  # Check if already initialized
        db.create_all()
        # Seed initial data only if the database is empty
        if Topic.query.count() == 0:
            topics = [
                Topic(title="Engaged Pedagogy", description="My insights on holistic education."),
                Topic(title="Ethics of AI", description="Reflections on the dangers and benefits of AI."),
                Topic(title="CTE Programs", description="Understanding Career and Technical Education pathways."),
            ]
            db.session.bulk_save_objects(topics)
            db.session.commit()
        app.db_initialized = True  # Mark as initialized to prevent reinitialization

# Homepage
@app.route("/")
def index():
    topics = Topic.query.all()
    return render_template("index.html", topics=topics)

# Topic Details
@app.route("/topic/<int:topic_id>")
def topic(topic_id):
    topic = Topic.query.get_or_404(topic_id)
    return render_template("topic.html", topic=topic)

# Add Reflections
@app.route("/add_reflection/<int:topic_id>", methods=["POST"])
def add_reflection(topic_id):
    topic = Topic.query.get_or_404(topic_id)
    reflection = request.form.get("reflection")
    topic.reflections = f"{topic.reflections or ''}\n{reflection}"
    db.session.commit()
    return redirect(url_for("topic", topic_id=topic_id))

if __name__ == "__main__":
    app.run(debug=True)
