# AgriPriceRisk_Proposed

## Setup Instructions (Windows PowerShell)
```powershell
cd Desktop
python -m venv agri_env
agri_env\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
```
Then open http://127.0.0.1:8000/docs to test API.

For dashboard UI:
```powershell
streamlit run dashboard.py
```
