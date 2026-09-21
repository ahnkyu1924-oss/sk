def num(v):
    if v is None:return None
    s=str(v).strip().replace(",","")
    if s in ("","-"):return None
    neg=s.startswith("(") and s.endswith(")"); s=s.strip("()")
    try:return -float(s) if neg else float(s)
    except:return None
def pick(rows,names):
    for n in names:
        for r in rows:
            if str(r.get("account_nm","")).strip()==n:
                v=num(r.get("thstrm_amount"))
                if v is not None:return v
    for n in names:
        for r in rows:
            if n in str(r.get("account_nm","")):
                v=num(r.get("thstrm_amount"))
                if v is not None:return v
    return None
def div(a,b): return None if a is None or b in (None,0) else a/b
def analyze(yr,cfg):
    out=[]
    for y in sorted(yr):
        d={"year":y}
        for k,n in cfg["metrics"].items():d[k]=pick(yr[y],n)
        out.append(d)
    for i,d in enumerate(out):
        p=out[i-1] if i else None
        aa=(d["assets"]+p["assets"])/2 if p and d.get("assets") is not None and p.get("assets") is not None else None
        ae=(d["equity"]+p["equity"])/2 if p and d.get("equity") is not None and p.get("equity") is not None else None
        d["revenue_growth_pct"]=(div(d.get("revenue"),p.get("revenue"))-1)*100 if p and div(d.get("revenue"),p.get("revenue")) is not None else None
        for k,a,b in [("gross_margin_pct","gross_profit","revenue"),("operating_margin_pct","operating_income","revenue"),("net_margin_pct","net_income","revenue"),("current_ratio_pct","current_assets","current_liabilities"),("debt_ratio_pct","liabilities","equity"),("equity_ratio_pct","equity","assets")]:
            q=div(d.get(a),d.get(b)); d[k]=q*100 if q is not None else None
        q=div(d.get("net_income"),aa);d["roa_pct"]=q*100 if q is not None else None
        q=div(d.get("net_income"),ae);d["roe_pct"]=q*100 if q is not None else None
        d["asset_turnover"]=div(d.get("revenue"),aa)
        d["cfo_to_net_income"]=div(d.get("cfo"),d.get("net_income"))
    return out
