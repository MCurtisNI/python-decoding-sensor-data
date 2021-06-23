# Runner script for all modules
from load_data import load_sensor_data
from house_info import HouseInfo
from datetime import date, datetime
from temperature_info import TemperatureData
from statistics import mean
from particle_count_info import ParticleData
from humidity_info import HumidityData

##############################
# Do not remove these two lines
# They are needed to validate your unittest
data = []
print("Sensor Data App")
data = load_sensor_data()
print("Loaded records: {}".format(len(data)))
house_info = HouseInfo(data)
test_area = 1
recs = house_info.get_data_by_area('id', rec_area=test_area)
print("\nHouse sensor records for area {} = {}".format(test_area, len(recs)))
test_date = datetime.strptime("5/9/20", "%m/%d/%y")
recs = house_info.get_data_by_date('id', rec_date=test_date)
print("\nHouse sensor records for date: {} = {}".format(test_date.strftime("%m/%d/%y"), len(recs)))
##############################

# Module 1 code here:

# Module 2 code here:

# Module 3 code here:

temperature_data = TemperatureData(data)
recs = temperature_data.get_data_by_area(rec_area=test_area)
print("\nHouse temperature sensor records for area {} = {}".format(test_area, len(recs)))
print("\tMaximum: {0}, Minimum: {1} temperatures".format(max(recs), min(recs)))

recs = temperature_data.get_data_by_date(rec_date=test_date)
print("\nHouse Temperature sensor records for date: {} = {}".format(test_date.strftime("%m/%d/%y"), len(recs)))
print("\tMaximum: {0}, Minimum: {1} temperatures".format(max(recs), min(recs)))
# Module 4 code here:

print("\nHouse Humidity sensor records for area {} = {}".format(test_area, len(recs)))
print("\tAverage: {} humidity".format(mean(recs)))

print("House Humidity sensor records for date: {} = {}".format( test_date.strftime("%m/%d/%y"), len(recs)))
print("\tAverage: {} humidity".format(mean(recs)))

particle_data = ParticleData(data)
recs = particle_data.get_data_by_area(rec_area=test_area)
print("\nHouse Particle sensor records for area {} = {}".format(test_area, len(recs)))

concentrations = particle_data.get_data_concentrations(data=recs)
print("\tGood Air Quality Recs: {}".format(concentrations["good"]))
print("\tModerate Air Quality Recs: {}".format(concentrations["moderate"]))
print("\tBad Air Quality Recs: {}".format(concentrations["bad"]))

recs = particle_data.get_data_by_date(rec_date=test_date)
print("\nHouse Particle sensor records for date: {} = {}".format( test_date.strftime("%m/%d/%y"), len(recs)))
concentration = particle_data.get_data_concentrations(data=recs)

print("\tGood Air Quality Recs: {}".format(concentrations["good"]))
print("\tModerate Air Quality Recs: {}".format(concentrations["moderate"]))
print("\tBad Air Quality Recs: {}".format(concentrations["bad"]))

# Module 5 code here: