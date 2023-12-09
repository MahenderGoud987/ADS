import psycopg2
import logging

from read_properties import properties


def get_ebuy_db_conn():
    try:
        connection = psycopg2.connect(user=properties['db_user'], password=properties['db_password'],
                                      host=properties['db_host'], dbname=properties['db_database'])

        cursor = connection.cursor()
        return connection
    except Exception as e:
        logging.info(f"Error occurred while connection.....{str(e)}")
        return [{"Error": [{"res_status": False, "Message": str(e)}]}]