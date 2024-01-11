from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample Q&A Data
qa_data = {
    "Technology": {
        "What is Python?": "Python is a programming language.",
        "What is machine learning?": "Machine learning is a field of artificial intelligence that uses statistical techniques to give computer systems the ability to learn from data.",
        "What does HTML stand for?": "HTML stands for HyperText Markup Language.",
        "What is an IP address?": "An IP address is a unique address that identifies a device on the internet or a local network.",
        "What is blockchain?": "Blockchain is a system of recording information in a way that makes it difficult or impossible to change, hack, or cheat the system."
    },
    "Science": {
        "What is photosynthesis?": "It's a process used by plants to convert light into energy.",
        "What is the theory of relativity?": "The theory of relativity, developed by Albert Einstein, describes the laws of physics in relation to various states of motion.",
        "What are Newton's three laws of motion?": "Newton's three laws of motion describe the relationship between a body and the forces acting upon it, and its motion in response to those forces.",
        "What is DNA?": "DNA, or deoxyribonucleic acid, is the hereditary material in humans and almost all other organisms.",
        "What is a black hole?": "A black hole is a region of space where the gravitational pull is so strong that nothing, not even light, can escape from it."
    },
    "History": {
        "Who was Cleopatra?": "Cleopatra was the last active ruler of the Ptolemaic Kingdom of Egypt.",
        "What was the Renaissance?": "The Renaissance was a period of European history marking the transition from the Middle Ages to modernity.",
        "When did the World War II begin?": "World War II began in 1939.",
        "What was the Industrial Revolution?": "The Industrial Revolution was a period of major industrialization that took place during the late 1700s and early 1800s.",
        "Who discovered America?": "Christopher Columbus is credited with discovering America in 1492."
    },
    "Geography": {
        "What is the largest ocean?": "The Pacific Ocean is the largest and deepest ocean on Earth.",
        "What is the highest mountain in the world?": "Mount Everest is the highest mountain in the world.",
        "What is a desert?": "A desert is a barren area of landscape where little precipitation occurs.",
        "How many continents are there?": "There are seven continents on Earth.",
        "What is the longest river in the world?": "The Nile River is commonly regarded as the longest river in the world."
    },
    "Mathematics": {
        "What is Pythagoras' theorem?": "It states that in a right triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides.",
        "What is a prime number?": "A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.",
        "What is algebra?": "Algebra is a branch of mathematics dealing with symbols and the rules for manipulating those symbols.",
        "What is the Fibonacci sequence?": "The Fibonacci sequence is a series of numbers where the next number is found by adding up the two numbers before it.",
        "What is calculus?": "Calculus is a branch of mathematics that involves the study of rates of change and accumulation."
    },
    "Literature": {
        "Who wrote '1984'?": "George Orwell is the author of '1984'.",
        "What is Shakespeare known for?": "Shakespeare is known for his plays and sonnets.",
        "What is a haiku?": "A haiku is a traditional form of Japanese poetry that consists of three lines.",
        "Who is the author of 'Pride and Prejudice'?": "Jane Austen is the author of 'Pride and Prejudice'.",
        "What is the theme of 'The Great Gatsby'?": "The theme of 'The Great Gatsby' deals with the American Dream and its fallacies."
    },
    "Art": {
        "What is Impressionism?": "Impressionism is an art movement characterized by small, thin brush strokes and an emphasis on the accurate depiction of light.",
        "Who painted the Mona Lisa?": "The Mona Lisa was painted by Leonardo da Vinci.",
        "What is cubism?": "Cubism is an early 20th-century art movement that brought European painting and sculpture historically forward toward 20th century Modern art.",
        "Who is Pablo Picasso?": "Pablo Picasso was a Spanish painter, sculptor, printmaker, and is widely regarded as one of the most influential artists of the 20th century.",
        "What is surrealism?": "Surrealism is a 20th-century avant-garde movement in art and literature which sought to release the creative potential of the unconscious mind."
    }
}



#@app.route('/')
#def home():
#    return render_template('index.html', categories=qa_data.keys())
@app.route('/')
def home():
    return render_template('index.html', categories=list(qa_data.keys()))

@app.route('/get_questions', methods=['POST'])
def get_questions():
    category = request.form['category']
    questions = list(qa_data[category].keys())
    return jsonify(questions)

@app.route('/get_answer', methods=['POST'])
def get_answer():
    category = request.form['category']
    question = request.form['question']
    answer = qa_data[category][question]
    return jsonify(answer)

if __name__ == '__main__':
    app.run(debug=True)

