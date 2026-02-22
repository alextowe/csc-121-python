def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car_info['manufacturer'] = manufacturer.title()
    car_info['model'] = model.title()
    return car_info

car = make_car('toyota', 'tundra', color='blue', tow_package=True)
print(car)