# YourKi木 

![YourKi木](https://github.com/anxkhn/YourKi/assets/83116240/5b7ed84b-62cb-4c5f-806a-914450d46545)

YourKi木 is a Streamlit project that empowers you to visualize balanced binary trees based on your custom input and preferences. Craft unique and personalized tree visualizations by choosing the traversal type (Preorder, Inorder, or Postorder) and entering the corresponding traversal order. Additionally, you can customize the graph style to create a distinctive and meaningful tree representation.

## How to Use

1. **Traversal Input:**
   - Enter your custom string for tree traversal. Spaces will be replaced with hyphens.
   
2. **Traversal Type:**
   - Select the traversal type from options: Preorder, Inorder, or Postorder.

3. **Graph Style:**
   - Choose between "Default" and "Custom" graph styles.
     - **Default:** Utilizes predefined styles for simplicity.
     - **Custom:** Tailor the graph style to your liking.
       - Choose node shape (circle, box, ellipse, triangle, diamond).
       - Select node style (filled, solid, dashed, dotted).
       - Pick a node fill color using the color picker.

4. **Visualize:**
   - Click the "Visualize" button to generate and display your customized tree.

5. **Save Image:**
   - Save your tree visualization as an image by clicking the "Save This Image" button.

## About YourKi木

"YourKi木" is a fusion of "Your" for personalization and "Ki" from Japanese, meaning "tree." In Japanese, "木" represents the profound symbolism of trees. This tool allows users to generate customized trees, sending wishes encoded in tree structures—an homage to the Japanese tradition of gifting trees for life and prosperity.

---

### Dependencies

- [Streamlit](https://streamlit.io/)
- [graphviz](https://pypi.org/project/graphviz/)

## Getting Started

1. **Clone the Repository:**
   - Clone the YourKi repository from [github.com/anxkhn/YourKi](https://github.com/anxkhn/YourKi).

     ```bash
     git clone https://github.com/anxkhn/YourKi.git
     ```

2. **Install Dependencies:**
   - Navigate to the project directory and install the required dependencies using pip.

     ```bash
     cd YourKi
     pip install -r requirements.txt
     ```

3. **Run the Application Locally:**
   - Execute the following command to run the Streamlit application on your local machine.

     ```bash
     streamlit run app.py
     ```

Make sure you have a proper environment to run the following command on a Linux environment:

```bash
sudo apt install graphviz
```

This command installs Graphviz on your Linux system.


## Check out the Deployed App

Visit [yourki.streamlit.app](https://yourki.streamlit.app) to explore and interact with the YourKi木 app online. Now you can visualize customized binary trees with ease. Adjust traversal input, select traversal types, and customize graph styles to create unique and personalized tree visualizations.

---

## Author

Made with ❤️ by [Anas Khan](https://github.com/anxkhn)

## Feedback and Contributions

Feel free to open issues or contribute to the project on [GitHub](https://github.com/anxkhn/graphviz). Your feedback and contributions are highly appreciated.
