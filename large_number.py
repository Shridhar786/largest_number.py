import streamlit as st

def largest_num(num1, num2, num3):
    """
    Returns the largest number among the three given numbers
    """
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3
    return largest

st.title("Find the Largest Number")

num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")
num3 = st.number_input("Enter the third number")

if st.button("Find the largest number"):
    result = largest_num(num1, num2, num3)
    st.write(f"The largest number is {result}")
