from database.DB_connect import DBConnect
from model.border import Border
from model.country import Country


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getNodes(anno):

        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result=[]
        query="""select distinct  c.*
                from country c , contiguity c2 
                where c.CCode = c2.state1no 
                or c.CCode = c2.state2no 
                and c2.`year` <= %s
                """

        cursor.execute(query,(anno,))

        for row in cursor:
            result.append(Country(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges(anno):

        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []
        query = """select LEAST( c.state1no , c.state2no ) as stato1, GREATEST(c.state1no,c.state2no) as stato2, c.year
                    from contiguity c 
                    where c.`year` <= %s
                    and c.conttype = 1
                    group by LEAST( c.state1no , c.state2no ) , GREATEST(c.state1no, c.state2no), c.year
                """

        cursor.execute(query,(anno,))

        for row in cursor:
            result.append(Border(**row))

        cursor.close()
        conn.close()
        return result
