# mathviz-gemini
# Mathematical Function Visualizer

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-API-4285F4?style=flat&logo=google&logoColor=white)

An interactive web application that combines and visualizes mathematical functions using Google's Gemini Pro API. Users can select different mathematical functions, adjust their parameters, and visualize their combinations in both 2D and 3D representations.

![Application Screenshot](screenshots/app_preview.png)

## Features

- 🔄 Interactive function combination and visualization
- 📊 Real-time 2D and 3D plotting
- 🤖 AI-powered function analysis using Google Gemini
- ⚙️ Adjustable function parameters
- 📐 Customizable plot ranges
- 📝 Detailed mathematical analysis of combined functions

## Demo

[Add a GIF or link to live demo if available]

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mathematical-function-visualizer.git
cd mathematical-function-visualizer
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Google API key:
```env
GOOGLE_API_KEY=your_api_key_here
```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Select functions and adjust parameters:
   - Choose from available mathematical functions
   - Adjust function parameters
   - Set x-axis range
   - Click "Generate Combined Visualization"

## Project Structure

```
mathematical-function-visualizer/
├── app.py                 # Main Streamlit application
├── config.py             # Configuration and function definitions
├── gemini_adapter.py     # Google Gemini API integration
├── visualizer.py         # Visualization logic
├── requirements.txt      # Project dependencies
├── .env                  # API key configuration (not included in repo)
└── README.md            # Project documentation
```

## Dependencies

- Python 3.8+
- Streamlit
- NumPy
- Plotly
- Google Generative AI
- python-dotenv
- matplotlib

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Google Gemini API for function analysis
- Streamlit for the web interface
- Plotly for interactive visualizations

## Contact
![image](https://github.com/user-attachments/assets/2c5b702d-d641-49b5-ad3f-3af0c782406d)

Your Name - [@yourusername](https://twitter.com/yourusername)

Project Link: [https://github.com/yourusername/mathematical-function-visualizer](https://github.com/yourusername/mathematical-function-visualizer)
