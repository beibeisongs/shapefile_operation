# encoding=utf-8
# Date: 2018-11-10
# Author: MJUZY
# URL: https://blog.csdn.net/stahuri/article/details/80838226


import csv
import shapefile


def shp2geo(path):

    csvFile2 = open("shp.csv", "a+", newline='', encoding="utf-8")    # 设置newline，否则两行之间会空一行
    writer = csv.writer(csvFile2)

    reader = shapefile.Reader(path)

    fields = reader.fields[1:]
    field_names = [field[0] for field in fields]

    buffer = []

    for sr in reader.shapeRecords():
        record = sr.record
        shape = sr.shape

        points = shape.points

        for r in record:
            if r == '':
                r = "none"

            buffer.append(r)

        buffer.append(points)

        writer.writerow(buffer)

        buffer = []

    csvFile2.close()


dirPath = "D:/USBei/Shapefile_data"
path = dirPath + '/' + "CHN_adm3.shp"
shp2geo(path)
