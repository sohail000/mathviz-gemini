import streamlit as st
from config import MATH_FUNCTIONS, GeminiConfig
from gemini_adapter import GeminiAdapter
from visualizer import MathVisualizer
from dotenv import load_dotenv
import os

# Load environment variables at startup
load_dotenv()

# Set page configuration
st.set_page_config(layout="wide", page_title="Math Function Visualizer")

def init_session_state():
    """Initialize the session state with Gemini adapter."""
    if 'gemini' not in st.session_state:
        api_key = os.getenv('GOOGLE_API_KEY')
        
        if not api_key:
            st.error("Please set your GOOGLE_API_KEY in the .env file")
            st.stop()
            
        gemini_config = GeminiConfig()
        adapter = GeminiAdapter(api_key)
        adapter.setup_model(gemini_config)
        st.session_state['gemini'] = adapter

def render_function_selection():
    """Render the function selection interface with parameters."""
    # Use columns for main layout
    left_col, right_col = st.columns([2, 1])
    
    with left_col:
        # Function selection in a more compact layout
        st.markdown("### Function Configuration")
        
        # Two columns for function inputs
        func_col1, func_col2 = st.columns(2)
        
        with func_col1:
            st.markdown("**First Function**")
            func1_name = st.selectbox(
                "Select",
                options=list(MATH_FUNCTIONS.keys()),
                key="func1",
                label_visibility="collapsed"
            )
            
            param1 = st.number_input(
                f"Parameter",
                value=MATH_FUNCTIONS[func1_name].default_param,
                step=0.1,
                key="param1"
            )
            
            expression1 = MATH_FUNCTIONS[func1_name].expression_template.format(param=param1)
            st.latex(expression1.replace('np.', '').replace('**', '^'))
        
        with func_col2:
            st.markdown("**Second Function**")
            compatible_funcs = MATH_FUNCTIONS[func1_name].compatible_functions
            func2_name = st.selectbox(
                "Select",
                options=compatible_funcs,
                key="func2",
                label_visibility="collapsed"
            )
            
            if func2_name in MATH_FUNCTIONS:
                param2 = st.number_input(
                    f"Parameter",
                    value=MATH_FUNCTIONS[func2_name].default_param,
                    step=0.1,
                    key="param2"
                )
                
                expression2 = MATH_FUNCTIONS[func2_name].expression_template.format(param=param2)
                st.latex(expression2.replace('np.', '').replace('**', '^'))
    
    with right_col:
        st.markdown("### X-Axis Range")
        range_col1, range_col2 = st.columns(2)
        with range_col1:
            x_min = st.number_input("Min", value=-5.0, step=0.5)
        with range_col2:
            x_max = st.number_input("Max", value=5.0, step=0.5)
        
        # Add generate button in the right column
        st.markdown("###")  # Add some spacing
        if st.button("Generate Combined Visualization", use_container_width=True):
            return func1_name, func2_name, expression1, expression2, (x_min, x_max), True
    
    return func1_name, func2_name, expression1, expression2, (x_min, x_max), False

def display_visualization(
    func1_name: str, 
    func2_name: str, 
    expression1: str,
    expression2: str,
    x_range: tuple
):
    """Generate and display the visualization."""
    # Use columns for layout
    viz_col, analysis_col = st.columns([3, 1])
    
    with viz_col:
        with st.spinner("Generating visualization..."):
            try:
                # Get Gemini's analysis
                response = st.session_state.gemini.generate_combination_analysis(
                    expression1,
                    expression2
                )
                
                # Parse response
                parsed = MathVisualizer.parse_gemini_response(response)
                
                # Create visualization
                fig = MathVisualizer.create_visualization(
                    expression1,
                    expression2,
                    parsed['expression'],
                    x_range=x_range
                )
                st.plotly_chart(fig, use_container_width=True)
                
            except Exception as e:
                st.error(f"Error generating visualization: {str(e)}")
                error_fig = MathVisualizer.create_error_plot(str(e))
                st.plotly_chart(error_fig, use_container_width=True)
    
    with analysis_col:
        st.markdown("### Gemini's Analysis")
        st.markdown(parsed['raw_response'])

def main():
    st.markdown("""
        <h1 style='text-align: center; margin-bottom: 0;'>Mathematical Function Combiner & Visualizer</h1>
        <p style='text-align: center; color: #666; margin-bottom: 2rem;'>Combine and visualize mathematical functions with interactive parameters</p>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    init_session_state()
    
    # Render function selection interface
    results = render_function_selection()
    if results[-1]:  # If generate button was clicked
        func1_name, func2_name, expr1, expr2, x_range, _ = results
        display_visualization(func1_name, func2_name, expr1, expr2, x_range)

if __name__ == "__main__":
    main()