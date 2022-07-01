#in terminal --> pip install qrcode
# pip install image   if image error

#in qrcode module there is QRCode class which has many methods. We have to make an object of the QRCode class 
# and create a qrcode using these methods.

#if we are using  'from qrcode import all'  then we don't have to give reference like qr=qrcode.QRCode, simply qr=QRCode(..) will do.

import qrcode
qr=qrcode.QRCode(                    #qr is an object of QRCode class
    version=15, #size of our qrcode
    box_size=10, #size of boxes in our qrcode
    border=5  #width of border
)
#now we'll create a data variable in which we will store a link

data="https://www.linkedin.com/in/harikabatchala/"
qr.add_data(data) #this will add mentioned data in our qrcode
qr.make(fit=True)  #this will generate final qrcode

#this qrcode generated has to be saved in a image
img=qr.make_image(fill="black",back_color="white")
img.save('text.png') #save the image and give it a name

