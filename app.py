from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

# Function to run the C code with the given query
def run_c_code(query):
    binary_path = 'querydb'  # Update with the correct path
    command = f"{binary_path} {query}"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    return result.stdout

def read_data_nme():
    data_nme_path = 'index-db/data.nme'  # Update with the correct path
    with open(data_nme_path, 'r') as file:
        lines = file.readlines()
    return [line.split()[1] for line in lines]

def extract_title_and_content(document_path):
    with open(document_path, 'r', encoding='utf-8', errors='replace') as file:
        document_lines = file.readlines()

    document_title = None
    document_h2 = None
    document_content = []

    for line in document_lines:
        if line.startswith('<title>'):
            document_title = line[len('<title>'):-len('</title>')].strip().replace('<', '')
        elif line.startswith('<h2>'):
            document_h2 = line[len('<h2>'):-len('</h2>')].strip().replace('<', '')
        elif line.startswith('<content>'):
            content_line = line[len('<content>'):-len('</content>')].strip().replace('<', '')
            document_content.append(content_line)

    return document_title, document_h2, ' '.join(document_content)

@app.route('/')
def index():
    return render_template('index.html', results=None)

@app.route('/search', methods=['GET', 'POST'])
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
    document_names = read_data_nme()

    for line in output.splitlines():
        parts = line.split()
        if len(parts) == 2:
            doc_id, score = parts
            doc_id = int(doc_id)  # Convert doc_id to integer
            if 0 <= doc_id < len(document_names):
                document_name = document_names[doc_id]
                document_title, _, _ = extract_title_and_content(f'data/{document_name}')
                results.append({'doc_id': doc_id, 'doc_name': document_name, 'score': score, 'doc_title': document_title})
            else:
                print(f"Ignoring line: {line}. Invalid doc_id: {doc_id}")
        else:
            print(f"Ignoring line: {line}. Incorrect format.")

    return results


@app.route('/document/<doc_id>', methods=['GET'])
def show_document(doc_id):
    # Read data.nme to get the document names
    document_names = read_data_nme()

    # Check if the doc_id is valid
    if 0 <= int(doc_id) < len(document_names):
        document_name = document_names[int(doc_id)]

        # Read the title, h2, and content of the document
        document_path = f'data/{document_name}'
        document_title, document_h2, document_content = extract_title_and_content(document_path)

        # Check if both title and content are found
        if document_title and document_content:
            display_text = f"Showing document with ID {doc_id}<br>Name: {document_name}<br>Title: {document_title}"
            if document_h2:
                display_text += f"<br>H2: {document_h2}"
            display_text += f"<br><br>Content: {document_content}"
            return display_text
        else:
            return f"Invalid document format in file: {document_path}"

    else:
        return f"Invalid document ID: {doc_id}"

if __name__ == '__main__':
    app.run(debug=True)
