import nbformat as nbf
import shutil
import json

def convert_md_to_ipynb(input_path, output_path):
    # Reading the content of the uploaded markdown file
    with open(input_path, 'r') as file:
        content = file.read()

    # Split the content by lines
    lines = content.split('\n')

    # Create a new notebook
    nb = nbf.v4.new_notebook()
    cells = []

    # Parse the lines to create appropriate cells
    code_block = False
    code_lines = []
    is_sql_block = False

    for line in lines:
        if line.startswith('```python'):
            code_block = True
            is_sql_block = False  # Reset SQL block flag
            if code_lines:
                cells.append(nbf.v4.new_markdown_cell('\n'.join(code_lines)))
                code_lines = []
        elif line.startswith('```sql'):
            code_block = True
            is_sql_block = True  # Mark SQL block
            if code_lines:
                cells.append(nbf.v4.new_markdown_cell('\n'.join(code_lines)))
                code_lines = []
        elif line.startswith('```') and code_block:
            code_block = False
            if is_sql_block:
                # Add %sql magic command before the SQL code
                code_lines.insert(0, '%%sql')
            cells.append(nbf.v4.new_code_cell('\n'.join(code_lines)))
            code_lines = []
        else:
            code_lines.append(line)

    # Add remaining lines as a markdown cell
    if code_lines:
        if code_block:
            if is_sql_block:
                code_lines.insert(0, '%%sql')
            cells.append(nbf.v4.new_code_cell('\n'.join(code_lines)))
        else:
            cells.append(nbf.v4.new_markdown_cell('\n'.join(code_lines)))

    # Assign cells to the notebook
    nb.cells = cells

    # Write the notebook to a file
    with open(output_path, 'w') as file:
        nbf.write(nb, file)

prefix_files = [
    '01-intruducao',
    '02-introducao-sql',
    '03-exercicios-criar-tabela',
    '04-exercicios-criar-indices',
    '05-exercicios-alterando-tabelas',
    '06-exercicios-criar-view',
    '07-select-tipos-de-joins',
    '08-exemplos-tipo-de-joins',
    '09-exemplo-subselect',
    '10-funcoes-de-agrupamento',
    '11-exemplos-funcoes-de-agrupamento',
    '12-exemplo-having',
    '13-tipos-de-union',
    '14-exemplo-union',
    '15-exemplo-union-all',
    '16-fase2-o-escopo-aumentou',
    '17-exercicios-sem-gabarito',
    '18-exercicios-gabarito',
]

# Convert the file
for prefix_file in prefix_files:
    convert_md_to_ipynb(
        f'conteudo/{prefix_file}.md',
        f'notebooks/{prefix_file}.ipynb')
