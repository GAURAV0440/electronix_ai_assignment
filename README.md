# Electronix AI Project 🤖
Simple sentiment analysis API - tells if text is positive or negative.

## 🎥 Demo Video
**Watch the project in action:** [Project Demo on Loom](https://www.loom.com/share/0602c99788fe4d3698c1a81158eaccf7?sid=c8b048c1-9338-4241-b6cf-982ccdcdc737)

## 📁 Complete Project Structure
```
ELECTRONIX-AI-PROJECT/
├── backend/
│   ├── __pycache__/
│   ├── model/              # Trained AI models
│   ├── venv310/           # Python virtual environment
│   ├── app.py             # Main API server
│   └── requirements.txt   # Python packages
├── frontend/
│   ├── build/             # Production build
│   ├── node_modules/      # NPM packages
│   ├── public/
│   │   ├── favicon.ico
│   │   ├── index.html
│   │   ├── logo192.png
│   │   └── logo512.png
│   ├── src/
│   │   ├── App.css
│   │   ├── App.js         # Main React component
│   │   ├── index.js
│   │   └── logo.svg
│   ├── package.json       # Frontend dependencies
│   └── package-lock.json
├── results/               # Training results
├── .gitignore
├── data.jsonl            # Sample training data
├── finetune.py           # Train custom models
└── README.md             # This file
```
## 🚀 What This Does
- Analyzes text sentiment (positive/negative)
- Trains custom AI models on your data
- REST API for easy integration

## Quick Setup

**1. Clone & Install**
```bash
git clone https://github.com/GAURAV0440/electronix_ai_assignment.git
cd electronix_ai_assignment

# Backend setup
cd backend
python -m venv venv310
.\venv310\Scripts\Activate
pip install -r requirements.txt

# Frontend setup  
cd ../frontend
npm install
```

**2. Run Both**
```bash
# Backend (in backend/ folder)
cd backend
.\venv310\Scripts\Activate
uvicorn app:app --reload --port 8000

# Frontend (in frontend/ folder)
cd frontend
npm start
```

Visit: `http://localhost:8000/docs` (API) | `http://localhost:3000` (Frontend)

## 🧪 Test API
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "I love this work or anything."}'
# Returns: {"label": "positive", "score": xxxxxxx}
```
## 🔧 Train Model
```bash
python finetune.py --data data.jsonl --epochs 3
```

**Label Mapping (automatically generated):**
```
{'negative': 0, 'positive': 1}
```
*The model assigns numerical labels during training and shows this mapping in the console.*
## 🤝 Contributing to This Project
1. Fork repository → Clone your fork
2. Create feature branch → `git checkout -b feature-name`
3. Implement changes in `backend/` or `frontend/` directories
4. Test thoroughly → Backend: `uvicorn app:app --reload` | Frontend: `npm start`
5. Submit Pull Request with clear description

## Requirements
**Backend:** transformers, torch, fastapi, uvicorn, pydantic, datasets, scikit-learn, accelerate
**Frontend:** react, react-dom, axios, react-scripts

## Common Issues
- **Backend won't start?** → Check you're in `backend/` folder, activate venv
- **Frontend won't start?** → Check you're in `frontend/` folder, run `npm install`
- **Training fails?** → Check data format matches `data.jsonl`
