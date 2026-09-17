import nbformat as nbf

def py_to_ipynb(py_file, ipynb_file):
    with open(py_file, 'r', encoding='utf-8') as f:
        code = f.read()

    # 创建一个新的 Notebook
    nb = nbf.v4.new_notebook()
    # 将代码按空行分割，生成多个代码单元格
    cells = []
    for cell in code.split('\n\n'):
        cells.append(nbf.v4.new_code_cell(cell))
    nb['cells'] = cells

    # 保存为 .ipynb 文件
    with open(ipynb_file, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)

# 使用示例
py_to_ipynb('lesson1.py', 'lesson1.ipynb')