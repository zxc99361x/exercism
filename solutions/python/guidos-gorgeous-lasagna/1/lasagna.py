EXPECTED_BAKE_TIME=40;

def bake_time_remaining(x):
    """Calculate the bake time remaining.
    
    :param elapsed_bake_time: int - elapsed baking time.
    :return: int - remaining bake time.
    """
    return EXPECTED_BAKE_TIME-x;

def preparation_time_in_minutes(y):
    """Calculate the preparation time.
    
    :param number_of_layers: int - the number of layers.
    :return: int - total preparation time.
    """
    return y*2;

def elapsed_time_in_minutes(x,y):
    """
    Calculate the total elapsed cooking time.
    
    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.
    """
    z=preparation_time_in_minutes(x)+y;
    return z;
    