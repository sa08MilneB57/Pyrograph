from tkinter import font as tkfont
import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *
import math,cmath,random,os,sys


#Allow users to save and load functions in text files

#Have UI class inherit from Tk() in tkinter and use UI as your "root"

#find out why "progress" in domain Gen is not displaying any changes


#_________CONSTANTS and GLOBALS____________
root = Tk() #Top Level Window Object
root.title("Graphs")
configFont = ('Courier','-18',"bold")
program_ver = "0.11" #Updated with any new code/upload to gitHub
file_ver = "0.1" #Updated with any new user config settings
py_ver = "3.5.1" #Updated whenever the code is tested on a newer version of Python


def domainGen(start,end,step):
    global progress
    #generates a list of points for t, x, or theta to be equal to.
    #Acts like a floating point equivalent to "range" except it generates an whole list object, not just an iterator
    domain = [] #creates an empty list to store the domain
    minInt = int(start//step) #rounding towards zero
    maxInt = int(end//step) #rounding towards zero
    for n in range(minInt-1,maxInt + 1): #The +/-1 is due to the way "range" works
        if n*step >= start and n*step <= end:
            domain.append(n*step)
    return domain

def getPrec(usr_input):#calculates the "decimal point precision" of a number stored in a string
    if '.' in usr_input:
        return len(usr_input) - usr_input.index('.') - 1
    else:
        return 0

def get_bin(x,n):
    #returns x as a binary in string form with minimum length n
    return format(x, 'b').zfill(n)

def search(find,string):
    #returns every index where "find" is located in "string" as a list
    result = []
    for c in range(len(string)):
        if string[c] == find:
            result.append(c)
    return result

#This stores all possible color names for tkinter to allow random color generation and user choice from comboboxes.
COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
          'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
          'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
          'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
          'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
          'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
          'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
          'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
          'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
          'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
          'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
          'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
          'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
          'indian red', 'saddle brown', 'sandy brown',
          'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
          'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
          'pale violet red', 'maroon', 'medium violet red', 'violet red',
          'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
          'thistle', 'snow2', 'snow3',
          'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
          'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
          'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
          'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
          'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
          'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
          'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
          'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
          'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
          'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
          'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
          'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
          'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
          'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
          'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
          'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
          'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
          'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
          'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
          'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
          'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
          'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
          'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
          'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
          'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
          'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
          'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
          'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
          'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
          'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
          'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
          'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
          'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
          'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
          'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
          'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
          'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
          'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
          'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
          'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
          'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
          'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
          'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
          'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
          'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
          'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
          'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
          'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
          'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
          'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
          'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
          'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
          'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
          'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
          'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
          'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
          'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']


#_______________________CLASSES________________________
class UI:
    def __init__(self,parent):#parent must be Tk() Object
        self.parent = parent
        self.real = Space(self,1600,1200,False,-40,40,-30,30,0,1,1,0) #space needs to be defined here so that menu commands can reffer to it
        
        #Menu Bar UI
        #   A pretty standard block of code that just defines some menus at the top, most of which are currently placeholders.
        
        self.bar = Menu(parent)
        parent.config(menu=self.bar)
        
        self.file = Menu(self.bar, tearoff=0)
        self.bar.add_cascade(label="File", menu=self.file)
        self.file.add_command(label="Clear Canvas", command=self.real.clearCanvas)
        self.file.add_command(label="Test Range", command=self.testRange)
        self.file.add_command(label="Vintage Project", command=self.doNothing)
        self.file.add_separator()
        self.file.add_command(label="Delete Project", command=self.doNothing)
        self.file.add_command(label="Exit Project", command=parent.destroy)
        
        self.edit = Menu(self.bar, tearoff=0)
        self.bar.add_cascade(label="Edit", menu=self.edit)
        self.edit.add_command(label="Cut", command=self.doNothing)
        self.edit.add_command(label="Copy", command=self.doNothing)
        self.edit.add_command(label="Paste", command=self.doNothing)
        
        #Space Placement
        #   Simply places the space into a space in the UI
        #   I would prefer to create the space here but the menu buttons need to be able to reference it and I would rather have the UI class written roughly in order of the widgets position.
        self.real.can.grid(row=0,column=0,rowspan=3,columnspan=6) #grids the space canvas into the window
        
        #Function Draw Config
        #   Sets up the buttons and entry boxes for function bounds and drawing options.
        self.controlSmooth = IntVar() #This is a control variable for the checkbutton
        self.controlFunkMin = StringVar() #These instantiate control variables for the text boxes contents
        self.controlFunkMax = StringVar()
        self.controlFunkStep = StringVar()

        self.labelFunkMin = Label(parent, text="Input Minimum") #These set up the labels
        self.labelFunkMax = Label(parent, text="Input Maximum")
        self.labelFunkStep = Label(parent, text="Input Step")
        self.labelSmooth = Label(parent, text="Smoothing:")
        self.entryFunkMin = Entry(parent,font=configFont, textvariable=self.controlFunkMin) #These set up entry boxes
        self.entryFunkMax = Entry(parent,font=configFont, textvariable=self.controlFunkMax)
        self.entryFunkStep = Entry(parent,font=configFont, textvariable=self.controlFunkStep)
        self.checkSmooth = Checkbutton(parent,variable=self.controlSmooth) #This is the smoothing checkbutton
        
        self.controlFunkMin.set("0") #This sets up default values for entry boxes
        self.controlFunkMax.set("2 * math.pi")
        self.controlFunkStep.set("0.01")
        
        self.labelFunkMin.grid(column=0,row=3)  #This block of code places the objects defined in the last block using "Grid"
        self.labelFunkMax.grid(column=1,row=3)
        self.labelFunkStep.grid(column=2,row=3)
        self.labelSmooth.grid(column=3,row=3)
        self.entryFunkMin.grid(column=0,row=4,sticky=W+E)
        self.entryFunkMax.grid(column=1,row=4,sticky=W+E)
        self.entryFunkStep.grid(column=2,row=4,sticky=W+E)
        self.checkSmooth.grid(column=4,row=3)
        
        
        #Explicit Functions UI
        #   Sets up the buttons and entry boxes for inputing explicit functions.
        self.controlFunkExp = StringVar()
        
        self.labelFunkExp = Label(parent, text="Function: y=")
        self.entryFunkExp = Entry(parent, font=configFont, textvariable=self.controlFunkExp) #Creates an input box in the window "root"
        self.btnFunkExp = Button(parent, text="Explicit Funk",command=self.real.drawFunkExp)
        self.btnPlusMinusExp = Button(parent, text="±",command=self.plusMinusExp)
        
        self.controlFunkExp.set("x**2") #This sets up default values for entry box
        
        self.labelFunkExp.grid(column=0,row=6)     #This block of code places the objects defined in the last block using "Grid"
        self.entryFunkExp.grid(column=1,row=6,columnspan=3,sticky=W+E)
        self.btnFunkExp.grid(column=5,row=6)
        self.btnPlusMinusExp.grid(column=4,row=6)
        
        
        #Parametric Functions UI
        #   Sets up the buttons and entry boxes for inputing parametric functions.
        self.controlFunkParX = StringVar()
        self.controlFunkParY = StringVar()
        
        self.labelFunkParY = Label(parent, text="Function: y(t)=")
        self.labelFunkParX = Label(parent, text="Function: x(t)=")
        self.entryFunkParX = Entry(parent, font=configFont, textvariable=self.controlFunkParX)
        self.entryFunkParY = Entry(parent, font=configFont, textvariable=self.controlFunkParY)
        self.btnFunkPar = Button(parent, text="Parametric Funk",command=self.real.drawFunkPar)
        self.btnPlusMinusParX = Button(parent, text="±",command=self.plusMinusParX)
        self.btnPlusMinusParY = Button(parent, text="±",command=self.plusMinusParY)
        
        self.controlFunkParX.set("25 * math.sin(t)")  #This sets up default values for entry boxes
        self.controlFunkParY.set("25 * math.cos(t)")
        
        self.labelFunkParY.grid(column=0,row=7,) #This block of code places the objects defined in the last block using "Grid"
        self.labelFunkParX.grid(column=0,row=8,)
        self.entryFunkParY.grid(column=1,row=7,columnspan=3,sticky=W+E)
        self.entryFunkParX.grid(column=1,row=8,columnspan=3,sticky=W+E)
        self.btnFunkPar.grid(column=5,row=7,rowspan=2)
        self.btnPlusMinusParX.grid(column=4,row=8)
        self.btnPlusMinusParY.grid(column=4,row=7)
        
    def testRange(self):
        beg=float(self.entryFunkMin.get())
        mid=float(self.entryFunkStep.get())
        end=float(self.entryFunkMax.get())
        print("beg: " + str(beg))
        print("mid: " + str(mid))
        print("end: " + str(end))
        print(domainGen(beg,end,mid))
        
    def doNothing(self):
        print(random.choice(["donuts","","coffee","42","Spaghetti"]))
        
    def funcNotFound(self):#displays a box asking the user to enter a function
        tkinter.messagebox.showinfo("You Gotta Get Funky", "Please Enter A Function")
        return True
    
    def plusMinusExp(self):
        self.entryFunkExp.insert(len(self.controlFunkExp.get()),"±")
        
    def plusMinusParX(self):
        self.entryFunkParX.insert(len(self.controlFunkParX.get()),"±")
        
    def plusMinusParY(self):
        self.entryFunkParY.insert(len(self.controlFunkParY.get()),"±")


class Space:
    def __init__(self,parent,pwidth,pheight,polar,xl,xr,yb,yt,mr,xgap,ygap,rgap):#parent must be of UI class
        self.parent = parent
        self.w = pwidth #pwidth= INT width of the Space in pixels
        self.h = pheight #pheight= INT height of the Space in pixels
        self.pol = polar #polar= BOOL is this Space using Polar coordinates? False=Cartesian
        self.minx = xl #xl= FLOAT Left boundary value of x
        self.maxx = xr #xr= FLOAT Right boundary value of x
        self.miny = yb #yb= FLOAT Bottom boundary value of y
        self.maxy = yt #yt= FLOAT top boundary value of y
        self.maxr = mr #mr= FLOAT boundary value of r (polar coords)
        self.resx = xgap #xgap= FLOAT number of units per minor axis gridline on x axis, set to 0 to remove gridlines
        self.resy = ygap #ygap= FLOAT number of units per minor axis gridline on y axis, set to 0 to remove gridlines
        self.resr = rgap #ygap= FLOAT number of units per minor axis gridline on y axis, set to 0 to remove gridlines
        self.dx = pwidth/(xr-xl) #number of pixels per unit of x coordinates
        self.dy = pheight/(yt-yb) #number of pixels per unit of y coordinates
        self.px = (xr-xl)/pwidth #number of units per pixel (More accurate than 1/dx for hardware reasons)
        self.py = (yt-yb)/pheight #number of units per pixel (More accurate than 1/dy for hardware reasons)
        self.can =	Canvas(parent.parent,width=pwidth,height=pheight,relief=GROOVE,bg="snow",borderwidth=2)#creates a canvas object on which to draw everything
        self.xcoord = [] #creates an empty list to store the x axis real coordinates of tickmarks and minor gridlines
        self.minIntX = int(self.minx/self.resx) #rounding towards zero, this calculates the number of negative minor gridlines
        self.maxIntX = int(self.maxx/self.resx) #rounding towards zero, this calculates the number of positive minor gridlines
        for n in range(self.minIntX,self.maxIntX + 1): #The +1 is due to the way "range" treats the last number
            if n==0:
                pass
            else:
                self.xcoord.append(n*self.resx)
        self.ycoord = [] #creates an empty list to store the y axis real coordinates of tickmarks and minor gridlines

        self.minIntY = int(self.miny/self.resy) #rounding towards zero, this calculates the number of negative minor gridlines
        self.maxIntY = int(self.maxy/self.resy) #rounding towards zero, this calculates the number of positive minor gridlines
        for n in range(self.minIntY,self.maxIntY + 1): #The +1 is due to the way "range" treats the last number
            if n==0:
                pass
            else:
                self.ycoord.append(n*self.resy)
        self.minax = MinorAxes(self) #object that stores and calls the minor axes (called before major so that the major axes are drawn "above" the minor ones)
        self.majax = MajorAxes(self) #object that stores and calls the major axes
        self.axlbls = TickLabels(self) #object that stores and calls the TickLabels object for displaying numbers by the axes
        self.funkList = [] #creates an empty list to store functions
    
    #Coordinate Conversion Functions
    def coordPxl(self,xcoord,ycoord): #input a real coordinate, returns a pixel location as a list object
        pixelx = int((xcoord - self.minx) * self.dx)
        pixely = int(self.h - ((ycoord - self.miny) * self.dy))
        return [pixelx,pixely]
    
    def pxlCoord(self,xPxl,yPxl): #input a pixel location, returns a real coordinate as a list object
        coordx = (xPxl / self.dx) + self.minx
        coordy = ((self.h-yPxl)/dy) + self.miny
        return [coordx,coordy]
    
    def polPxl(self,r,theta): #input a polar coordinate, returns a pixel location 
        pass #polar update pending
    
    def pxlPol(self,x,y): #input a pixel location, returns a polar coordinate
        pass #polar update pending
    
    #Line drawing functions
    def drawFunkExp(self):
        if "±" in self.parent.entryFunkExp.get():
            for f in iterateFunk(self.parent.entryFunkExp.get()):
                self.funkList.append(Funk(self,"exp",self.parent.controlSmooth,exp = f))
        else:
            self.funkList.append(Funk(self,"exp",self.parent.controlSmooth,exp = self.parent.entryFunkExp.get()))
    
    def drawFunkPar(self):
        if "±" in self.parent.entryFunkParX.get() or "±" in self.parent.entryFunkParY.get():
            fpairs = tuple(itertools.product(iterateFunk(self.parent.entryFunkParX.get()),iterateFunk(self.parent.entryFunkParY.get())))
            for fp in range(len(fpairs)):
                self.funkList.append(Funk(self,"par",self.parent.controlSmooth,parX = fpairs[fp][0],parY = fpairs[fp][1]))
        else:
            self.funkList.append(Funk(self,"par",self.parent.controlSmooth,parX = self.parent.entryFunkParX.get(),parY = self.parent.entryFunkParY.get()))
    
    #Plus Minus functionality
    def iterateFunk(funk):
        length = funk.count("±") #this stores the length of the binary numbers used to calculate possible combinations
        combinations = 2**length #this is the total number of binary combinations of +s and -s
        str_index = search("±",funk)
        orders = [] #instantiates empty list for storing all the binary combinations
        new_funks = [] #instantiates empty list for storing all the new functions generated
        for i in range(combinations):
            orders.append(get_bin(i,length))#adds a binary number to "orders" from 0 to 2**length
        for o in orders: #loops through every possible order
            track_o = list(o) #copies the current order as a list into temporary variable
            list_funk = list(funk) #copies the function as a list into temporary variable
            for i in range(length): #iterates over each ± sign
                if int(track_o.pop(0)) == 0:#0 replaces it with +, 1 replaces it with a -
                    list_funk[int(str_index[i])] = "+"
                else:
                    list_funk[int(str_index[i])] = "-"
            new_funks.append("".join(list_funk))
        return new_funks
    
    #Clear the canvas of lines    
    def clearCanvas(self):
        for f in self.funkList:
            self.can.delete(f.line)
        self.funkList = []


class Point: #this class is used to draw points on the canvas
    def __init__(self,parent,xtheta,yr):#parent must be a "Space" object, the other two args specify coordinates
        self.parent = parent
        if parent.pol == True:#this function calls different functions in polar coordinates but is ultimately the same
            pass
        else:
            xcenter,ycenter = parent.coordPxl(xtheta,yr)
            self.hor = parent.can.create_line(xcenter-11,ycenter,xcenter+12,ycenter)
            self.vert = parent.can.create_line(xcenter,ycenter+11,xcenter,ycenter-12)
            self.rndl = parent.can.create_oval(xcenter-8,ycenter+8,xcenter+8,ycenter-8,outline="red")
            self.lbl = parent.can.create_text(xcenter,ycenter+20,text=str([xtheta,yr]),font = configFont)


class MajorAxes: #this is the primary X and Y axes gridlines (see minor for the faded lines)
    def __init__(self,parent): #parent must be a "Space" object
        self.parent = parent
        xorig,yorig = parent.coordPxl(0,0)#calculates the coordinates of the origin
        self.xaxis = parent.can.create_line(0,yorig,parent.w,yorig,width=2) #creates x axis from the leftmost pixel to the rightmost
        self.yaxis = parent.can.create_line(xorig,0,xorig,parent.h,width=2) #creates x axis from the topmost pixel to the bottommost


class MinorAxes: #this object is the minor axis gridlines (the faded ones)
    def __init__(self,parent):#parent must be a "Space" object
        self.parent = parent
        if parent.pol == True:#this function behaves differently depending on whether the Space is using polar coordinates
            pass #polar update pending
        else:
            if parent.resx == 0:#set xgap of your space to 0 to remove gridlines
                pass
            else:
                self.xaxes = [] #creates an empty list object to store the y oriented axis lines marking off the x axis
                for i in parent.xcoord:
                    pxl = parent.coordPxl(i,0)
                    self.xaxes.append(parent.can.create_line(pxl[0],0,pxl[0],parent.h,fill="gray80"))
                    
            if parent.resy == 0:#set ygap of your space to 0 to remove gridlines
                pass
            else:
                self.yaxes = [] #creates an empty list object to store the x oriented axis lines marking off the y axis
                for i in parent.ycoord:
                    pxl = parent.coordPxl(0,i)
                    self.yaxes.append(parent.can.create_line(0,pxl[1],parent.w,pxl[1],fill="gray80"))
 
                
class TickLabels: #this is the numbered labels for axes.
    def __init__(self,parent):#parent must be a "Space" object
        self.parent = parent
        self.org = parent.coordPxl(0,0)
        if parent.resx == 0:#set xgap of your space to 0 to remove tick labels
            pass
        else:
            self.xlbls = [] #creates an empty list object to store the x axis number labels
            self.xmarks = [] #creates an empty list for the tick mark objects
            botPxl = self.org[1] + 6
            topPxl = self.org[1] - 6
            for i in parent.xcoord:
                xPxl = parent.coordPxl(i,0)
                self.xmarks.append(parent.can.create_line(xPxl[0],topPxl,xPxl[0],botPxl,width=2))
                
        if parent.resy == 0:#set ygap of your space to 0 to remove tick labels
            pass
        else:
            self.ylbls = [] #creates an empty list object to store the x axis number labels
            self.xmarks = [] #creates an empty list for the tick mark objects
            lftPxl = self.org[0] - 6
            rgtPxl = self.org[0] + 6
            for i in parent.ycoord:
                yPxl = parent.coordPxl(0,i)
                self.ylbls.append(parent.can.create_line(lftPxl,yPxl[1],rgtPxl,yPxl[1],width=2))
                
                
class Funk:#this class stores and draws functions on the space
    def __init__(self,parent,type,smooth,exp="",parX="",parY=""):
        #parent must be a space object
        #type is a string defining whether the function is explicit"exp" or parametric"par"
        #funk is a string containing the expression of the function
        # **functions represents the keyword arguments
        self.funk = str(exp) #string expression of function
        self.funkX = str(parX) #string expression of parametric X function
        self.funkY = str(parY) #string expression of parametric Y function
        self.pxls = [] #defines an empty list to store the pixel coordinates of the lines
        self.coordsX = [] #defines an empty list to store the X coordinates
        self.coordsY = [] #defines an empty list to store the Y
        try:
            beg=eval(parent.parent.entryFunkMin.get())
            mid=eval(parent.parent.entryFunkStep.get())
            end=eval(parent.parent.entryFunkMax.get())
        except:
             tkinter.messagebox.showinfo("Boundin'", "There's something wrong with your bounds.")
             raise
        if type == "exp":
            #funk = parent.parent.entryFunkExp.get()            #commented out to test plus/minus functionality
            for c in domainGen(beg,end,mid):
                x = c
                self.coordsX.append(x)
                try:
                    self.coordsY.append(eval(self.funk))
                except ZeroDivisionError:
                    x = x - 0.0001
                    self.coordsY.append(eval(self.funk))
                    x = c
                    self.coordsX.append(x)
                    x = x +0.0001
                    self.coordsY.append(eval(self.funk))
        elif type == "par":
            #funkX = parent.parent.entryFunkParX.get()          #commented out to test plus/minus functionality
            #funkY = parent.parent.entryFunkParY.get()          #commented out to test plus/minus functionality
            for c in domainGen(beg,end,mid):
                t = c
                try:
                    self.coordsX.append(eval(self.funkX))
                    self.coordsY.append(eval(self.funkY))
                except ZeroDivisionError:
                    t = c - 0.0001
                    self.coordsX.append(eval(self.funkX))
                    self.coordsY.append(eval(self.funkY))
                    t = c +0.0001
                    self.coordsX.append(eval(self.funkX))
                    self.coordsY.append(eval(self.funkY))

        for x,y in zip(self.coordsX,self.coordsY):
            pxlX, pxlY = parent.coordPxl(x,y)
            self.pxls.append(pxlX)
            self.pxls.append(pxlY)
        if smooth == 0:
            self.line = parent.can.create_line(*self.pxls,smooth=False)
        else:
            self.line = parent.can.create_line(*self.pxls,smooth=True)
        
        
        
#___________________________SCRIPT______________________


ui = UI(root)

root.mainloop()






























