# config.py
from dataclasses import dataclass
from typing import List

@dataclass
class MathFunction:
    name: str
    expression_template: str  # Changed to template to allow parameter
    description: str
    compatible_functions: List[str]
    default_param: float = 1.0  # Default parameter value

@dataclass
class GeminiConfig:
    temperature: float = 0.7
    max_output_tokens: int = 2000
    top_p: float = 0.8
    top_k: int = 40

# Mathematical function definitions
MATH_FUNCTIONS = {
    'sine': MathFunction(
        name='Sine',
        expression_template='np.sin({param}*x)',
        description='Sinusoidal wave with adjustable frequency',
        compatible_functions=['cosine', 'polynomial'],
        default_param=1.0
    ),
    'cosine': MathFunction(
        name='Cosine',
        expression_template='np.cos({param}*x)',
        description='Cosine wave with adjustable frequency',
        compatible_functions=['sine', 'polynomial'],
        default_param=1.0
    ),
    'polynomial': MathFunction(
        name='Polynomial',
        expression_template='x**{param}',
        description='Power function with adjustable exponent',
        compatible_functions=['sine', 'cosine'],
        default_param=2.0
    )
}

# Gemini prompt templates
COMBINATION_ANALYSIS_PROMPT = """
Analyze the mathematical combination of these functions:
1. {func1}
2. {func2}

Provide:
1. A Python expression that combines these functions (use numpy as np). 
   IMPORTANT: Write the expression without spaces and use explicit multiplication operators (*).
2. A brief description of what happens when these functions are combined
3. Any interesting mathematical properties of the combination

Format your response as:
EXPRESSION: [your expression]
DESCRIPTION: [your description]
PROPERTIES: [properties]

Example of good expression format:
np.sin(2*x)*np.cos(x)  # No spaces, explicit multiplication
"""