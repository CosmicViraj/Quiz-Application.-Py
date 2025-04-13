import tkinter as tk
from tkinter import messagebox

# Quiz data: list of dictionaries
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris",
        "explanation": "Paris is the capital and most populous city of France."
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars",
        "explanation": "Mars is called the Red Planet due to the iron oxide (rust) on its surface."
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean",
        "explanation": "The Pacific Ocean is the largest and deepest ocean on Earth."
    },
    {
    "question": "Who developed the theory of relativity?",
    "options": ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Galileo Galilei"],
    "answer": "Albert Einstein",
    "explanation": "Albert Einstein developed the theory of relativity, which revolutionized modern physics."
    },
    {
    "question": "What is the powerhouse of the cell?",
    "options": ["Nucleus", "Mitochondria", "Ribosome", "Golgi apparatus"],
    "answer": "Mitochondria",
    "explanation": "Mitochondria are known as the powerhouse of the cell because they generate most of the cell's energy."
    },
    { 
    "question": "Which language is used to style web pages?",
    "options": ["HTML", "Python", "JavaScript", "CSS"],
    "answer": "CSS",
    "explanation": "CSS (Cascading Style Sheets) is used to style and layout web pages."
    },
    {
    "question": "What is the chemical symbol for water?",
    "options": ["O2", "H2O", "CO2", "NaCl"],
    "answer": "H2O",
    "explanation": "H2O is the chemical formula for water, consisting of two hydrogen atoms and one oxygen atom."
    },
    {
    "question": "Which country is known as the Land of the Rising Sun?",
    "options": ["India", "China", "Japan", "Thailand"],
    "answer": "Japan",
    "explanation": "Japan is called the Land of the Rising Sun because it lies to the east of China, where the sun rises."
    },
    {
    "question": "Which gas is most abundant in the Earth's atmosphere?",
    "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
    "answer": "Nitrogen",
    "explanation": "Nitrogen makes up about 78% of the Earth's atmosphere."
    },
    {
    "question": "Who painted the Mona Lisa?",
    "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
    "answer": "Leonardo da Vinci",
    "explanation": "The Mona Lisa was painted by Leonardo da Vinci, one of the most famous artists of the Renaissance."
    },
    {
    "question": "Which is the smallest prime number?",
    "options": ["0", "1", "2", "3"],
    "answer": "2",
    "explanation": "2 is the smallest and the only even prime number."
    },
    {
    "question": "How many continents are there on Earth?",
    "options": ["5", "6", "7", "8"],
    "answer": "7",
    "explanation": "There are 7 continents: Asia, Africa, North America, South America, Antarctica, Europe, and Australia."
    },
    {
    "question": "Which instrument is used to measure temperature?",
    "options": ["Barometer", "Thermometer", "Hygrometer", "Altimeter"],
    "answer": "Thermometer",
    "explanation": "A thermometer is used to measure temperature in degrees Celsius or Fahrenheit."
    }

]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz with Explanation")
        self.root.geometry("500x400")
        
        self.question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=450)
        self.question_label.pack(pady=20)
        
        self.selected_option = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(root, text="", variable=self.selected_option, font=("Arial", 12), value="", anchor="w")
            btn.pack(fill='x', padx=50, pady=2)
            self.option_buttons.append(btn)
        
        self.submit_btn = tk.Button(root, text="Submit", command=self.check_answer, font=("Arial", 14), bg="blue", fg="white")
        self.submit_btn.pack(pady=20)
        
        self.current_question = 0
        self.score = 0
        self.load_question()
    
    def load_question(self):
        if self.current_question < len(quiz_data):
            q = quiz_data[self.current_question]
            self.question_label.config(text=f"Q{self.current_question+1}: {q['question']}")
            self.selected_option.set(None)
            for i, option in enumerate(q["options"]):
                self.option_buttons[i].config(text=option, value=option)
        else:
            self.show_score()

    def check_answer(self):
        selected = self.selected_option.get()
        if not selected:
            messagebox.showwarning("No Selection", "Please select an option.")
            return
        
        correct_answer = quiz_data[self.current_question]["answer"]
        explanation = quiz_data[self.current_question]["explanation"]
        
        if selected == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", f"Good job!\n\nExplanation: {explanation}")
        else:
            messagebox.showerror("Wrong!", f"Oops! The correct answer is: {correct_answer}\n\nExplanation: {explanation}")
        
        self.current_question += 1
        self.load_question()

    def show_score(self):
        messagebox.showinfo("Quiz Completed", f"Your Score: {self.score} out of {len(quiz_data)}")
        self.root.destroy()

# Run the app
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
