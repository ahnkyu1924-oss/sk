import json
from pathlib import Path
def fm(x):return "N/A" if x is None else f"{x/1e12:,.2f}조"
def fp(x):return "N/A" if x is None else f"{x:,.1f}%"
def build(rs,name,out):
    x=rs[-1] if rs else {}
    rows="".join(f"<tr><td>{r['year']}</td><td>{fp(r.get('revenue_growth_pct'))}</td><td>{fp(r.get('operating_margin_pct'))}</td><td>{fp(r.get('net_margin_pct'))}</td><td>{fp(r.get('roe_pct'))}</td><td>{fp(r.get('roa_pct'))}</td><td>{fp(r.get('debt_ratio_pct'))}</td></tr>" for r in rs)
    labs=json.dumps([str(r["year"]) for r in rs],ensure_ascii=False)
    rev=json.dumps([r.get("revenue") for r in rs])
    op=json.dumps([r.get("operating_income") for r in rs])
    h=f"""<!doctype html><html lang=ko><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>{name} DART Dashboard</title><script src="https://cdn.jsdelivr.net/npm/chart.js"></script><style>body{{font-family:system-ui;background:#f5f7fb;color:#172033}}main{{max-width:1100px;margin:auto;padding:28px}}.g{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px}}.c{{background:white;padding:18px;border-radius:15px;margin:12px 0}}.b{{font-size:25px;font-weight:700}}table{{width:100%;border-collapse:collapse}}td,th{{padding:9px;border-bottom:1px solid #ddd;text-align:right}}td:first-child,th:first-child{{text-align:left}}</style></head><body><main><h1>{name} 재무 Dashboard</h1><p>OpenDART 연결재무제표 · 3~5년 추세</p><div class=g><div class=c>매출액<div class=b>{fm(x.get('revenue'))}</div></div><div class=c>영업이익률<div class=b>{fp(x.get('operating_margin_pct'))}</div></div><div class=c>ROE<div class=b>{fp(x.get('roe_pct'))}</div></div><div class=c>부채비율<div class=b>{fp(x.get('debt_ratio_pct'))}</div></div></div><div class=c><canvas id=t></canvas></div><div class=c><table><tr><th>연도</th><th>매출증가율</th><th>영업이익률</th><th>순이익률</th><th>ROE</th><th>ROA</th><th>부채비율</th></tr>{rows}</table></div><div class=c><b>주의</b><p>ROA·ROE는 전기·당기 평균 잔액을 사용할 수 있을 때 계산합니다. CAPEX·FCF·EBITDA·순차입금·ROIC·CCC·시장가치 지표는 필요한 계정/주석/시장가격이 확보되지 않으면 임의 추정하지 않습니다.</p></div><script>new Chart(t,{{type:'line',data:{{labels:{labs},datasets:[{{label:'매출액',data:{rev}}},{{label:'영업이익',data:{op}}}]}}}});</script></main></body></html>"""
    Path(out).write_text(h,encoding="utf-8")
