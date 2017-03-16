
segundos_str = input("Por favor, entre com o numero de segundos que deseja converter: ")
total_segs = int(segundos_str)

dias = total_segs // 86400
horas = (total_segs % 86400) // 3600
segs_retantes = total_segs % 3600
minutos = segs_retantes // 60
segs_retantes_final = segs_retantes % 60

print(dias, "dias,", horas, "horas, ", minutos,"minutos e", segs_retantes_final, "segundos.")
