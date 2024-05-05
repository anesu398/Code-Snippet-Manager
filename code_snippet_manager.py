import json
import os

class CodeSnippetManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.snippets = {}
        self.load_snippets()

    def load_snippets(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                self.snippets = json.load(file)

    def save_snippets(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.snippets, file, indent=4)

    def add_snippet(self, name, code):
        self.snippets[name] = code
        self.save_snippets()

    def delete_snippet(self, name):
        if name in self.snippets:
            del self.snippets[name]
            self.save_snippets()

    def get_snippet(self, name):
        return self.snippets.get(name, None)

    def list_snippets(self):
        return list(self.snippets.keys())

# Example usage:
if __name__ == "__main__":
    snippet_manager = CodeSnippetManager("snippets.json")
    
    # Add new snippets
    snippet_manager.add_snippet("Hello World", "print('Hello, world!')")
    snippet_manager.add_snippet("Factorial", "def factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n - 1)")

    # List snippets
    print("List of snippets:")
    for name in snippet_manager.list_snippets():
        print(f"- {name}")

    # Get a specific snippet
    snippet_name = "Hello World"
    snippet_code = snippet_manager.get_snippet(snippet_name)
    if snippet_code:
        print(f"\nCode for '{snippet_name}':\n{snippet_code}")

    # Delete a snippet
    snippet_manager.delete_snippet("Factorial")
    print("\nList of snippets after deletion:")
    for name in snippet_manager.list_snippets():
        print(f"- {name}")
