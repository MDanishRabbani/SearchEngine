from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

# Function to run the C code with the given query
def run_c_code(query):
    binary_path = 'querydb'  # Update with the correct path
    command = f"{binary_path} {query}"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    return result.stdout

@app.route('/')
def index():
    return render_template('index.html', results=None)

@app.route('/search', methods=['POST'])
def search():
    # Get the query from the form
    query = request.form.get('search_query')

    if query:
        # Run the C code with the query
        c_output = run_c_code(query)

        # Parse the C code output
        results = parse_c_output(c_output)

        return render_template('index.html', results=results, query=query)
    else:
        # Handle the case where the query is empty
        return render_template('index.html', results=None, query=None, error="Please enter a query.")

def parse_c_output(output):
    results = []
    for line in output.splitlines():
        parts = line.split()
        if len(parts) == 2:
            doc_id, score = parts
            results.append({'doc_id': doc_id, 'score': score})
        else:
            # Handle the case where the line doesn't have exactly two parts
            print(f"Ignoring line: {line}")

    return results

@app.route('/document/<doc_id>', methods=['GET'])
def show_document(doc_id):
    # Add logic to retrieve and display the document with the given doc_id
    # ...

    # For now, let's return a simple message
    return f"Showing document with ID {doc_id}"

if __name__ == '__main__':
    app.run(debug=True)
