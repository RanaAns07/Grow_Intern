class Response:
    def answers(self, question: str) -> str:
        # Normalize the input
        self.question = question.lower().strip()

        # Python Basics
        if (
            "what is python" in self.question
            or "tell me about python" in self.question
            or "explain python" in self.question
        ):
            return "Python is a versatile, high-level programming language known for its simplicity and readability. It’s widely used in web development, data science, AI, and automation."

        if (
            "why learn python" in self.question
            or "benefits of python" in self.question
            or "why is python popular" in self.question
        ):
            return "Python is easy to learn, has a vast library ecosystem, and is used in many fields like AI, web development, and data science, making it highly in-demand."

        # Python Features
        if (
            "python features" in self.question
            or "what are python features" in self.question
            or "key features of python" in self.question
        ):
            return "Python is simple, interpreted, versatile, supports multiple paradigms (OOP, procedural, functional), and has extensive libraries and community support."

        # Python Applications
        if (
            "python uses" in self.question
            or "what can python do" in self.question
            or "applications of python" in self.question
        ):
            return "Python is used for web development (Django, Flask), AI and machine learning (TensorFlow, PyTorch), data analysis (pandas, NumPy), game development, and scripting."

        # Learning Python
        if (
            "how to learn python" in self.question
            or "best way to learn python" in self.question
            or "python learning resources" in self.question
        ):
            return "Start with online tutorials (Codecademy, Coursera, freeCodeCamp), practice on coding platforms (HackerRank, LeetCode), and build small projects to apply what you learn."

        # Python Syntax
        if (
            "python syntax" in self.question
            or "is python syntax easy" in self.question
            or "how does python syntax work" in self.question
        ):
            return "Python's syntax is simple and resembles plain English. It uses indentation instead of braces, making it easy to read and write."

        # Debugging and Errors
        if (
            "common python errors" in self.question
            or "python debugging tips" in self.question
            or "how to fix python errors" in self.question
        ):
            return "Common errors include syntax errors, indentation errors, and type errors. Use tools like pdb for debugging and always check your code carefully."

        # Python Career Opportunities
        if (
            "python jobs" in self.question
            or "careers in python" in self.question
            or "python career opportunities" in self.question
        ):
            return "Python offers careers in web development, data science, AI, machine learning, automation, and more. Its demand is growing across industries."

        # Python Frameworks
        if (
            "python frameworks" in self.question
            or "popular python frameworks" in self.question
            or "which python frameworks are best" in self.question
        ):
            return "Popular Python frameworks include Django and Flask for web development, TensorFlow for AI, and PyTorch for machine learning."

        # Python Libraries
        if (
            "python libraries" in self.question
            or "important python libraries" in self.question
            or "most used python libraries" in self.question
        ):
            return "Common Python libraries include NumPy, pandas, Matplotlib, TensorFlow, Flask, and requests. Each serves specific purposes, from data analysis to web development."

        # Python Community Support
        if (
            "python community" in self.question
            or "how to get python help" in self.question
            or "where to ask python questions" in self.question
        ):
            return "You can seek help on platforms like Stack Overflow, Python forums, Reddit, or GitHub. Python’s community is large and very supportive."

        # Python Advanced Topics
        if (
            "advanced python topics" in self.question
            or "python for experts" in self.question
            or "what to learn after python basics" in self.question
        ):
            return "After mastering the basics, explore advanced topics like decorators, generators, multiprocessing, data structures, algorithms, and web frameworks like Django or Flask."

        # Default response for unrecognized inputs
        return "I'm not sure about that. Can you rephrase or ask something else about Python?"
