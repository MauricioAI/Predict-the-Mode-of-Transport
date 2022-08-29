import sys, os
import getpass
import pandas as pd
from math import sqrt
import geopandas as gpd  
from zipfile import ZipFile  
import glob 
import psycopg2 
from convertHex import calculateAverage

# Python 3 compat
if sys.version_info[0] >= 3:
    raw_input = input

#to access the Spatial PostgreSQL database
user = "postgres"                 # raw_input("Database username:")
passwd = "****"                     # getpass.getpass("Password for " + user + ":")
database_name = "tp_ai"          # raw_input("Database name:")

#assuming there is a spatial table Landuse (imported from a shapefile available at
connection_str='postgresql://'+user+':'+passwd+'@localhost:5432/'+database_name

dir_src = './'
filenames = os.listdir(dir_src)

print(filenames)

# another directory smc_processed is created/used to store a flag for each session
# imported to the spatial database
if not os.path.exists(dir_src + "_processed"):
    os.makedirs(dir_src + "_processed")

acc_file = glob.glob("./*.csv")

if len(acc_file) > 0:
    for j in range(len(acc_file)):
        basename = acc_file[j].split("/")
        basename_file = basename[len(basename) - 1]
        if not os.path.exists(dir_src + "_processed/" + basename_file):

            recolhas_accelerometer = []
            # with open(dir_src+"_processed/"+basename_file,"w") as flag_file:
            #    flag_file.write("inserted " + str(len(recolhas_list)) + " points" )

            with open(acc_file[j]) as current_csv_file:
                for line in current_csv_file:
                    values = line.split(",")
                    if len(values) > 4 and values[0].isnumeric():
                        recolhas_accelerometer.append((values[1], values[0], values[2], values[3], values[4]))

            if len(recolhas_accelerometer) > 0:
                acc_out = []
                for i in range(len(recolhas_accelerometer)):
                    dec_accx = calculateAverage(recolhas_accelerometer[i][2].replace('\\', '0').replace('"', ''))
                    dec_accy = calculateAverage(recolhas_accelerometer[i][3].replace('\\', '0').replace('"', ''))
                    dec_accz = calculateAverage(recolhas_accelerometer[i][4].replace('\\', '0').replace('"', ''))

                    acc_out.append(
                        (recolhas_accelerometer[i][0], int(recolhas_accelerometer[i][1]),
                         sqrt(dec_accx + dec_accy + dec_accz)))

            if (len(acc_out) > 0):

                #  insert multiple points into the recolhas table  """
                sql1 = "INSERT INTO recolhas_accelerometer_sussex(actividade, instante, acceleration) VALUES (%s,%s,%s)"
                conn = None
                try:
                    #  connect to the PostgreSQL database
                    conn = psycopg2.connect(dbname=database_name, user=user,
                                            password=passwd)
                    # create a new cursor
                    cur = conn.cursor()
                    #  execute the INSERT statement
                    cur.executemany(sql1, acc_out)
                    #  commit the changes to the database
                    conn.commit()
                    #  close communication with the database
                    cur.close()
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally:
                    if conn is not None:
                        conn.close()