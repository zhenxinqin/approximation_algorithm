# -*- coding: UTF-8 -*-
states_needed = set(['mt','wa','or','id','nv','ut','ca','az'])

stations = {}
stations['kone'] = set(['id','nv','ut'])
stations['ktwo'] = set(['wa','id','mt'])
stations['kthree'] = set(['or','nv','ca'])
stations['kfour'] = set(['nv','ut'])
stations['kfive'] = set(['ca','az'])

final_stations = set()
# print stations
while states_needed:
	best_station = None
	states_covered = set()		#被覆盖的城市
	i = 0
	for station, state_for_station in stations.items():
		# print station,state_for_station
		i = i + 1
		print i 
		covered = states_needed & state_for_station		#覆盖城市与需要覆盖城市的交集
		print states_covered
		if len(covered) > len(states_covered):
			best_station = station
			# print best_station 
			states_covered = covered
		states_needed -= states_covered
		final_stations.add(best_station)
		# print states_covered,len(states_covered)
# for n in final_stations:
# 	print n

