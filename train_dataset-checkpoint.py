{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5b372e88",
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import*\n",
    "from tkinter import ttk\n",
    "from PIL import Image,ImageTk\n",
    "from tkinter import messagebox\n",
    "import mysql.connector\n",
    "import cv2\n",
    "import numpy as np\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3794ddff",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Exception in Tkinter callback\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\MEER\\anaconda3\\lib\\tkinter\\__init__.py\", line 1892, in __call__\n",
      "    return self.func(*args)\n",
      "  File \"<ipython-input-7-4fa865cbd926>\", line 44, in train_classifier\n",
      "    clf.train(faces,ids)\n",
      "cv2.error: OpenCV(4.7.0) D:\\a\\opencv-python\\opencv-python\\opencv_contrib\\modules\\face\\src\\lbph_faces.cpp:362: error: (-210:Unsupported format or combination of formats) Empty training data was given. You'll need more than one sample to learn a model. in function 'cv::face::LBPH::train'\n",
      "\n"
     ]
    }
   ],
   "source": [
    "class Train:\n",
    "    def __init__(self,root):\n",
    "        self.root=root\n",
    "        self.root.geometry(\"1560x768+0+0\")\n",
    "        self.root.minsize(1024,768)\n",
    "        self.root.title(\"Face Rcongnization System\")\n",
    "        \n",
    "        title_lbl = Label(self.root,text=\"TRAIN DATA SET\",font=(\"Helvetica\",30,\"bold\"),bg=\"white\",fg=\"darkblue\")\n",
    "        title_lbl.place(x=0,y=0,width=1400,height=45)\n",
    "        \n",
    "        self.img_top= Image.open(r\"C:\\Users\\MEER\\Desktop\\Face Recongnization system\\images\\std1.png\")\n",
    "        self.img_top= self.img_top.resize((1530,325),Image.ANTIALIAS)   #used to change high level image to low level image\n",
    "        self.photoimg_top=ImageTk.PhotoImage(self.img_top)\n",
    "        \n",
    "        f_lbl = Label(self.root,image=self.photoimg_top)\n",
    "        f_lbl.place(x=0,y=55,width=1530,height=325)\n",
    "        \n",
    "        #button\n",
    "        b1_1 =Button(self.root,text = \"Train Data\",command=self.train_classifier,cursor=\"hand2\",font=(\"times new roman\",20,\"bold\"),bg=\"red\",fg=\"white\")\n",
    "        b1_1.place(x=560,y=400,width=280,height=50)\n",
    "        \n",
    "        \n",
    "    def train_classifier(self):\n",
    "        data_dir=(\"data\")\n",
    "        path =[os.path.join(data_dir,file) for file in os.listdir(data_dir)]\n",
    "        \n",
    "        faces=[]\n",
    "        ids=[]\n",
    "        \n",
    "        for image in path:\n",
    "            img=Image.open(image).convert('L') #gray scale\n",
    "            imgNp=np.array(img,'unit8')\n",
    "            id=int(os.path.split(img)[1].split('.')[1])\n",
    "            \n",
    "            faces.append(imgNp)\n",
    "            ids.append(id)\n",
    "            cv2.imshow(\"Training\",imgNp)\n",
    "            cv2.waitket(1)==13\n",
    "        ids=np.array(ids)\n",
    "        \n",
    "        #=====================Train the classifiers============================\n",
    "        clf=cv2.face.LBPHFaceRecognizer_create()\n",
    "        \n",
    "        clf.train(faces,ids)\n",
    "        clf.write(\"classifier.xml\")\n",
    "        cv2.destroyAllWindows()\n",
    "        messagebox.show(\"Result\",\"Training datasets are completed\")\n",
    "            \n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "                                         \n",
    "                                         \n",
    "    root=Tk()\n",
    "    obj = Train(root)\n",
    "    root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c7bfecad",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
