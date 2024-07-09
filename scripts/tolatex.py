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
    with open(input_filename, 'r') as file:
        content = file.read()

    # Replace each tag with its LaTeX equivalent
    for tag in tags:
        content = content.replace(f'<{tag}>', f'\\begin{{{tag}}}')
        content = content.replace(f'</{tag}>', f'\\end{{{tag}}}')

    # Write the modified content to a new LaTeX file
    with open(output_filename, 'w') as file:
        file.write(content)

    print(f"Converted tags and wrote to {output_filename}")

# Example usage
input_filename = 'input.md'  # Replace with your input filename
output_filename = 'output.tex'  # Replace with your desired output filename
convert_tags(input_filename, output_filename)
