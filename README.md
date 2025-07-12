# Electronix AI Project - Sentiment Analysis API

A machine learning project that provides sentiment analysis through a FastAPI backend. The project includes model fine-tuning capabilities and is designed for easy deployment and contribution.

## 📋 Project Overview

This project consists of:
- **Backend API**: FastAPI-based sentiment analysis service
- **Model Training**: Fine-tuning script for custom sentiment models
- **Sample Data**: Example training data in JSONL format
- **Frontend**: (Placeholder for future UI development)

## 🚀 Features

- **Sentiment Analysis API**: Real-time sentiment prediction with confidence scores
- **Custom Model Training**: Fine-tune DistilBERT on your own data
- **Flexible Model Loading**: Automatically uses fine-tuned model if available, falls back to pre-trained
- **Easy Deployment**: Simple setup with Python virtual environment

## 🛠️ Prerequisites

- Python 3.8+ (tested with Python 3.10)
- pip (Python package manager)
- Git

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/electronix-ai-project.git
cd electronix-ai-project
```

### 2. Set Up Python Environment
```bash
# Create virtual environment
python -m venv backend/venv310

# Activate virtual environment
# On Windows:
backend\venv310\Scripts\activate
# On macOS/Linux:
source backend/venv310/bin/activate
```

### 3. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

## 🚀 Quick Start

### Running the API Server

1. **Activate your virtual environment** (if not already active):
   ```bash
   # Windows
   backend\venv310\Scripts\activate
   # macOS/Linux
   source backend/venv310/bin/activate
   ```

2. **Start the server**:
   ```bash
   cd backend
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```

3. **Test the API**:
   - Open your browser and go to: `http://localhost:8000`
   - API documentation: `http://localhost:8000/docs`

### Making Predictions

Send a POST request to `/predict`:

```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "I love this product!"}'
```

Expected response:
```json
{
  "label": "positive",
  "score": 0.9998
}
```

## 🔧 Model Training

### Using Sample Data
```bash
# From project root directory
python finetune.py --data data.jsonl --epochs 3 --lr 3e-5
```

### Using Custom Data

1. **Prepare your data** in JSONL format:
   ```json
   {"text": "Your text here", "label": "positive"}
   {"text": "Another text", "label": "negative"}
   ```

2. **Train the model**:
   ```bash
   python finetune.py --data your_data.jsonl --epochs 5 --lr 2e-5
   ```

### Training Parameters
- `--data`: Path to your JSONL training file (required)
- `--epochs`: Number of training epochs (default: 3)
- `--lr`: Learning rate (default: 3e-5)

## 📁 Project Structure

```
electronix-ai-project/
├── README.md                 # This file
├── data.jsonl               # Sample training data
├── finetune.py              # Model training script
├── backend/
│   ├── app.py               # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   ├── model/               # Directory for fine-tuned models
│   └── venv310/             # Python virtual environment
└── frontend/                # Future frontend development
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Setup

1. **Fork the repository** on GitHub
2. **Clone your fork**:
   ```bash
   git clone https://github.com/your-username/electronix-ai-project.git
   cd electronix-ai-project
   ```
3. **Set up development environment** (follow installation steps above)
4. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

### Making Changes

1. **Backend changes**: Modify files in the `backend/` directory
2. **Model improvements**: Update `finetune.py` or add new training scripts
3. **Documentation**: Update this README or add inline documentation

### Testing Your Changes

1. **Test the API**:
   ```bash
   cd backend
   uvicorn app:app --reload
   # Test endpoints at http://localhost:8000/docs
   ```

2. **Test model training**:
   ```bash
   python finetune.py --data data.jsonl --epochs 1
   ```

### Submitting Changes

1. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add: description of your changes"
   ```

2. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create a Pull Request** on GitHub

## 📝 API Documentation

### Endpoints

#### `GET /`
- **Description**: Health check endpoint
- **Response**: `{"message": "Sentiment analysis API is running!"}`

#### `POST /predict`
- **Description**: Analyze sentiment of input text
- **Request Body**:
  ```json
  {
    "text": "string"
  }
  ```
- **Response**:
  ```json
  {
    "label": "positive|negative",
    "score": 0.0000
  }
  ```

## 🔧 Technical Details

- **Framework**: FastAPI with Uvicorn server
- **ML Library**: Hugging Face Transformers
- **Base Model**: DistilBERT (distilbert-base-uncased)
- **Model Format**: PyTorch
- **Data Format**: JSONL for training data

## 🐛 Troubleshooting

### Common Issues

1. **Virtual environment not activating**:
   - Ensure you're using the correct path
   - On Windows, try using PowerShell or Command Prompt

2. **Package installation fails**:
   - Upgrade pip: `python -m pip install --upgrade pip`
   - Try installing packages individually

3. **Model loading errors**:
   - Check if `backend/model/` directory exists and contains model files
   - The API will fall back to the default model if fine-tuned model is missing

4. **Memory issues during training**:
   - Reduce batch size in `finetune.py`
   - Use fewer epochs or smaller dataset

## 📄 License

This project is open source. Please add your preferred license here.

## 🙋‍♂️ Support

- **Issues**: Report bugs or request features via GitHub Issues
- **Documentation**: Check this README and API docs at `/docs` endpoint
- **Community**: Feel free to start discussions in GitHub Discussions

## 🔮 Future Enhancements

- [ ] Frontend web interface
- [ ] Support for multiple languages
- [ ] Model performance metrics dashboard
- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] Additional ML models (BERT, RoBERTa)
- [ ] Batch prediction endpoint
- [ ] Model versioning system

---

**Happy coding! 🚀**