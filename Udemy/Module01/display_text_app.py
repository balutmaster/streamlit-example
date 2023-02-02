# Core Pkgs
import streamlit as st 

# Additional pkgs

# Fxns

def main():
    st.title("This is a title")
    st.text("this is the text")
    name = "Rich"
    st.text("this is an example of variable name:  {} " .format(name))

    st.header("This is a header")
    st.subheader("This is a sub-header")
    
    st.markdown("## This is markdown")
    
# Displaying Colored Text/Bootstrap Alert
    st.success("Successful")
    st.warning("Warning") 
    st.info("Information")
    st.error("Error")
    st.exception("Exception")

# Superfunciton
    st.write("This is st.write with normal text")
    st.write("### This is st.write with markdown")
    st.write(" one plus two = " , 1+2)

# Help Info
    st.help(range)
    
if __name__ == '__main__':
    main()
    