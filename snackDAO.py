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
            print(n,p)
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
