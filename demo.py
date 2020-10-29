import cv2
import numpy as np 
import imutils 
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
	success,frame=cap.read()
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


	lower_s_g_green=np.array([37,52,100])
	upper_s_g_green=np.array([42,255,255])

	lower_b_green=np.array([46,52,72])
	upper_b_green=np.array([52,255,255])

	lower_d_green=np.array([65,52,72])
	upper_d_green=np.array([75,255,255])

	lower_j_green=np.array([84,52,72])
	upper_j_green=np.array([94,255,255])

	lower_t_blue=np.array([95,52,72])
	upper_t_blue=np.array([102,255,255])

	lower_pantone=np.array([106,52,72])
	upper_pantone=np.array([113,255,255])

	lower_pantone1=np.array([115,42,0])
	upper_pantone1=np.array([117,255,255])


	lower_ral_blue=np.array([108,52,72] )
	upper_ral_blue=np.array([111,225,255])

	lower_blue=np.array([118,52,100])
	upper_blue=np.array([126,255,255])

	lower_c_red=np.array([170,84,141])
	upper_c_red=np.array([190,255,255])
	
	lower_orange1= np.array([0, 50, 80])
	upper_orange1=np.array([10,255,255])

	lower_orange2=np.array([11,50,80])
	upper_orange2=np.array([14,255,255])

	lower_d_yellow=np.array([15,55,100])
	upper_d_yellow=np.array([20,255,255])

	lower_l_yellow=np.array([30,50,100])
	upper_l_yellow=np.array([35,255,255])

	lower_mouve=np.array([133,42,0])
	upper_mouve=np.array([145,255,255])

	lower_pink=np.array([160,42,0])
	upper_pink=np.array([166,255,255])

        
#	lower_kblue=np.array([102,52,72])
#	upper_kblue=np.array([130,255,255])





	mask1=cv2.inRange(hsv,lower_s_g_green,upper_s_g_green)
	mask2=cv2.inRange(hsv,lower_b_green,upper_b_green)
	mask3=cv2.inRange(hsv,lower_d_green,upper_d_green)
	mask4=cv2.inRange(hsv,lower_j_green,upper_j_green)
	mask5=cv2.inRange(hsv,lower_t_blue,upper_t_blue)
	mask6=cv2.inRange(hsv,lower_pantone,upper_pantone)
	mask7=cv2.inRange(hsv,lower_pantone1,upper_pantone1)
	mask8=cv2.inRange(hsv,lower_ral_blue,upper_ral_blue)
	mask9=cv2.inRange(hsv,lower_blue,upper_blue)
	mask10=cv2.inRange(hsv,lower_c_red,upper_c_red)
	
	mask11=cv2.inRange(hsv,lower_orange1,upper_orange1)
	mask12=cv2.inRange(hsv,lower_orange2,upper_orange2)
	
	mask13=cv2.inRange(hsv,lower_d_yellow,upper_d_yellow)
	mask14=cv2.inRange(hsv,lower_l_yellow,upper_l_yellow)
	mask15=cv2.inRange(hsv,lower_mouve,upper_mouve)
	mask16=cv2.inRange(hsv,lower_pink,upper_pink)
#	mask17=cv2.inRange(hsv,lower_kblue,upper_kblue)



	cnts1=cv2.findContours(mask1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnts1=imutils.grab_contours(cnts1)

	cnts2=cv2.findContours(mask2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnts2=imutils.grab_contours(cnts2)
	

	cnts3=cv2.findContours(mask3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnts3=imutils.grab_contours(cnts3)
	
	cnts4=cv2.findContours(mask4,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnts4=imutils.grab_contours(cnts4)
	cnts5=cv2.findContours(mask5,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnts5=imutils.grab_contours(cnts5)
	

	cnts6=cv2.findContours(mask6,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnts6=imutils.grab_contours(cnts6)
	
	cnts7=cv2.findContours(mask7,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnts7=imutils.grab_contours(cnts7)
	
	cnts8=cv2.findContours(mask8,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnts8=imutils.grab_contours(cnts8)

	cnts9=cv2.findContours(mask9,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnts9=imutils.grab_contours(cnts9)

	cnts10=cv2.findContours(mask10,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnts10=imutils.grab_contours(cnts10)

	cnts11=cv2.findContours(mask11,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnts11=imutils.grab_contours(cnts11)

	cnts12=cv2.findContours(mask12,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnts12=imutils.grab_contours(cnts12)

	cnts13=cv2.findContours(mask13,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnts13=imutils.grab_contours(cnts13)

	cnts14=cv2.findContours(mask14,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnts14=imutils.grab_contours(cnts14)

	cnts15=cv2.findContours(mask15,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnts15=imutils.grab_contours(cnts15)

	cnts16=cv2.findContours(mask16,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnts16=imutils.grab_contours(cnts16)
#	cnts17=cv2.findContours(mask17,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#	cnts17=imutils.grab_contours(cnts17)

	for c in cnts1:
		area1=cv2.contourArea(c)

		if area1 > 1000:
			cv2.drawContours(frame,[c],-1,(0,255,0),3)

			M=cv2.moments(c)

			cx=int(M["m10"]/M["m00"])
			cy=int(M["m01"]/M["m00"])

			cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
			cv2.putText(frame,"S/G Green",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),3)
			if area > 28000:
                            cv2.putText(frame,"Type: 5580F",(cx-30,cy-30),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),3)
                        elif area>25000 and area<28000:
                            cv2.putText(frame,"Type: DP480N",(cx-30,cy-30),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),3)
			

	for c in cnts2:
		area2=cv2.contourArea(c)

		if area2 > 1000:
			cv2.drawContours(frame,[c],-1,(0,255,0),3)
			print(area2)
			M=cv2.moments(c)

			cx=int(M["m10"]/M["m00"])
			cy=int(M["m01"]/M["m00"])

			cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
			cv2.putText(frame,"Bright Green",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),3)

	for c in cnts3:
		area2=cv2.contourArea(c)

		if area2 > 10000:
			cv2.drawContours(frame,[c],-1,(0,255,0),3)

			M=cv2.moments(c)

			cx=int(M["m10"]/M["m00"])
			cy=int(M["m01"]/M["m00"])

			cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
			cv2.putText(frame,"Dark Green",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),3)
	for c in cnts4:
		area2=cv2.contourArea(c)

		if area2 > 1000:
			cv2.drawContours(frame,[c],-1,(0,255,0),3)

			M=cv2.moments(c)

			cx=int(M["m10"]/M["m00"])
			cy=int(M["m01"]/M["m00"])

			cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
			cv2.putText(frame,"J. Green",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),3)

	for c in cnts5:
		area2=cv2.contourArea(c)

		if area2 > 1000:
			cv2.drawContours(frame,[c],-1,(0,255,0),3)

			M=cv2.moments(c)

			cx=int(M["m10"]/M["m00"])
			cy=int(M["m01"]/M["m00"])

			cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
			cv2.putText(frame,"T. Blue",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),3)

	for c in cnts6:
		area2=cv2.contourArea(c)

		if area2 > 1000:
			cv2.drawContours(frame,[c],-1,(0,255,0),3)
			print(area2)
			M=cv2.moments(c)

			cx=int(M["m10"]/M["m00"])
			cy=int(M["m01"]/M["m00"])

			cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
			cv2.putText(frame,"300 C Pantone",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),3)


	for c in cnts7:
		area2=cv2.contourArea(c)

		if area2 > 1000:
			cv2.drawContours(frame,[c],-1,(0,255,0),3)

			M=cv2.moments(c)

			cx=int(M["m10"]/M["m00"])
			cy=int(M["m01"]/M["m00"])

			cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
			cv2.putText(frame,"293 C Pantone",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),3)


	for c in cnts8:
		area2=cv2.contourArea(c)

		if area2 > 1000:
			cv2.drawContours(frame,[c],-1,(0,255,0),3)

			M=cv2.moments(c)

			cx=int(M["m10"]/M["m00"])
			cy=int(M["m01"]/M["m00"])

			cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
			cv2.putText(frame,"Ral Blue",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),3)


	for c in cnts9:
		area2=cv2.contourArea(c)

		if area2 > 1000:
			cv2.drawContours(frame,[c],-1,(0,255,0),3)
			print (area2)
			M=cv2.moments(c)

			cx=int(M["m10"]/M["m00"])
			cy=int(M["m01"]/M["m00"])

			cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
			cv2.putText(frame,"Blue",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),3)


	for c in cnts10:
		area2=cv2.contourArea(c)

		if area2 > 1000:
			cv2.drawContours(frame,[c],-1,(0,255,0),3)

			M=cv2.moments(c)

			cx=int(M["m10"]/M["m00"])
			cy=int(M["m01"]/M["m00"])

			cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
			cv2.putText(frame,"Blue",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),3)

	for c in cnts11:
		area2=cv2.contourArea(c)

		if area2 > 1000:
			cv2.drawContours(frame,[c],-1,(0,255,0),3)
			print(area2)
			M=cv2.moments(c)

			cx=int(M["m10"]/M["m00"])
			cy=int(M["m01"]/M["m00"])

			cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
			cv2.putText(frame,"Bright Orange",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),3)



	for c in cnts12:
		area2=cv2.contourArea(c)

		if area2 > 1000:
			cv2.drawContours(frame,[c],-1,(0,255,0),3)

			M=cv2.moments(c)

			cx=int(M["m10"]/M["m00"])
			cy=int(M["m01"]/M["m00"])

			cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
			cv2.putText(frame,"Ral 2008 orange",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),3)



	for c in cnts13:
		area2=cv2.contourArea(c)

		if area2 > 1000:
			cv2.drawContours(frame,[c],-1,(0,255,0),3)

			M=cv2.moments(c)

			cx=int(M["m10"]/M["m00"])
			cy=int(M["m01"]/M["m00"])

			cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
			cv2.putText(frame,"Dark Yellow",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),3)


	for c in cnts14:
		area2=cv2.contourArea(c)

		if area2 > 1000:
			cv2.drawContours(frame,[c],-1,(0,255,0),3)

			M=cv2.moments(c)

			cx=int(M["m10"]/M["m00"])
			cy=int(M["m01"]/M["m00"])

			cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
			cv2.putText(frame,"Lemon Yellow",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),3)



	for c in cnts15:
		area2=cv2.contourArea(c)

		if area2 > 1000:
			cv2.drawContours(frame,[c],-1,(0,255,0),3)

			M=cv2.moments(c)

			cx=int(M["m10"]/M["m00"])
			cy=int(M["m01"]/M["m00"])

			cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
			cv2.putText(frame,"Mouve",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),3)



	for c in cnts16:
		area2=cv2.contourArea(c)

		if area2 > 1000:
			cv2.drawContours(frame,[c],-1,(0,255,0),3)

			M=cv2.moments(c)

			cx=int(M["m10"]/M["m00"])
			cy=int(M["m01"]/M["m00"])

			cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
			cv2.putText(frame,"F. Pink",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),3)
	
	cv2.imshow("result",frame)
	k=cv2.waitKey(2)
	if k == 27 :
		break


cap.release()
cv2.destroyAllWindows()

