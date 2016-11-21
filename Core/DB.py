import MySQLdb as mysql


class DB:
    def __init__(self):
        self.connection = mysql.connect(user="root", passwd="root", db="cmpe138_project_team3_feedback")

    def close(self):
        """close connection"""
        self.connection.close()

    def query(self, table, paramsJson=None):
        """Will execute the query and return rows as a list of objects.
        Return empty list in case of No results"""
        pass

    def insert_feedback_record(self, tablename, values):
        cursor = self.connection.cursor()
        if tablename == "product":
            cursor.execute(
                "INSERT INTO product_feedback(ratings,customer_id,product_id,comments,franchise_id)VALUES (%s,%s,%s,%s,%s)",
                values)
        else:
            cursor.execute(
                "INSERT INTO service_feedback(ratings,customer_id,service_id,comments,franchise_id)VALUES (%s,%s,%s,%s,%s)",
                values)
        self.connection.commit()
        self.close()

    def update_record(self):
        pass

    # TODO add query to check if product id is available for particular franchise record
    def check_product_record(self, check_id, franchise_id):
        return True

    def check_franchise_exists(self, franchise_id):
        return True

    def check_service_exists(self, service_id):
        return True

    def insert_action_item(self, values, feedback_type):
        cursor = self.connection.cursor()
        item_type = ""
        if feedback_type == "product":
            item_type = "product_feedback_id"
        else:
            item_type = "service_feedback_id"

        cursor.execute(
            "INSERT INTO action_items(start_date,end_date,created_by,assigned_to,comments," + item_type + ")VALUES(%s,%s,%s,%s,%s,%s)"
            , values)

        self.connection.commit()
        self.close()

    def update_action_item(self):
        return True