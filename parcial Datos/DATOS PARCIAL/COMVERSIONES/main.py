#malo
# import pandas as pd

# datos = pd.read_csv("VIH\mines.csv")

# sql_insert = "CREATE TABLE if not exists mines(\n"

# for i in datos.columns:
#     sql_insert = sql_insert + i + " TEXT,\n"

# sql_insert = sql_insert[0:-2]

# sql_insert = sql_insert + ");"

# print(sql_insert)
# def return_insert(values):
#     txt_data = ""
#     for i in range(len(values)):  
#         if i == 0: 
#             if str(values[i]) == "nan":
#                 txt_data = txt_data + "TO_DATE(\'\', 'yyyy/mm/dd'),"
#             elif isinstance(values[i], (int, float)):
#                 txt_data = txt_data + "TO_DATE(" + str(values[i]) + ", 'yyyy/mm/dd'),"
#             else:
#                 txt_data = txt_data + "TO_DATE(\'" + str(values[i]) + "\', 'yyyy/mm/dd'),"
#         else:
#             if str(values[i]) == "nan":
#                 txt_data = txt_data + "\'\',"
#             elif isinstance(values[i], (int, float)):
#                 txt_data = txt_data + str(values[i]) + ","
#             else:
#                 txt_data = txt_data + "\'" + str(values[i]) + "\',"

#     return txt_data
#bueno
import math
import pandas as pd

datos = pd.read_csv("parcial\VIH\product_worker.csv", sep="|")

datos.columns = datos.columns.str.replace("|", "_")

sql_insert = "CREATE TABLE if not exists workers(\n"

for i in datos.columns:
    sql_insert = sql_insert + i + " TEXT,\n"

sql_insert = sql_insert[0:-2]

sql_insert = sql_insert + ");"

print(sql_insert)


sql_datos_cabecera = "insert into product_worker (id_product_worker,"
for i in datos.columns:
    sql_datos_cabecera = sql_datos_cabecera  + i + ","

sql_datos_cabecera = sql_datos_cabecera[0:-1]

sql_datos_cabecera = sql_datos_cabecera + ") VALUES" "(" 

# def return_insert(values):
#     txt_data = ""
#     for i in range(len(values)):  
#         if i == 3: 
#             if str(values[i]) == "nan":
#                 txt_data = txt_data + "TO_DATE(\'\', 'yyyy/mm/dd'),"
#             elif isinstance(values[i], (int, float)):
#                 txt_data = txt_data + "TO_DATE(" + str(values[i]) + ", 'yyyy/mm/dd'),"
#             else:
#                 txt_data = txt_data + "TO_DATE(\'" + str(values[i]) + "\', 'yyyy/mm/dd'),"
#         else:
#             if str(values[i]) == "nan":
#                 txt_data = txt_data + "\'\',"
#             elif isinstance(values[i], (int, float)):
#                 txt_data = txt_data + str(values[i]) + ","
#             else:
#                 txt_data = txt_data + "\'" + str(values[i]) + "\',"

#     return txt_data

# def return_insert(values):
#     txt_data = ""
#     for i in values:
#         if pd.notna(i):
#             try:
#                 date_value = pd.to_datetime(i)
#                 txt_data += "TO_DATE('" + date_value.strftime('%Y-%m-%d') + "','YYYY-MM-DD'),"
#             except ValueError:
                
#                 txt_data += "'" + str(i) + "',"
#         else:
#             txt_data += "NULL,"
#     return txt_data

def return_insert(values):
    txt_data = ""
    for i in values:
        if str(i) == "nan":
            txt_data = txt_data + "\'\',"
        else:
            txt_data = txt_data +  str(math.ceil(i)) + ","  # Eliminamos round() para mantener los valores como están

    return txt_data

SQL_FINAL = ""
for indice, fila in datos.iterrows():
    txt = return_insert(fila.values)
    txt = txt[0:-1]

    SQL_FINAL = SQL_FINAL + sql_datos_cabecera + str(indice+1) + "," +txt + ");\n"


with open("product_worker.sql", "w", encoding="UTF-8") as f:
    f.write(SQL_FINAL)