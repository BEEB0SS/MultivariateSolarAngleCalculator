# Multivariate Solar Angle Calculator calculates the necessary mirror angles for a certain distance relative to the point of where you want to reflect sunlight. 
import math
import copy

diagonaldistance = 0
horizontaldistance = 0
verticaldistance = 0
elevation = 0
mirrorTime = 0
Azimuth = 0


AllIncidentAngles = []
# This inputs the incident angles at each time. You calculate this from this website:
#https://gml.noaa.gov/grad/solcalc/ 
#Latitude: 35.802987
#Longitude: -78.902145
def calcVerticalIncidentangle():
  global AllIncidentAngles
  Angle308 = input("What is the solar elevation at 3:08:30?: ")
  Angle317 = input("What is the solar elevation at 3:17?: ")
  Angle325 = input("What is the solar elevation at 3:25:30?: ")
  Angle334 = input("What is the solar elevation at 3:34?: ")
  Angle342 = input("What is the solar elevation at 3:42:30?: ")
  Angle351 = input("What is the solar elevation at 3:51: ")
  
  

  AllIncidentAngles = [Angle308, Angle317, Angle325, Angle334, Angle342, Angle351]

  return AllIncidentAngles

#This calculates the vertical reflection angle needed relative to the board  
def calcVerticalReflectionangle(): #group refers to which side of the board the mirrors are on 
    global diagonaldistance, elevation

    dist = float(diagonaldistance)
    
    height = 21 
    elevation1 = float(elevation)
    
    actual_height = height - elevation1
    reflection_angle = math.atan(actual_height / dist)    
    reflection_angle_degrees = reflection_angle * (180 / math.pi)

    return reflection_angle_degrees

#This calculates the verticle normal and parses through the different incident angles and calculates the normal based on the needed reflection angle
def calculateVerticalNormal():
  global mirrorTime
  timeofday = mirrorTime
  try:
    if '3:08:30' in timeofday:
      incidentangle = AllIncidentAngles
      incidentangle = float(incidentangle[0])
      reflectionangle = calcVerticalReflectionangle()
      difference = abs(incidentangle - reflectionangle)/2
      if difference > 90: print ("FIX calculateVerticalNormal, difference is greater than 180, line 56")
      if incidentangle > reflectionangle:
        normal = reflectionangle + difference
      elif reflectionangle > incidentangle:
        normal = incidentangle + difference
      else:
        print("Error in line 62")
      normal = round(normal, 0)
      return normal
    elif '3:17' in timeofday:
      incidentangle = AllIncidentAngles
      incidentangle = float(incidentangle[1])
      reflectionangle = calcVerticalReflectionangle()
      difference = abs(incidentangle - reflectionangle)/2
      if difference > 90: print ("FIX calculateVerticalNormal, difference is greater than 180, line 70")
      if incidentangle > reflectionangle:
        normal = reflectionangle + difference
      elif reflectionangle > incidentangle:
        normal = incidentangle + difference
      else:
        print("Error in line 76")
      normal = round(normal, 0)
      return normal
    elif '3:25:30' in timeofday:
      incidentangle = AllIncidentAngles
      incidentangle = float(incidentangle[2])
      reflectionangle = calcVerticalReflectionangle()
      reflectionangle = 180 - reflectionangle
      difference = abs(incidentangle - reflectionangle)/2
      if difference > 90: print ("FIX calculateVerticalNormal, difference is greater than 180, line 85")
      if incidentangle > reflectionangle:
        normal = reflectionangle + difference
      elif reflectionangle > incidentangle:
        normal = incidentangle + difference
      else:
        print("Error in line 91")
      normal = round(normal, 0)
      return normal
    elif '3:34' in timeofday:
      incidentangle = AllIncidentAngles
      incidentangle = float(incidentangle[3])
      reflectionangle = calcVerticalReflectionangle()
      difference = abs(incidentangle - reflectionangle)/2
      if difference > 90: print ("FIX calculateVerticalNormal, difference is greater than 180, line 99")
      if incidentangle > reflectionangle:
        normal = reflectionangle + difference
      elif reflectionangle > incidentangle:
        normal = incidentangle + difference
      else:
        print("Error in line 105")
      normal = round(normal, 0)
      return normal
    elif '3:42:30' in timeofday:
      incidentangle = AllIncidentAngles
      incidentangle = float(incidentangle[4])
      reflectionangle = calcVerticalReflectionangle()
      difference = abs(incidentangle - reflectionangle)/2
      if difference > 90: print ("FIX calculateVerticalNormal, difference is greater than 180, line 113")
      if incidentangle > reflectionangle:
        normal = reflectionangle + difference
      elif reflectionangle > incidentangle:
        normal = incidentangle + difference
      else:
        print("Error in line 119")
      normal = round(normal, 0)
      return normal
    elif '3:51' in timeofday:
      incidentangle = AllIncidentAngles
      incidentangle = float(incidentangle[5])
      reflectionangle = calcVerticalReflectionangle()
      difference = abs(incidentangle - reflectionangle)/2
      if difference > 90: print ("FIX calculateVerticalNormal, difference is greater than 180, line 127")
      if incidentangle > reflectionangle:
        normal = reflectionangle + difference
      elif reflectionangle > incidentangle:
        normal = incidentangle + difference
      else:
        print("Error in line 133")
      normal = round(normal, 0)
      return normal
  except:
    print("Wrong time inputted")


# This calculates the Vertical mirror angle based on the normal function
def calcVerticalMirrorAngle():
  normal = calculateVerticalNormal()
  if normal <= 90.0:
    verticalmirrorangle = normal + 90.0
    return 180 - verticalmirrorangle
  elif normal > 90.0:
    verticalmirrorangle = normal + 90.0
    verticalmirrorangle -= 180.0
    verticalmirrorangle = 90.0 - verticalmirrorangle
    print('This mirror angle is reversed with 0 being the west and 180 being the east')
    return 180 - verticalmirrorangle

#This method calculates the necesssary the horizontal mirror angle rotation needed on the horizontal axis.  
#https://gml.noaa.gov/grad/solcalc/ 
#Latitude: 35.802987
#Longitude: -78.902145
def calcHorizontalMirrorAngle(): 
  global horizontaldistance, verticaldistance, Azimuth
  
  #Azimuth is in respect to the North
  IncidentAngle =  float(Azimuth)
  # D = distance from mirror to Box (w/ help of Pythag)
  # use the legs of that triangle w/ Pythag
  # H = distance along east-west line
  # V = distance along north-south license
  H = horizontaldistance
  V = verticaldistance
  H = float(H)
  V = float(V)
  #reflection angle is measured counterclockwise from north starting at the mirror
  #Top Right
  if H > 0 and V > 0:
    reflectionAngle = math.atan(H/V)
    reflectionAngle = reflectionAngle * (180/math.pi)
    reflectionAngle = reflectionAngle + 180
    
    '''diff = reflectionAngle - IncidentAngle
    diff = diff/2
    normal = IncidentAngle + diff'''

  #Top Left
  elif H < 0 and V > 0:
    H = abs(H)
    V = abs(V)
    reflectionAngle = math.atan(H/V)
    reflectionAngle = reflectionAngle * (180/math.pi)
    reflectionAngle = 180 - reflectionAngle
    
    '''diff = abs(IncidentAngle-reflectionAngle)/2
    if IncidentAngle > reflectionAngle:
      normal = reflectionAngle + diff
    elif reflectionAngle > IncidentAngle:
      normal = IncidentAngle + diff'''
  
  #Bottom Left
  elif H < 0 and V < 0: 
    H = abs(H)
    V = abs(V)
    reflectionAngle = math.atan(H/V)
    #changed from atan(H/V)
    reflectionAngle = reflectionAngle * (180/math.pi)
    
    '''diff = (IncidentAngle - reflectionAngle)/2
    normal = diff + reflectionAngle'''
    
    #this angle is wrt to east-west license


  #Bottom Right
  elif H > 0 and V < 0:
    H = abs(H)
    V = abs(V)
    reflectionAngle = math.atan(H/V)
    #changed from atan(H/V)
    reflectionAngle = reflectionAngle * (180/math.pi)
    reflectionAngle = 360 - reflectionAngle
    '''diff = reflectionAngle - IncidentAngle
    diff = diff/2
    normal = IncidentAngle + diff'''
    

  elif V == 0 and H > 0:
    reflectionAngle = 90    
  elif V == 0 and H < 0:
    reflectionAngle = 270
  
  reflectionAngle = round(reflectionAngle, 2)

  difference = abs(IncidentAngle - reflectionAngle)

  if difference > 180:  
    difference = 360 - difference
    if IncidentAngle > reflectionAngle:
      normal = difference/2 + IncidentAngle
    elif reflectionAngle > IncidentAngle:
      normal = difference/2 + reflectionAngle
  
  elif difference < 180:
    if IncidentAngle > reflectionAngle:
      normal = difference/2 + reflectionAngle
    elif reflectionAngle > IncidentAngle:
      normal = difference/2 + IncidentAngle
  
  
  #Remember that normal is wrt True North in the clockwise direction
  #At 0 degrees, the mirror should completely face True North. (90: east, 180: south, 270: west)
  #This means that NORMAL extends towards North

  
  HorizontalMirrorAngle = round(normal, 0)
  return HorizontalMirrorAngle


# This combines the horizontal and vertical mirror angles into one list 
def finalMirrorangle():
  horizontalangle = calcHorizontalMirrorAngle()
  verticalangle = calcVerticalMirrorAngle()
  listofangles = ["Horizontal Angle: " +  str(horizontalangle)," Vertical Angle: "+ str(verticalangle)]
  return listofangles


def main():
  global AllIncidentAngles, diagonaldistance, horizontaldistance, verticaldistance, elevation, mirrorTime, Azimuth
 
  mirror_angle_file = open("angles.txt","w")
  with open("info.txt") as measurements:
    data = measurements.readlines()
  x = True

  while x:
    day = input("What is the day of experimentation? ")
    temp = input("What is the temperature outside during expeirmentation on the forecast (F°)? ")
    mirrorangles = []
    AllIncidentAngles = calcVerticalIncidentangle()
    mirror_angle_file.write(" "+"\n")
    mirror_angle_file.write(" "+"\n")
    mirror_angle_file.write(day+"\n")
    mirror_angle_file.write(temp+"F°"+"\n") 
    mirror_angle_file.write(" "+"\n")
    times = ["3:51","3:42:30","3:34","3:25:30","3:25:30","3:17","3:08:30","3:51","3:42:30","3:34","3:25:30","3:17","3:08:30", "3:51","3:42:30","3:34","3:25:30","3:17","3:08:30","3:51","3:42:30","3:34","3:34","3:25:30","3:17","3:08:30"]
    row1 = []
    for count, line in enumerate(data):
      
      mirrorTime = times[count]
      
      beamnumber = count + 1
      values = line.split(":")
      values = values[1]
      #Diagonal Distance
      diagonalDistance = values.split("Diagonal Distance|")
      diagonalDistance = diagonalDistance[1]
      diagonalDistance = diagonalDistance.split(", Horizontal Distance|")
      diagonaldistance = diagonalDistance[0]
      print("Diagonal Distance ", diagonaldistance)      
      #HorizontalDistance
      horizontalDistance = values.split("Horizontal Distance|")
      horizontalDistance = horizontalDistance[1]
      horizontalDistance = horizontalDistance.split(", Vertical Distance")
      horizontaldistance = horizontalDistance[0]
      print("Horizontal Distance", horizontaldistance) 
      #VerticalDistance
      verticalDistance = values.split("Vertical Distance|")
      verticalDistance = verticalDistance[1]
      verticalDistance = verticalDistance.split(", Elevation")
      verticaldistance = verticalDistance[0]
      print("Vertical Distance: ", verticaldistance)
      #Elevation
      Elevation = values.split("Elevation|")
      elevation = Elevation[1]
      print("Elevation: ", elevation)
      
      if count == 4:
        Azimuth = float(input(f"What is the azimuth value at the time ({mirrorTime}) assigned to the mirror? SAME AS PREVIOUS ONE: "))
        row1.append(Azimuth)
      
      elif  0 <= count < 4 or 4 < count < 6 :
        Azimuth = float(input(f"What is the azimuth value at the time ({mirrorTime}) assigned to the mirror?: "))
        row1.append(Azimuth)

      #Insert failsafe for Beam 5 here
        
      elif count == 6:
        Azimuth = float(input(f"What is the azimuth value at the time ({mirrorTime}) assigned to the mirror?: "))
        row1.append(Azimuth)
        row2 = copy.deepcopy(row1)
        row4 = copy.deepcopy(row1)
        row4[3] = row4[2]
        
        del row2[3]
      elif 6 < count <= 18:
        index = count%6
        Azimuth = row2[index]
      elif 18 < count < 25:
        index = count%7
        Azimuth = row4[index]
      ans = finalMirrorangle()
      ans0 = ans[0]
      ans1 = ans[1]
      print("Mirror " + str(beamnumber) + f" ({mirrorTime}) : " + str(ans0) + ',' + str(ans1))
      print()
      mirrorangles.append("Mirror " + str(beamnumber) + ":" + str(ans0) + ',' + str(ans1))
      mirror_angle_file.write("Mirror " + str(beamnumber) + ":" + str(ans0) + ',' + str(ans1)+"\n")
    continue_statement = input("Are you done: ")
    if 'y' in continue_statement:
      x = False
      print("You can check the angles.txt file now")
      mirror_angle_file.close()
    else:
      x = True
     
    print()
    print()
    print()
    print()
    print()
    print()
    print(day)
    print(mirrorangles)
    print()
    print()
    print()
    
    

if __name__ == '__main__':
  main()