from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import *
from pytube import YouTube




app=QtWidgets.QApplication([])
dlg=uic.loadUi("YouTubeVideoDownloader.ui")






def download():
    if dlg.lineEdit.text()=="":
        msgbox("Warning!","You have not added any URL!")
    else:
        
        url=dlg.lineEdit.text()
        dlg.lineEdit.setText("")
        
        yt=YouTube(url)
        print(yt.title+"is downloading....\nPlease wait for atleast 30 seconds...")
        stream=yt.streams.first()
        stream.download()
        msgbox("Message","Your video has been downloaded successfully!")


    

def msgbox(title,message):
    QMessageBox.information(None,title,message)



dlg.pushButton.clicked.connect(download)



dlg.show()
app.exec()



