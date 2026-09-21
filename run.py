import os,json,yaml
from pathlib import Path
from datetime import date,timedelta
from dotenv import load_dotenv
from src.dart_client import DartClient
from src.analysis import analyze
from src.dashboard import build
load_dotenv();R=Path(__file__).parent
c=yaml.safe_load((R/"config/company.yaml").read_text(encoding="utf-8"));m=yaml.safe_load((R/"config/metrics.yaml").read_text(encoding="utf-8"))
d=DartClient(os.getenv("DART_API_KEY"));corp=c["corp_code"]
(R/"data/raw/company.json").write_text(json.dumps(d.company(corp),ensure_ascii=False,indent=2),encoding="utf-8")
now=date.today();f=d.filings(corp,(now-timedelta(days=400)).strftime("%Y%m%d"),now.strftime("%Y%m%d"))
(R/"data/raw/filings_latest.json").write_text(json.dumps(f,ensure_ascii=False,indent=2),encoding="utf-8")
ys={};end=now.year-1
for y in range(end-int(c["years_back"]),end+1):
    try:
        q=d.statements(corp,y,c["fs_div"]);(R/f"data/raw/financial_{y}.json").write_text(json.dumps(q,ensure_ascii=False,indent=2),encoding="utf-8")
        if q.get("list"):ys[y]=q["list"]
    except Exception as e:print("[WARN]",y,e)
a=analyze(ys,m);(R/"data/processed/financial_analysis.json").write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding="utf-8")
build(a,c["company_name"],R/"docs/index.html");(R/"docs/.nojekyll").write_text("");print("완료",len(a))
