import cv2
#add lines on images
pikachu = cv2.imread(r"pika.png",cv2.IMREAD_COLOR)
linecolor = (0,255,0)
linethickness = 13
startpoint = (0,100)
endpoint = (100,200)
pikachuline = cv2.line(pikachu,startpoint,endpoint,linecolor,linethickness)
cv2.imshow("pikachu with line",pikachuline)
cv2.waitKey(0)
#add rectangle
startingpoint = (0,100)
endingpoint = (200,300)
rectanglecolor = (255,0,0)
rectanglethickness = -1
pikachurectangle = cv2.rectangle(pikachu,startingpoint,endingpoint,rectanglecolor,rectanglethickness)
cv2.imshow("pikachu with rectangle",pikachurectangle)
cv2.waitKey(0)
#add circle
centerpoint = (100,100)
radius = 35
circlecolor = (0,255,0)
circlethickness = 15
pikachucircle = cv2.circle(pikachu,centerpoint,radius,circlecolor,circlethickness)
cv2.imshow("pikachu with line rectangle and circle", pikachucircle)
cv2.waitKey(0)

#text on screen
text = "Hello how are you doing"
font = cv2.FONT_ITALIC
textcolor = (255,255,255)
textthickness = 3
textcoordinates = (100,100)
fontscale = 1
newimage = cv2.putText(pikachu,text,textcoordinates,font,fontscale,textcolor,textthickness,cv2.LINE_8)
cv2.imshow("image",newimage)
cv2.waitKey(0)
