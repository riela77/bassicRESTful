from DBconnectLibrary.kimDBmanager import kimDBmanager


class ProductDAO:
    def getAll(self):
        try:
            con,cur=kimDBmanager.makeConCur("KIMCR/1@195.168.9.126:1521/xe")
            sql="SELECT * FROM apr23_product"
            cur.execute(sql)
            products=[]
            for n,p in cur:
                s={"name":n,"price":p}
                products.append(s)
            return products
        except Exception as e:
            print(e)
        finally:
            kimDBmanager.closeConCur(con,cur)

    def reg(self,n,p):
        try:
            con,cur=kimDBmanager.makeConCur("KIMCR/1@195.168.9.126:1521/xe")
            sql="INSERT INTO apr23_product values('%s',%s)"%(n,p)
            cur.execute(sql)
            
            if cur.rowcount==1:
                con.commit()
                return {"result":n+"등록성공"}
            return {"result":n+"등록실패"}
        except Exception as e:
            print(e)
            return {"result":n+"등록실패"}
        finally:
            kimDBmanager.closeConCur(con,cur)

    def proDel(self,minn,maxx):
        try:
            con,cur=kimDBmanager.makeConCur("KIMCR/1@195.168.9.126:1521/xe")
            sql="delete from apr23_product where p_price > %s and p_price < %s"%(minn,maxx)
            cur.execute(sql)
            
            if cur.rowcount>=1:
                con.commit()
                return {"result":"삭제 성공"}
            return {"result":"삭제 실패"}
        except Exception as e:
            print(e)
            return {"result":"앙삭제 실패"}
        finally:
            kimDBmanager.closeConCur(con,cur)
