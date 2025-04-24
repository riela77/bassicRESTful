# 요즘 웹사이트는 DB관련 작업은 back-end에서 다하고 보내준 결과만  front에서 관리하는 
from tkinter.tix import Control
from fastapi import FastAPI
from fastapi.responses import Response
from fastapi.responses import JSONResponse

app = FastAPI()
# 서버 호출에 따라 xml파일을 출력하는 
@app.get("/xml.test")
def xmlTest():
    xmll=""
    xmll+="<snacks>"
    xmll+="<snack><s_name>빼빼로</s_name><s_price>2000</s_price></snack>"
    xmll+="<snack><s_name>새우깡</s_name><s_price>1000</s_price></snack>"
    xmll+="<snack><s_name>초코칩</s_name><s_price>2500</s_price></snack>"
    xmll+="</snacks>"

    return Response(content=xmll,media_type="application/xml")

# 서버 호출에 따라 json파일을 출력하는
@app.get("/json.test")
def jsonTest():
    jsonn=[
        {"s_name":"빼빼로","s_price":2000},
        {"s_name":"새우깡","s_price":1000}
    ]
    # 외부에서도 결과를 확인할수있게 하려면
    # Access-Control-Allow-Origin이라는 헤더를 세팅해야된다. 
    h={"Access-Control-Allow-Origin":"*"}
    return JSONResponse(content=jsonn ,headers=h)

if __name__ == "__main__":
    app.run(debug=True)