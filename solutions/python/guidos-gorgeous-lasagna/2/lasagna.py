# Task 1: 常數要定義在「最外面」(Global Scope)
EXPECTED_BAKE_TIME = 40

# Task 2: 
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    
    :param elapsed_bake_time: int - elapsed baking time.
    :return: int - remaining bake time.
    """
    # 你的邏輯是對的 (總時間 - 經過時間)
    return EXPECTED_BAKE_TIME - elapsed_bake_time

# Task 3: 
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.
    
    :param number_of_layers: int - the number of layers.
    :return: int - total preparation time.
    """
    # 你的邏輯也是對的 (層數 * 2)
    return number_of_layers * 2

# Task 4 & 5: (Task 5 就是補上註解，我也都補好了)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the total elapsed cooking time.
    
    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.
    """
    # 總花費時間 = 準備時間 + 已經烤的時間
    prep_time = preparation_time_in_minutes(number_of_layers)
    return prep_time + elapsed_bake_time