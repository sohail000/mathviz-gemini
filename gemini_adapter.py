# gemini_adapter.py
import google.generativeai as genai
from typing import Optional
from config import GeminiConfig, COMBINATION_ANALYSIS_PROMPT

class GeminiAdapter:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = None
        self.current_config = None
        
    def setup_model(self, config: Optional[GeminiConfig] = None):
        if config is None:
            config = GeminiConfig()
            
        self.current_config = config
        generation_config = genai.types.GenerationConfig(
            temperature=config.temperature,
            max_output_tokens=config.max_output_tokens,
            top_p=config.top_p,
            top_k=config.top_k
        )
        
        self.model = genai.GenerativeModel(
            'gemini-pro',
            generation_config=generation_config
        )

    def generate_combination_analysis(self, func1: str, func2: str) -> str:
        if self.model is None:
            self.setup_model()
            
        prompt = COMBINATION_ANALYSIS_PROMPT.format(func1=func1, func2=func2)
        response = self.model.generate_content(prompt)
        return response.text

    def get_current_temperature(self) -> float:
        return self.current_config.temperature if self.current_config else 0.7
    
    def get_current_max_tokens(self) -> int:
        return self.current_config.max_output_tokens if self.current_config else 100