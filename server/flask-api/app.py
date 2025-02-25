from flask import Flask, request, jsonify
from sympy import symbols, solve, Eq

app = Flask(__name__)

@app.route('/api/solve_question', methods=['POST'])
def solve_question():
    data = request.json
    question = data.get('question')  # e.g., "2x + 3 = 5"
    try:
        x = symbols('x')
        left, right = question.split('=')
        eq = Eq(eval(left.strip()), eval(right.strip()))  # Unsafe; refine later
        solution = solve(eq, x)
        proof = "Steps: Subtract {} from both sides, then divide by {}".format(right.strip()[-1], left.strip()[0])
        return jsonify({"solution": str(solution[0]), "proof": proof})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)