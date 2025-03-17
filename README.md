# Ikorodu Scholarship GPT

This repository contains a fine-tuned GPT model designed specifically to answer questions related to **Ikorodu scholarships**. The model is built using OpenAI's API and is fine-tuned to provide accurate, relevant, and up-to-date responses on available scholarships, eligibility, and application processes for students in Ikorodu.

## Features
- **Focused Knowledge:** The model is trained to answer only **Ikorodu scholarship** queries.
- **Fast and Reliable:** Leveraging OpenAI's API ensures accurate and quick responses.
- **Customizable:** Can be further fine-tuned or integrated into applications for expanded use cases.

## Setup

### Prerequisites
Before running the project, ensure you have the following:
- Python 3.7+
- An OpenAI API key
- Required dependencies (listed in `requirements.txt`)

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ikorodu-scholarship-gpt-finetuning.git
   cd ikorodu-scholarship-gpt
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key:**
   Create a `.env` file in the root directory and add your API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the model:**
   ```bash
   python main.py
   ```

## Usage
- Send scholarship-related queries to the model via API calls.
- The model responds with information specifically related to **Ikorodu scholarships**.

## Example Query
```python
from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="your-finetuned-model-id",
    messages=[{"role": "user", "content": "What scholarships are available in Ikorodu?"}]
)

print(response["choices"][0]["message"]["content"])
```

## Contribution
If you’d like to contribute:
1. Fork the repository
2. Create a new branch (`feature-branch`)
3. Commit your changes
4. Open a pull request

## License
This project is licensed under the MIT License.

## Contact
For issues or inquiries, reach out to **[tiletiletoheebatyewande@outlook.com]**.

