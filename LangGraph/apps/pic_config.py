from IPython.display import Image
from pathlib import Path

def save_png(graph, BASE_DIR, FILENAME):
    image = Image(graph.get_graph().draw_mermaid_png())
    FILENAME = BASE_DIR / "png" / FILENAME
    with open(FILENAME, "wb") as f:
        f.write(image.data)