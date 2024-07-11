import re

def markdown_to_latex_list(markdown_lines):
    latex_lines = []
    in_list = False
    list_type = None
    list_items = []
    
    for line in markdown_lines:
        if re.match(r'^\s*[-*+]\s+', line):  # Unordered list item
            if not in_list:
                latex_lines.append(r'\begin{itemize}')
                in_list = True
                list_type = 'itemize'
            list_items.append(line.strip()[2:].strip())
        elif re.match(r'^\s*\d+\.\s+', line):  # Ordered list item
            if not in_list:
                latex_lines.append(r'\begin{enumerate}')
                in_list = True
                list_type = 'enumerate'
            list_items.append(line.strip().split('.', 1)[1].strip())
        else:  # Not a list item
            if in_list:
                if list_type == 'itemize':
                    latex_lines.extend([r'\item {}'.format(item) for item in list_items])
                    latex_lines.append(r'\end{itemize}')
                elif list_type == 'enumerate':
                    latex_lines.extend([r'\item {}'.format(item) for item in list_items])
                    latex_lines.append(r'\end{enumerate}')
                in_list = False
                list_items = []
            latex_lines.append(line.rstrip())

    # Check if there was an open list at the end
    if in_list:
        if list_type == 'itemize':
            latex_lines.extend([r'\item {}'.format(item) for item in list_items])
            latex_lines.append(r'\end{itemize}')
        elif list_type == 'enumerate':
            latex_lines.extend([r'\item {}'.format(item) for item in list_items])
            latex_lines.append(r'\end{enumerate}')
    
    return latex_lines

def convert_tags(input_filename, output_filename):
    # List of tags to replace
    tags = [
        'theorem',
        'conjecture',
        'construction',
        'corollary',
        'definition',
        'example',
        'exercise',
        'lemma',
        'problem',
        'proposition',
        'remark',
        'proof',
        'solution'
    ]
    
    # Read the file content
    with open(input_filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace each tag with its LaTeX equivalent
    for tag in tags:
        content = content.replace(f'<{tag}>', f'\\begin{{{tag}}}')
        content = content.replace(f'</{tag}>', f'\\end{{{tag}}}')

    # Write the modified content to a new LaTeX file
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Converted tags and wrote to {output_filename}")

def main():
    input_filename = 'input.md'  # Replace with your input filename
    output_temp_filename = 'temp.tex'  # Temporary output file
    
    # Step 1: Convert Markdown to LaTeX lists
    with open(input_filename, 'r', encoding='utf-8') as md_file:
        markdown_lines = md_file.readlines()
    
    latex_lines = markdown_to_latex_list(markdown_lines)
    
    with open(output_temp_filename, 'w', encoding='utf-8') as temp_file:
        temp_file.write('\n'.join(latex_lines))
    
    # Step 2: Convert tags in the temporary LaTeX file
    convert_tags(output_temp_filename, 'output.tex')
    
    # Optionally, you may delete the temporary file after conversion
    import os
    os.remove(output_temp_filename)

if __name__ == "__main__":
    main()
