
weight =float(input('введите вес в тоннах:'))


truck_capacity = 22.000
gaz_capasity =1.35

truck_number = weight // truck_capacity
remein_after_truck = weight % truck_capacity

gaz_number = remein_after_truck // gaz_capasity
remein_after_gaz = remein_after_truck % gaz_capasity
print('понадобиться ',int(truck_number),'фуры','понадобиться',int(gaz_number),'газелей' )






