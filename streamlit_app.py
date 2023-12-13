import streamlit as st

def find_largest_number(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Largest Number Finder")

    # Input for three numbers
    num1 = st.number_input("Enter the first number:", value=0)
    num2 = st.number_input("Enter the second number:", value=0)
    num3 = st.number_input("Enter the third number:", value=0)

    # Find the largest number
    result = find_largest_number(num1, num2, num3)

    # Display the result
    st.write(f"The largest number is: {result}")

if __name__ == "__main__":
    main()
