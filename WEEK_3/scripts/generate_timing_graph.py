import graphviz

def generate_graph_from_path(path_file, output_png="critical_path.png"):
    with open(path_file, "r") as f:
        lines = [line.strip().split() for line in f.readlines() if line.strip()]

    dot = graphviz.Digraph(comment="Critical Path Timing Graph", format="png")
    dot.attr(rankdir="LR", fontsize="12", splines="polyline")

    prev_node = None
    for i, (cell, pin, delay) in enumerate(lines):
        node_label = f"{cell}\\n{pin}\\nDelay: {delay} ns"
        node_name = f"n{i}"

        dot.node(node_name, label=node_label, shape="box", style="rounded,filled", fillcolor="lightgrey")

        if prev_node:
            dot.edge(prev_node, node_name, label=f"+{delay} ns")
        prev_node = node_name

    dot.render(output_png.replace(".png", ""), cleanup=True)
    print(f"✅ Critical path graph generated: {output_png}")

if __name__ == "__main__":
    generate_graph_from_path("reports/critical_path_points.txt")

