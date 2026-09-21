import requests
BASE="https://opendart.fss.or.kr/api"
class DartError(RuntimeError): pass
class DartClient:
    def __init__(self,key):
        if not key or key.startswith("PUT_"): raise DartError("DART_API_KEY가 설정되지 않았습니다.")
        self.key=key
    def get(self,ep,**p):
        p["crtfc_key"]=self.key
        r=requests.get(f"{BASE}/{ep}",params=p,timeout=30); r.raise_for_status(); d=r.json()
        if d.get("status") and d["status"]!="000": raise DartError(f"{d.get('status')}: {d.get('message')}")
        return d
    def company(self,c): return self.get("company.json",corp_code=c)
    def filings(self,c,b,e): return self.get("list.json",corp_code=c,bgn_de=b,end_de=e,pblntf_ty="A",page_count=100)
    def statements(self,c,y,fs="CFS"): return self.get("fnlttSinglAcntAll.json",corp_code=c,bsns_year=str(y),reprt_code="11011",fs_div=fs)
