
import config

cult_attrinutes = config.CultAttr()


#Utility Functions

def select_day(x):
    return x[-1]

def process(data):
    if data.get('days',None):
        days = [i['id'] for i in data['days']]
        info = data.get("classByDateMap",None)
        if info:
            desired_slots = [i for i in info[select_day(days)]['classByTimeList'] if i['id'] in cult_attrinutes.time]
            if desired_slots:
                desired_centers = [i for i in desired_slots[0]['centerWiseClasses']
                                   if i['centerId'] in cult_attrinutes.center]
                if desired_centers:
                    desired_classes = [i for i in desired_centers[0]['classes']
                                       if i['workoutId'] in cult_attrinutes.classes]
                    if desired_classes:
                        for i in desired_classes:
                            if not i['waitlistInfo']:
                                if i["state"]!="BOOKED":
                                    return i['id'], True
                                else:
                                    return 'Already Booked', False
                            else:
                                return 'waitlist', False
                    else:
                        return 'classes', False
                else:
                    return 'centers', False
            else:
                return 'slots', False
        else:
            return 'classByDateMap', False
    else:
        return 'Days', False

