import shapefile
import ast

# Returns a list of lists representing polygons
def text_to_list(file_path):
    f = open(file_path, 'r')
    lines = f.readlines()
    list_list = []
    for line in lines:
        list_of_lists = ast.literal_eval(line)
        tuple_list = []
        for coord in list_of_lists:
            tuple_list.append(tuple(coord)) 
        list_list.append(tuple_list)
    return list_list

def save_shp(file_path):
    poly_list = text_to_list(file_path)
    print(poly_list)

    w = shapefile.Writer('shp.shp')
    w.field('name', 'C')

    slice_ = 0
    for polygon in poly_list:
        w.poly(poly_list) 
        w.record('Polygon' + str(slice_))

    w.close()
