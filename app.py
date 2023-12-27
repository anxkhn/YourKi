import graphviz
import streamlit as st
import base64


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree_preorder(preorder):
    if not preorder:
        return None
    root_val = preorder.pop(0)
    root = TreeNode(root_val)
    mid_idx = len(preorder) // 2
    root.left = build_tree_preorder(preorder[:mid_idx])
    root.right = build_tree_preorder(preorder[mid_idx:])
    return root


def build_tree_inorder(inorder):
    if not inorder:
        return None
    mid_idx = len(inorder) // 2
    root = TreeNode(inorder[mid_idx])
    root.left = build_tree_inorder(inorder[:mid_idx])
    root.right = build_tree_inorder(inorder[mid_idx + 1 :])
    return root


def build_tree_postorder(postorder):
    if not postorder:
        return None
    root_val = postorder.pop()
    root = TreeNode(root_val)
    mid_idx = len(postorder) // 2
    root.right = build_tree_postorder(postorder[mid_idx:])
    root.left = build_tree_postorder(postorder[:mid_idx])
    return root


def visualize_tree(node, graph=None, parent_id=None, node_style=None):
    if graph is None:
        graph = graphviz.Digraph(format="png")
        graph.attr("node", shape="circle", style="filled", fillcolor="#F8BBD0")
        graph.attr(dpi="350")
        graph.attr(rankdir="TB")
    if node_style is not None:
        graph.attr("node", **node_style)
    if node:
        node_id = str(id(node))
        graph.node(node_id, label=node.val, fontname="Arial")
        if parent_id is not None:
            graph.edge(parent_id, node_id)
        visualize_tree(node.left, graph, node_id, node_style)
        visualize_tree(node.right, graph, node_id, node_style)
    return graph


def save_image_button(tree_graph):
    # Create a download link for the image
    image_data = tree_graph.pipe(format="png")
    b64_image = base64.b64encode(image_data).decode("utf-8")
    href = f'<div style="text-align:center; padding-top: 20px;"><a href="data:image/png;base64,{b64_image}" download="yourki_tree.png"><button style="padding: 10px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">Save This Image</button></a></div>'
    st.markdown(href, unsafe_allow_html=True)


def main():
    st.title("YourKi木")
    st.markdown(
        "YourKi木 is a streamlit project that allows you to visualize balanced binary trees based on "
        "your custom input and preferences. Choose the traversal type (Preorder, Inorder, or Postorder) "
        "and enter the corresponding traversal order. You can also customize the graph style to create a "
        "unique and personalized tree visualization."
    )
    # Get user input for the traversal order
    default_traversal_input = "Happy Birthday Friend"
    traversal_input = st.text_input(
        f"Enter Your String:", default_traversal_input
    ).replace(" ", "-")
    traversal_type = st.radio(
        "Select traversal type:", ["Preorder", "Inorder", "Postorder"]
    )
    st.markdown("---")
    # Get user input for graph style
    graph_style = st.selectbox("Select graph style:", ["Default", "Custom"])
    if graph_style == "Custom":
        node_style = {
            "shape": st.selectbox(
                "Select node shape:",
                ["circle", "box", "ellipse", "triangle", "diamond"],
            ),
            "style": st.selectbox(
                "Select node style:", ["filled", "solid", "dashed", "dotted"]
            ),
            "fillcolor": st.color_picker("Select node fill color:", "#F8BBD0"),
        }
    else:
        node_style = None
    if traversal_input:
        if traversal_type == "Preorder":
            root = build_tree_preorder(list(traversal_input))
        elif traversal_type == "Inorder":
            root = build_tree_inorder(list(traversal_input))
        elif traversal_type == "Postorder":
            root = build_tree_postorder(list(traversal_input))
        tree_graph = visualize_tree(root, node_style=node_style)
        st.image(tree_graph.pipe(format="png"))
        st.markdown(
            '"YourKi木" is a fusion of "Your" for personalization, "Ki" from Japanese meaning "tree". '
            'In Japanese, "木" represents the profound symbolism of trees. This tool allows users to generate customized trees, '
            "sending wishes encoded in tree structures—an homage to the Japanese tradition of gifting trees for life and prosperity."
        )
        save_image_button(tree_graph)
    footer_html = """
    <style>
        .footer {
            
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            background-color: rgba(38, 37, 48,0.5); 
        }
    </style>
    <div class="footer">
        Built with ❤️ by <a href="https://github.com/anxkhn" target="_blank">Anas Khan</a> | Powered by <a href="https://graphviz.gitlab.io/" target="_blank">Graphviz</a>
    </div>
"""
    # Display custom footer
    st.markdown(footer_html, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
