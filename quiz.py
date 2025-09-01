import json

def load_questions(filename):
    """Load questions from JSON file."""
    with open(filename, "r") as f:
        return json.load(f)

def get_user_answer():
    """Ask for user input until valid (1–4)."""
    while True:
        user_answer = input("Your answer (1/2/3/4): ").strip()
        if user_answer in ["1", "2", "3", "4"]:
            return user_answer
        else:
            print("⚠️ Please select from 4 options (1/2/3/4).")

def run_quiz(questions):
    answers = []  # store (user_answer, correct_answer)
    total = len(questions)

    # Ask all questions
    for idx, q in enumerate(questions, start=1):
        print(f"\nQ{idx}. {q['question']}")
        for i, choice in enumerate(q["choices"], start=1):
            print(f"   {i}. {choice}")

        user_answer = get_user_answer()
        answers.append({
            "question": q["question"],
            "choices": q["choices"],
            "user_answer": user_answer,
            "correct_answer": q["correct_ans"]
        })

    # Show results
    print("\n--- QUIZ RESULTS ---")
    score = 0
    for idx, result in enumerate(answers, start=1):
        q = result["question"]
        choices = result["choices"]
        user_ans = result["user_answer"]
        correct_ans = result["correct_answer"]

        user_text = choices[int(user_ans) - 1]
        correct_text = choices[int(correct_ans) - 1]

        status = "✅ Correct" if user_ans == correct_ans else "❌ Wrong"
        if status.startswith("✅"):
            score += 1

        print(f"\nQ{idx}. {q}")
        print(f"   Your Answer   : {user_text}")
        print(f"   Correct Answer: {correct_text}")
        print(f"   Result        : {status}")

    print("\n--- FINAL SCORE ---")
    print(f"Your Score: {score}/{total}")

if __name__ == "__main__":
    questions = load_questions("quiz.json")
    run_quiz(questions)
