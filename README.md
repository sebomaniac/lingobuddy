# LingoBuddy
 
## Table of Contents
- [Project Members](#project-members)
- [Project Description](#project-description)
- [Technology Stack](#technology-stack)
- [Setup Instructions](#setup-instructions)

## Project Members
Jeff Huang, Lorelei Tang, Hannah Kendall, Sebastian Johannessen

## Project Description
LingoBuddy is an AI-powered tool for learning new languages. It provides a platform for practicing language skills through interactive exercises, quizzes, and conversation simulations. The tool is designed to be user-friendly and accessible, suitable for learners of all levels.

## Technology Stack
#### Frontend
- React.js
- Next.js

#### Backend
- FastAPI
- Google Gemini API

#### Database
- Supabase

## Setup Instructions
*Make sure you have Python 3.12 or earlier installed*

1. Clone this GitHub repository
```
git clone https://github.com/sebomaniac/lingobuddy.git
```

2. In Visual Studio Code, change directory to lingobuddy
```
cd lingobuddy
```

3. Install dependencies
```
npm install
```

4. Add your keys for the database and Gemini API
```
// frontend/.env.local
NEXT_PUBLIC_SUPABASE_URL = 
NEXT_PUBLIC_SUPABASE_ANON_KEY = 
NEXT_PUBLIC_GEMINI_API_KEY =

// /backend/.env
GEMINI_API_KEY = 
```

6. Change directory to the backend directory
```
cd backend
```

6. Make virtual environment
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

7. Run backend
```
python -m uvicorn server:app --reload --host 0.0.0.0 --port 8000
```

8. Change directory to frontend
```
cd frontend
```

9. Install dependencies in frontend
```
npm install --force
```

10. Run frontend
```
npm run dev
```

11. Open the link in your browser
```
Cmd-Click --> http://localhost:3000/
```
