# Code Snippet Manager

This project is a simple Python-based code snippet manager that allows you to organize and store code snippets for easy access and retrieval.

## Features

- **Add Snippets**: Add new code snippets with a name and corresponding code.
- **Delete Snippets**: Delete existing code snippets by name.
- **Get Snippets**: Retrieve code snippets by name.
- **List Snippets**: List all available code snippets.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/anesu398/code-snippet-manager.git
    ```

2. Navigate to the project directory:

    ```bash
    cd code-snippet-manager
    ```

3. Run the script:

    ```bash
    python code_snippet_manager.py
    ```

## Usage

1. Initialize the `CodeSnippetManager`:

    ```python
    snippet_manager = CodeSnippetManager("snippets.json")
    ```

2. Add new snippets:

    ```python
    snippet_manager.add_snippet("Snippet Name", "Your code snippet here")
    ```

3. Delete snippets:

    ```python
    snippet_manager.delete_snippet("Snippet Name")
    ```

4. Get a specific snippet:

    ```python
    snippet_code = snippet_manager.get_snippet("Snippet Name")
    ```

5. List all snippets:

    ```python
    snippet_names = snippet_manager.list_snippets()
    ```

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or find any issues, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
