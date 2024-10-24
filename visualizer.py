# visualizer.py
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import re
from typing import Dict, Tuple
from matplotlib.figure import Figure

class MathVisualizer:
    @staticmethod
    def parse_gemini_response(response: str) -> Dict:
        """Parse the structured response from Gemini."""
        expression_match = re.search(r'EXPRESSION:\s*(.*?)(?=DESCRIPTION:|$)', response, re.DOTALL)
        expression = expression_match.group(1).strip() if expression_match else "x"
        
        # Clean up the expression
        expression = expression.replace('```python', '').replace('```', '').strip()
        expression = expression.replace(' ', '').replace('*', '*')
        
        return {
            'expression': expression,
            'raw_response': response
        }

    @staticmethod
    def create_visualization(
        func1: str, 
        func2: str, 
        combined_expr: str,
        x_range: Tuple[float, float] = (-5, 5)
    ) -> Figure:
        """Create a comprehensive visualization of the functions."""
        x_min, x_max = x_range
        x = np.linspace(x_min, x_max, 1000)
        
        # Create the combined plot using plotly
        fig = make_subplots(
            rows=2, 
            cols=2, 
            subplot_titles=(
                'Function 1', 
                'Function 2', 
                'Combined Function', 
                'Combined 3D View'
            ),
            specs=[[{'type': 'xy'}, {'type': 'xy'}],
                  [{'type': 'xy'}, {'type': 'surface'}]],
            vertical_spacing=0.12,
            horizontal_spacing=0.1
        )
        
        try:
            # Evaluate functions
            y1 = eval(func1)
            y2 = eval(func2)
            y_combined = eval(combined_expr)
            
            # Add 2D plots
            fig.add_trace(
                go.Scatter(x=x, y=y1, name='Function 1'), 
                row=1, col=1
            )
            fig.add_trace(
                go.Scatter(x=x, y=y2, name='Function 2'), 
                row=1, col=2
            )
            fig.add_trace(
                go.Scatter(x=x, y=y_combined, name='Combined'), 
                row=2, col=1
            )
            
            # Add 3D visualization
            x_mesh = np.linspace(x_min, x_max, 100)
            y_mesh = np.linspace(x_min, x_max, 100)
            X, Y = np.meshgrid(x_mesh, y_mesh)
            Z = eval(combined_expr.replace('x', 'X'))
            
            fig.add_trace(
                go.Surface(x=x_mesh, y=y_mesh, z=Z, colorscale='Viridis', name='3D View'),
                row=2, col=2
            )
            
            # Update layout for more compact display
            fig.update_layout(
                height=600,  # Reduced height
                margin=dict(l=20, r=20, t=60, b=20),  # Reduced margins
                title_text="Mathematical Function Visualization",
                showlegend=True,
                scene=dict(
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Z'
                )
            )
            
            # Make subplots more compact
            fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')
            fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')
            
        except Exception as e:
            print(f"Error in visualization: {str(e)}")
            for i in range(1, 3):
                for j in range(1, 3):
                    fig.add_annotation(
                        text=f"Error: {str(e)}",
                        xref=f"x{i*j}",
                        yref=f"y{i*j}",
                        x=0.5,
                        y=0.5,
                        showarrow=False,
                        row=i,
                        col=j
                    )
        
        return fig

    @staticmethod
    def create_error_plot(error_message: str) -> Figure:
        """Create a simple error plot when visualization fails."""
        fig = go.Figure()
        fig.add_annotation(
            text=f"Error: {error_message}",
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False
        )
        return fig