
Day_Time = "Morning"
print("Hii, Goood <Day_Time>")

#By using String Formating Method:
day_time ="Morning"
print("Hii,Goood {}".format(day_time))
day_time ="evening"
print("Hii,Goood {}".format(day_time))
day_time ="Afternoon"
print("Hii,Goood {} ,My name is {}, My age is {}".format(day_time, 'Dnyaneshwar',29))

#OR
#f-string 3.6 (formmatted strings)
name = 'Dnyaneshwar'
age =29
print(f"Hii,Goood {day_time} ,My name is {name}, My age is {age}")

#Old-c Style
info="my age is %d,%f,%s" % (29,23.43,'Dnyaneshwar')
print(info)




