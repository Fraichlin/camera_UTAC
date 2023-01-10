import cv2, os
import numpy as np

IMG_PATH = os.getcwd()+'/img/'
CURRENT_PATH = os.getcwd()

list_files = os.listdir(IMG_PATH)

def detect(fil):
      # Read image
      image = cv2.imread(IMG_PATH + fil)
      
      # Convert image to grayscale
      gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
      
      # Use canny edge detection
      edges = cv2.Canny(gray,50,150,apertureSize=3)
      
      # Apply HoughLinesP method to
      # to directly obtain line end points
      lines_list =[]
      lines = cv2.HoughLinesP(
                edges, # Input edge image
                1, # Distance resolution in pixels
                np.pi/180, # Angle resolution in radians
                threshold=100, # Min number of votes for valid line
                minLineLength=5, # Min allowed length of line
                maxLineGap=10 # Max allowed gap between line for joining them
                )
      
      # Iterate over points
      try :
                lines = np.array([[4,5,6,7],[2,4,1,0],[7,1,3,9]])
                index = np.random.randint(0,len(lines))
                taille_min = 50

                line_temp = lines[index]
                point1 = [line_temp[0],line_temp[1]]
                point2 = [line_temp[2],line_temp[3]]

                points = [point1,point2]
                new_lines = []
                for l in lines:
                  if not np.array_equal(l,line_temp):
                    point1 = [l[0],l[1]]
                    point2 = [l[2],l[3]]

                    flag1 = 0
                    flag2 = 0
                    for p in points:
                      dist1 = np.linalg.norm(np.array(point1)-np.array(p))
                      dist2 = np.linalg.norm(np.array(point2)-np.array(p))

                      if dist1 <= taille_min and dist1 >= 0:
                        new_lines.append([p[0],p[1],point2[0],point2[1]])
                        flag1 =1
                      if dist2 <= taille_min and dist2 >= 0:
                        new_lines.append([p[0],p[1],point1[0],point1[1]])
                        flag2 = 1
                    if flag1 == 1: points.append(point2)
                    if flag2 == 1: points.append(point1)
               
                print(np.array(new_lines))

                for n in new_lines:
                        cv2.line(image,(n[0],n[1]),(n[2],n[3]),(0,255,0),2)

            '''for points in lines:
                  # Extracted points nested in the list
                x1,y1,x2,y2=points[0]
                # Draw the lines joing the points
                # On the original image
                cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)
                # Maintain a simples lookup list for points
                lines_list.append([(x1,y1),(x2,y2)])'''
                
            # Save the result image
            cv2.imwrite(CURRENT_PATH + '/DetectedLines/'+fil,image)
            print(str(len(lines)) + " lignes détectées")
      except:
            print("Aucune ligne détectée")

