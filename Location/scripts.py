from Location.models import Area


# Script for inserting any three Areas of your choice into a database table named areas.

def add_area():

    area = ['Chinhoyi', 'Harare', 'Bindura']

    for i in area:

        try:
            obj = Area.objects.get(name=i)
        except Area.DoesNotExist:
            obj = Area(name=i)
            obj.save()
            print(f'{i} added')
