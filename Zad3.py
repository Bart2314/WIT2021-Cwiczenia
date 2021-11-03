AveCarSpeed = int(input("Podaj przypuszczalną średnią prędkość na trasie w km\h: "))

TrainTimeHour = 2.75
DistanceKm = 250
AveTrainSpeed = DistanceKm / TrainTimeHour

if AveCarSpeed > AveTrainSpeed:
    print("Na miejsce szybciej dojedziesz autem.")
else:
    print("Na miejsce szybciej dojedziesz pociągiem.")


