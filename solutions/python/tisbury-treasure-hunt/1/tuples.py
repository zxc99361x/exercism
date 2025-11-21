def get_coordinate(record):
    return record[1]

def convert_coordinate(coordinate):
    s=[]
    s+=coordinate[0]
    s+=coordinate[1]
    return tuple(s)
        
def compare_records(azara_record, rui_record):
    cc=convert_coordinate(azara_record[1])
    return cc in rui_record

def create_record(azara_record, rui_record):
    cr=convert_coordinate(azara_record[1])
    if cr in rui_record:
        return tuple(azara_record)+tuple(rui_record)
    else:
        return 'not a match'


def clean_up(combined_record_group):
    s=""
    for i in combined_record_group:
        cu=(i[0],)+i[2:]
        s+=str(cu)+"\n"
    return s
        
