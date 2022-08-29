import sys, os
import getpass
import pandas as pd
from math import sqrt
import geopandas as gpd  
from zipfile import ZipFile  
import glob  
import psycopg2  
from convertHex import calculateAverage

#  Python 3 compat
if sys.version_info[0] >= 3:
    raw_input = input

# to access the Spatial PostgreSQL database
user = "postgres"  # raw_input("Database username:")
passwd = "****"  # getpass.getpass("Password for " + user + ":")
database_name = "tp1_ai"  # raw_input("Database name:")

# assuming there is a spatial table Landuse (imported from a shapefile available at
connection_str = 'postgresql://' + user + ':' + passwd + '@localhost:5432/' + database_name

dir_src = './'
filenames = os.listdir(dir_src)

# another directory smc_processed is created/used to store a flag for each session
# imported to the spatial database
if not os.path.exists(dir_src + "_processed"):
    os.makedirs(dir_src + "_processed")

for file in filenames:
    # print(file)
    if os.path.isfile(dir_src + "/" + file):
        with open(dir_src + "/" + file) as current_file:
            if file.endswith(".zip"):
                tokens = file.split("_")
                session = tokens[1]
                activity = tokens[2]
                user_id = tokens[3].lower().split(".")[0].replace("user", "")

                # only dealing with Location sensor file in each SenseMyCity session
                acc_file = glob.glob("./**/SenseMyCity-" + session + "-magnetometer.csv", recursive=True)
                if len(acc_file) == 0:
                    with ZipFile(dir_src + "/" + file, 'r') as zip_ref:
                        zip_ref.extractall()
                        acc_file = glob.glob("./**/SenseMyCity-" + session + "-magnetometer.csv", recursive=True)

                if len(acc_file) > 0:
                    basename = acc_file[0].split("/")
                    basename_file = basename[len(basename) - 1]
                    if not os.path.exists(dir_src + "_processed/" + basename_file):

                        recolhas_magnetometer = []
                        # with open(dir_src+"_processed/"+basename_file,"w") as flag_file:
                        #    flag_file.write("inserted " + str(len(recolhas_list)) + " points" )

                        with open(acc_file[0]) as current_csv_file:
                            for line in current_csv_file:
                                values = line.split(";")
                                if len(values) > 4 and values[0].isnumeric():
                                    recolhas_magnetometer.append((values[1], values[2], values[3], values[4]))
                        if len(recolhas_magnetometer) > 0:
                            mag_out = []
                            for i in range(len(recolhas_magnetometer)):
                                dec_magx = calculateAverage(recolhas_magnetometer[i][1].replace('\\', '0').replace('"', ''))
                                dec_magy = calculateAverage(recolhas_magnetometer[i][2].replace('\\', '0').replace('"', ''))
                                dec_magz = calculateAverage(recolhas_magnetometer[i][3].replace('\\', '0').replace('"', ''))
                                mag_out.append((recolhas_magnetometer[i][0], sqrt(dec_magx + dec_magy + dec_magz)))

                            if (len(mag_out) > 0):
                                #  insert multiple points into the recolhas table  """
                                sql = "INSERT INTO recolhas_magnetometer(id_recolha, actividade, id_user, instante, magnitude) VALUES (" + session + ",'" + activity + "'," + user_id + ",%s,%s)"
                                conn = None
                                try:
                                    #  connect to the PostgreSQL database
                                    conn = psycopg2.connect(dbname=database_name, user=user,
                                                            password=passwd)
                                    # create a new cursor
                                    cur = conn.cursor()
                                    #  execute the INSERT statement
                                    cur.executemany(sql, mag_out)
                                    #  commit the changes to the database
                                    conn.commit()
                                    #  close communication with the database
                                    cur.close()
                                except (Exception, psycopg2.DatabaseError) as error:
                                    print(error)
                                finally:
                                    if conn is not None:
                                        conn.close()
