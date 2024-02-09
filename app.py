import streamlit as st
from sympy import Symbol, diff, simplify

def main():
    st.title("Derivative Calculator")
    st.write('Noah Rubin')

    # Get user input for the expression
    expression = st.text_input("Enter a mathematical expression")

    # Get user input for the variable with respect to which the derivative will be calculated
    variable = st.text_input("Enter the variable for differentiation")

    # Calculate and display the derivative
    if expression and variable:
        try:
            x = Symbol(variable)
            derivative = diff(expression, x)
            derivative = simplify(derivative)
            st.write("The derivative of", expression, "with respect to", variable, "is:")
            st.latex(derivative)
        except Exception as e:
            st.write("Error:", e)

if __name__ == "__main__":
    main()
