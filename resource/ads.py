import os
import logging
import pandas as pd
from flask import request
from flask_restful import Resource
from models import config

file_name = os.path.basename(__file__)


class AdsInsert(Resource):
    def post(self):
        conn = False
        try:
            logging.info(f'filename:{file_name}-class:{self.__class__}')
            conn = config.get_ebuy_db_conn()
            if 'False' in str(conn):
                return {"res_status": False, "msg": "Database Connection Failed"}
            request_data = request.get_json()

            query_1 = f"INSERT INTO ads_details (base_url, socket_url, google_native_ad_id_android, " \
                      f"google_native_ad_id_ios) " \
                      f"VALUES ('{request_data['base_url']}', '{request_data['socket_url']}', " \
                      f"'{request_data['google_native_ad_id_android']}', '{request_data['google_native_ad_id_ios']}')"
            cur = conn.cursor()
            cur.execute(query_1)
            conn.commit()
            cur.close()
            return {"res_status": True, "status": 200, "msg": "Data Inserted Successfully"}

        except Exception as e:
            logging.error("Error occurred while inserting item: " + str(e)
                          + "/n...........................................")
            return {"res_status": False, "msg": "Failed to add item", "error": str(e)}
        finally:
            if str(conn) != 'False':
                conn.close()


class AdsList(Resource):
    def post(self):
        conn = False
        try:
            conn = config.get_ebuy_db_conn()
            if 'False' in str(conn):
                return {"res_status": False, "msg": "Database Connection Failed"}
            logging.info(f'Retrieving ads details data')

            profile_details = f"select * from ads_details "

            row = pd.read_sql(profile_details, conn)
            logging.info('.../n fetching records from ads table../n')
            if row.empty:
                return {"res_status": False, "msg": 'No records found'}

            result = row.to_dict(orient="records")

            logging.info(f'Retrieved ads details data successfully')
            return {"res_status": True, "status": 200, "data": result}

        except Exception as e:
            logging.error("Error occurred in ads list class: " + str(e)
                          + "/n...........................................")
            return {"res_status": False, "msg": str(e)}
        finally:
            if str(conn) != 'False':
                conn.close()


class AdsUpdate(Resource):
    def post(self):
        conn = False
        try:
            conn = config.get_ebuy_db_conn()
            if 'False' in str(conn):
                return {"res_status": False, "msg": "Database Connection Failed"}
            cur = conn.cursor()
            logging.info('../n establishing connection../n')
            request_data = request.get_json()
            base_url = request_data['base_url']
            socket_url = request_data['socket_url']
            google_native_ad_id_android = request_data['google_native_ad_id_android']
            google_native_ad_id_ios = request_data['google_native_ad_id_ios']
            ad_id = request_data['ad_id']
            if ad_id == '':
                return {"res_status": False, "msg": 'Enter wallet_id'}

            logging.info('..../n enter mandatory fields.../n')

            cur.execute(f"update ads_details set base_url = '{base_url}', "
                        f"socket_url = '{socket_url}', "
                        f"google_native_ad_id_android = '{google_native_ad_id_android}',"
                        f"google_native_ad_id_ios = '{google_native_ad_id_ios}' "
                        f" where ad_id = {ad_id} ")
            conn.commit()
            return {"res_status": True, "status": 200, "msg": "Data Updated Successfully"}

        except Exception as e:
            logging.error("Error occurred while retrieving data details update data: " + str(e)
                          + "/n...........................................")
            return {"res_status": False, "msg": str(e)}
        finally:
            if str(conn) != 'False':
                conn.close()


