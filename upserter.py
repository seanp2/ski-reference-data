import csv
import sys
import mysql.connector


_, USERNAME, PASSWORD, HOST, DATABASE, FIS_LIST_FILE = sys.argv


def upsert():
    with mysql.connector.connect(user=USERNAME, password=PASSWORD,
                                  host=HOST,
                                  database=DATABASE) as cnx:
        with cnx.cursor() as cursor:
            input_file = csv.DictReader(open(FIS_LIST_FILE))
            athlete_insert_tuples = []
            ranking_insert_tuples = []
            for row in input_file:
                athlete_tuple = f"({row['Fiscode']}, '{row['Lastname']}', '{row['Firstname']}', '{row['Gender']}', '{row['Birthdate']}', '{row['Skiclub']}', '{row['Nationcode']}')"
                ranking_tuple = f"""({row['Fiscode']},{row['Listid']},{row['Published']},'{row['Sectorcode']}', 
                                    '{row['Status']}',{row['Competitorid']},'{row['DHpoints']}','{row['DHpos']}',
                                    '{row['SGpoints']}','{row['SGpos']}','{row['GSpoints']}','{row['GSpos']}',
                                    '{row['SLpoints']}','{row['SLpos']}','{row['DHSta']}','{row['SGSta']}',
                                    '{row['GSSta']}','{row['SLSta']}')"""
                athlete_insert_tuples.append(athlete_tuple)
                ranking_insert_tuples.append(ranking_tuple)
            insert_new_athlete_query = f"""
                INSERT IGNORE INTO FIS_database.Athlete (`Fiscode`,`Lastname`,`Firstname`,`Gender`, `Birthdate`,`Skiclub`,`NationalCode`)
                VALUES
                {",".join(athlete_insert_tuples)}
            """
            insert_new_ranking_query = f"""
                            INSERT IGNORE INTO FIS_database.Ranking 
                                (`Fiscode`,`Listid`,`Published`,`SectorCode`, `Status`,`CompetitorID`,`DHpoints`,`DHpos`,`SGpoints`,`SGpos`,
                                    `GSpoints`,`GSpos`,`SLpoints`,`SLpos`,`DHSta`,`SGSta`,`GSSta`,`SLSta`) VALUES 
                            {",".join(ranking_insert_tuples)}   
                        """
            cursor.execute(insert_new_athlete_query)
            print("New athletes inserted = {}".format(cursor.rowcount))
            cursor.execute(insert_new_ranking_query)
            print("New rankings inserted = {}".format(cursor.rowcount))
        cnx.commit()

upsert()
