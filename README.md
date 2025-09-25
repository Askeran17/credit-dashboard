# Credit Dashboard

A full‑stack app to manage credit institutions and their loan portfolios. The backend is a FastAPI service with MongoDB, and the frontend is a Vue 3 + Vite app.

## Features
- Create and list credit institutions
- Upload CSV files with loans for an institution
- Auto‑update loan status when due date expires
- Per‑institution dashboard with totals and status breakdown
- Global dashboard across all institutions

## Tech Stack
- Backend: FastAPI, Pydantic v2, Uvicorn, MongoDB (PyMongo)
- Frontend: Vue 3, Vue Router, Vite, Axios.
- CSV parsing: Pandas

## Prerequisites
- Python 3.9+
- Node.js 20+
- MongoDB (Atlas or local). The app expects a connection string in `.env`.

## Setup

### 1) Clone and install
```bash
# Clone
git clone <your-repo-url> credit-dashboard
cd credit-dashboard

# Backend: create venv and install
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Frontend: install deps
cd ../frontend
npm install
```

### 2) Configure environment
Create a file named `.env` in the project root (same level as `backend/` and `frontend/`):

```env
# .env (project root)
MONGO_URI=mongodb+srv://<user>:<password>@<cluster>/<db>?retryWrites=true&w=majority
ENV=development
```

Notes:
- `MONGO_URI` is required. You can also use a local MongoDB URI, e.g. `mongodb://localhost:27017`.
- When `ENV=development`, CORS is allowed for `http://localhost:5173` (Vite dev server).

## Running (development)

### Backend
```bash
cd backend
source .venv/bin/activate
uvicorn main:app --reload
```
Defaults:
- API base: `http://localhost:8000`
- After you build the frontend, FastAPI will also serve the SPA from `frontend/dist`.

### Frontend
```bash
cd frontend
npm run dev
```
Defaults:
- Dev server: `http://localhost:5173`
- Axios base URL is set in `src/main.js` to `http://localhost:8000`.

## Build and Serve (production‑like)
- Build SPA:
```bash
cd frontend
npm run build
```
- Start backend (it will serve `frontend/dist` at `/`):
```bash
cd backend
source .venv/bin/activate
uvicorn main:app --reload
```
Open `http://localhost:8000` in your browser.

## How to Use
1) Create an institution
- Go to `/` (Create). Fill the form and click `Create`.
- You will see the created ID and can copy it or click `Go to dashboard`.

2) Upload loans for an institution
- Go to `Upload CSV`.
- Select a CSV file and paste the Institution ID.
- Click `Upload`.

3) View dashboards
- `Dashboard` shows aggregated loans across all institutions and lets you click an institution name to open its dashboard.
- `Dashboard /:id` shows totals and loan table for the selected institution.

## API Endpoints (summary)
- `POST /institutions` → create an institution. Returns `{ id: string }`.
- `GET /institutions` → list institutions. Each document includes stringified `_id`.
- `DELETE /institutions/{id}` → delete an institution and its loans.
- `POST /loans/import/{institution_id}` (multipart file) → import CSV loans.
- `GET /dashboard/{institution_id}` → get totals and loans for one institution.
- `GET /loans/{institution_id}` → list loans for one institution.

## CSV Format
The CSV parser expects columns similar to:
- `loan_no`, `principal_open_eur`, `loan_last_date`, `status` (derived), etc.

The `utils/csv_parser.py` uses Pandas to parse the uploaded file and attaches `institution_id` to each row. Expired loans are marked automatically when the due date passes.

## License
MIT
