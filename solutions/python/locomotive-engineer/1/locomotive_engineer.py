
def get_list_of_wagons(*args):
    a=[]
    for i in args:
        a.append(i)
    return a
    

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    new=[]
    last=[]
    a=each_wagons_id.index(1)
    new=[each_wagons_id[a]]+missing_wagons+each_wagons_id[a+1:]+each_wagons_id[:a]
    return new


def add_missing_stops(route,**kwargs):
    l=list(kwargs.values())
    
    #for i in kwargs:
     #   l=kwargs[i][7:]
    route["stops"]=l
    return route
    


def extend_route_information(route, more_route_information):

    return route | more_route_information


def fix_wagon_depot(wagons_rows):
    return [list(row) for row in zip(*wagons_rows)]
