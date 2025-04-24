import fastapi
from fastapi.responses import JSONResponse
from product.productDAO import ProductDAO


app=fastapi.FastAPI()
pDAO=ProductDAO()

# DB데이터 불러오는 역할
@app.get("/product.get")
def productGet():
    resBody=pDAO.getAll()
    resHeader={"Access-Control-Allow-Origin":"*"} 
    return JSONResponse(resBody,headers=resHeader)

# get 방식으로 DB데이터 등록하는 역할
# /product.reg?namee=볼펜&pricee=500
@app.get("/product.reg")
def productReg(namee,pricee):
    resBody=pDAO.reg(namee,pricee)
    resHeader={"Access-Control-Allow-Origin":"*"} 
    return JSONResponse(resBody,headers=resHeader)

# 가격범위에 따라 데이터를 삭제하는 역할
# /product.del?minn=10&maxx=500
@app.get("/product.del")
def productDel(minn,maxx):
    resBody=pDAO.proDel(minn,maxx)
    resHeader={"Access-Control-Allow-Origin":"*"} 
    return JSONResponse(resBody,headers=resHeader)
    
