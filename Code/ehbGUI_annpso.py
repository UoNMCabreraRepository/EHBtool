# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:17:47 2022

@author: evxmc3
"""


import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Notebook, Style

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon

import joblib
import math
import os

from PIL import ImageTk
import sys 
from tkinter import scrolledtext
from tkinter import messagebox

path='C:/Users/evxmc3/exe/Packing'

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

concr_value=[]

Height=450
Width=700
respacing=0.08

#frame 1
frame1_rewidth=.65
entry_width=.25
text_height=.07

def getValue(event):

    thickness=int(300/int(slend_scale.get()))
        
    diam_value=int(diam_scale.get())
    diam_vlabel['text']="{:.1f}".format(diam_value)
    
    sha_value=int(sha_scale.get())
    sha_vlabel['text']="{:.1f}".format(sha_value)
     
    bg_value=float(bg_scale.get())
    if bg_value ==8:
        bg_vlabel['text']=8.8
    else:
        bg_vlabel['text']=10.9
       
    gaug_value=int(gaug_scale.get())   
    gaug_vlabel['text']="{:.1f}".format(gaug_value)
    
    concr_value=int(concr_scale.get())
    concr_vlabel['text']="{:.1f}".format(concr_value)
    
    slend_value=int(slend_scale.get())
    slend_vlabel['text']="{:.1f}".format(slend_value)
    
    thick_label2['text']="{:.1f}".format(thickness)

    graph(slend_scale.get(), sha_scale.get(),gaug_scale.get(), diam_scale.get(),concr_scale.get(),bg_scale.get())
    a.cla()  
    
    #clean o8utput if inputs are changed
    outfail_label['text']=''
    outstif_label['text']=''
    outstre_label['text']=''
    detail_label['text']=''

    
def graph(slend_entry, sha_entry, gaug_entry,diam_entry,concr_entry,bg_entry):
    labelframe2=ttk.LabelFrame(root, text=" Drawing ")
    labelframe2.place(relx=0.5, rely=0.04, relwidth=.46, relheight=.51)
      
    thickness=int(300/int(slend_entry))
    graph_thickness=float(thickness)/3
    graph_shank=(int(sha_entry))/(-0.0425*(int(sha_entry))+9.375)
    graph_gauge=int(gaug_entry)
    graph_diameter=int(diam_entry)/(-0.125*int(diam_entry)+4)
             
    # coordinates
    t_coord = [[260+graph_thickness,115],[275+graph_thickness,115],[275+graph_thickness,285],[400,285],[400,315],[275+graph_thickness,315],[275+graph_thickness,485],[260+graph_thickness,485]]
    ar_coord=[[430,295],[475,295],[475,275],[500,300],[475,325],[475,305],[430,305],[430,295]]
    
    #           1                        2                                          3                                                           4                                                            5                                                          6                                                            7                                          8                          9                          10                                        11                                                     12                                                       13                                                        14                                                     15                                                        16                                                      17
    B1_coord=[[260,300+graph_gauge/2-15],[275+graph_thickness,300+graph_gauge/2-15],[275+graph_thickness,300-30+graph_gauge/2-graph_diameter/2],[285+graph_thickness,300-30+graph_gauge/2-graph_diameter/2],[285+graph_thickness,300+graph_gauge/2+30+graph_diameter/2],[275+graph_thickness,300+graph_gauge/2+30+graph_diameter/2], [275+graph_thickness,300+graph_gauge/2+15],[260,300+graph_gauge/2+15],[230,300+graph_gauge/2+30],[230,300+graph_gauge/2+graph_diameter],[230-graph_shank/2,300+graph_gauge/2+graph_diameter],[230-graph_shank/2,300+graph_gauge/2+15+graph_diameter/2],[220-graph_shank/2,300+graph_gauge/2+15+graph_diameter/2],[220-graph_shank/2,300+graph_gauge/2-15-graph_diameter/2],[230-graph_shank/2,300+graph_gauge/2-15-graph_diameter/2],[230-graph_shank/2,300+graph_gauge/2-graph_diameter] ,[230,300+graph_gauge/2-graph_diameter],[230,300+graph_gauge/2-30],  [260,300+graph_gauge/2-15]]
    B2_coord=[[260,300-graph_gauge/2-15],[275+graph_thickness,300-graph_gauge/2-15],[275+graph_thickness,300-30-graph_gauge/2-graph_diameter/2],[285+graph_thickness,300-30-graph_gauge/2-graph_diameter/2],[285+graph_thickness,300-graph_gauge/2+30+graph_diameter/2],[275+graph_thickness,300-graph_gauge/2+30+graph_diameter/2], [275+graph_thickness,300-graph_gauge/2+15],[260,300-graph_gauge/2+15],[230,300-graph_gauge/2+30],[230,300-graph_gauge/2+graph_diameter],[230-graph_shank/2,300-graph_gauge/2+graph_diameter],[230-graph_shank/2,300-graph_gauge/2+15+graph_diameter/2],[220-graph_shank/2,300-graph_gauge/2+15+graph_diameter/2],[220-graph_shank/2,300-graph_gauge/2-15-graph_diameter/2],[230-graph_shank/2,300-graph_gauge/2-15-graph_diameter/2],[230-graph_shank/2,300-graph_gauge/2-graph_diameter] ,[230,300-graph_gauge/2-graph_diameter],[230,300-graph_gauge/2-30],  [260,300-graph_gauge/2-15]]
    
    a.axis('off')
    a.set_ylim([0,600])
    a.set_xlim([0,500])

    #T drawing
    t_stub = Polygon(t_coord, facecolor = '#a3170b')
    a.add_patch(t_stub)
    
    #Arrow drawing
    arrow = Polygon(ar_coord, facecolor = 'k')
    a.add_patch(arrow)
       
    alpha=int(concr_entry)/100

    #SHS drawing
    a.add_patch(Rectangle((30, 95), 230, 410,         
             facecolor = '#b8b8b8',
             alpha=alpha,
             fill=True,
             lw=0))
    
    #SHS drawing
    a.add_patch(Rectangle((30, 95), 230, 410,           
             edgecolor = 'gray',
             fill=False,
             lw=graph_thickness))
    
    #Bolts drawing
    if bg_entry==10.0:
        Bcolor='#606060'
    else:
        Bcolor='#808080'
        
    B1 = Polygon(B1_coord, edgecolor='k',facecolor = Bcolor, linewidth=.5)
    a.add_patch(B1)   
    B2 = Polygon(B2_coord, edgecolor='k',facecolor = Bcolor,linewidth=.5)
    a.add_patch(B2)

    a.text(485, 370, 'F', horizontalalignment='center', verticalalignment='center')
    dataPlot = FigureCanvasTkAgg(f, master=labelframe2)
    dataPlot.get_tk_widget().pack(fill='both')     
    dataPlot.draw()
    
 
def Norm(param,value):
    
    if param=='Diameter':
        str_min=16.00
        str_max=20.00
    elif param=='Shank':
        str_min=150.00
        str_max=190.00
    elif param=='Grade':
        str_min=8.00
        str_max=10.00
    elif param=='Gauge':
        str_min=80.00
        str_max=180.00
    elif param=='Concrete':
        str_min=20.00
        str_max=82.33
    elif param=='Slenderness':
        str_min=18.00
        str_max=47.00
    
    norm=0.1+(((value-str_min)*(0.9-0.1))/(str_max-str_min))
    return norm

def BackNorm(param,value):

    if param=='Strength':
        str_min=165.302
        str_max=389.300
    elif param=='Stiffness':
        str_min=69.786
        str_max=434.066
    elif param=='Coldisp':
        str_min=0.160
        str_max=13.564
  
    backnorm=((value-0.1)/(0.9-0.1))*(str_max-str_min)+str_min
    return backnorm

def Pred_func(diam_scale,sha_scale,bg_scale,gaug_scale,concr_scale,slend_scale):
    
    diameter=Norm('Diameter',float(diam_scale))
    shank=Norm('Shank', float(sha_scale))
    
    if bg_scale==8.8:
        bg_scale=8.0
    elif bg_scale==10.9:
        bg_scale=10.0
        
    grade=Norm('Grade', float(bg_scale))
    gauge=Norm('Gauge', float(gaug_scale))
    concrete=Norm('Concrete', float(concr_scale))
    
    slend=slend_scale
    slenderness=Norm('Slenderness',float(slend))
    
    inputs=[[diameter, shank, grade, gauge, concrete, slenderness]]
    
    #Strength prediction
    annpso_strength_model = joblib.load(resource_path('finalised_ANNpso_Strength_model.pkl'))   
    annpso_strength_predict = annpso_strength_model.predict(inputs)
    strength_value=BackNorm('Strength',float(annpso_strength_predict) )      
    outstre_label['text']="{:.2f}".format(strength_value)
    
    #Stiffness prediction
    annpso_stiffness_model = joblib.load(resource_path('finalised_ANNpso_Stiffness_model.pkl'))   
    annpso_stiffness_predict = annpso_stiffness_model.predict(inputs)
    stiffness_value=BackNorm('Stiffness',float(annpso_stiffness_predict) )      
    outstif_label['text']="{:.2f}".format(stiffness_value)
    
    #Failure prediction
    annpso_coldispl_model = joblib.load(resource_path('finalised_ANNpso_Coldisp_model.pkl'))   
    annpso_coldispl_predict = annpso_coldispl_model.predict(inputs)
    coldispl_value=BackNorm('Coldisp',float(annpso_coldispl_predict) )
    
    outcoldispl_label['text']=coldispl_value  
    
    if coldispl_value >=3:
        failure='Column'
        failure_detail='column failure in bending'
    elif coldispl_value <3 and coldispl_value>1.5:
        failure='Combined'
        failure_detail='combined failure'
    else:
        failure='Bolt'  
        failure_detail='bolts fracture'
        #failure_details='This failure mode is characterised by negligible column wall deformation (<1mm), light to no concrete cracking, and bolt fracture.'
    
    outfail_label['text']=failure    
    detail_label['text']=failure_detail    
    

def ValWindow(param,label,failure):
    pred_value=[]
    unit=[]
    
    fig=plt.figure(str(param)+" validation")

    if failure=='':
        messagebox.showerror('Calculation Error', 'Error: Calculation is required first.')
        plt.close()
        return
        
    fig.show()
    ax=fig.add_subplot(111)
    
    
    if param=='Strength':
        pred_value=float(outstre_label.cget("text"))
        unit=' (kN)'
        R=0.995

    elif param=='Stiffness':
        pred_value=float(outstif_label.cget("text"))
        unit=' (kN/mm)'
        R=0.983

    else:
        pred_value=float(outcoldispl_label.cget("text"))
        unit=' (mm)'
        R=0.979
        ax.add_patch(Rectangle((0, 0), 1.5, 1.5, edgecolor='darkorange' ,         
         fill=False))
        ax.add_patch(Rectangle((1.5, 1.5), 1.5, 1.5,  edgecolor='m',         
         fill=False))
        ax.add_patch(Rectangle((3, 3), 11, 11, edgecolor='g',      
         fill=False))
        plt.text(13.1,3,"III")
        plt.text(3.1,1.5,"II")
        plt.text(1.6,0,"I")
        ax.title.set_text('Failure I: Bolt, II: Combined, III: Column')

    per_xerror=(1-R)
    xerror=pred_value*per_xerror
  
    filename= resource_path(str(param)+"_val_annpso.txt")   
    dataset = open( filename, 'r' ).readlines()  
    
    x, y = [], []

    for line in dataset:
        x.append(float(line.split()[0]))
        y.append(float(line.split()[1]))
        
    min_x=round(math.floor(min(x)))
    max_x=round(math.ceil(max(x)))

    ax.plot([min_x,max_x],[min_x,max_x], 'k--')
    ax.plot(x, y, 's', label='validation values') 
    ax.set_xlabel('Experimental '+str(param)+ str(unit))
    ax.set_ylabel('Predicted '+str(param)+ str(unit))

    ax.plot(pred_value,pred_value, 'sr', label='prediction value')
    plt.errorbar(pred_value,pred_value, color='r', ecolor='r', xerr=xerror, xuplims=True, xlolims=True,  label='error bar')
    plt.legend(loc='lower right')
    plt.text((min_x),(max_x)*.95,"$R^2= $"+str(R))
    plt.draw()

def Ilustration(failure):
    
    illustrationWindow = tk.Toplevel()
    illustrationWindow.title('Failure Illustration')
    illustrationWindow.geometry("652x320")
    
    if failure=='':
        messagebox.showerror('Calculation Error', 'Error: Calculation is required first.')
        illustrationWindow.destroy()
        return
  
    canvas = tk.Canvas(illustrationWindow, width = 365, height = 320, bg='white')  
    canvas.pack(side ='left') 
       
    filename=resource_path(str(failure)+".gif")
    img = ImageTk.PhotoImage(file=filename)
    canvas.create_image(10, 10, image=img, anchor='nw')
    canvas.img = img
 
    if  failure=='Column':
        failure_detail='Column failure in bending'
        failure_description="""This failure mode is characterised first by concrete tensile cracks and crushing. As the load is increased, the force is transmitted to the column tube wall by bolt sleeve bearing. Large column deformation is characteristic with bolt slippage out of the pre-drilled holes with no bolt fracture. \n\nThis failure mode is usually defined by a weak-column/strong-bolt configuration. \n\nConcrete crushing followed by tube wall yielding may be regarded as the preferred failure mode. \n\nIn order to change this failure mode, one of the following options or a combination of them could be adopted: \n+ increasing the slenderness ratio \n+ increasing the concrete strength \n+ increasing the gauge distance"""
    elif failure=='Combined':
        failure_detail='Combined failure'
        failure_description="""Combined failure mode is characterised by column deformation of less than 3mm and usually accompanied by sleeve fracture. Similar to column wall failure, concrete crushing is observed at the beginning of the curve, as the load is increased, it is transferred to the tube wall by the sleeves. \n\nIn this case, large column deformation is limited by the properties of the tube, as this is no longer the weakest component, high concentration of stress occur in the contact area between the pre-drilled holes and the sleeves, causing the sleeves to fracture. This failure mode could also present bolt elongation."""
    else:
        failure_detail='Bolts fracture'
        failure_description="""Bolt failure mode is characterised by negligible column wall deformation (<1mm), light to no concrete cracking, and bolt fracture. This failure mode is usually defined by a strong-column/weak-bolt configuration. \n\n This failure mode miay not be desirable as the bolts usually fracture abruptly. Concrete crushing followed by tube wall yielding may be regarded as the preferred failure mode. \n\nIn order to change this failure mode, one of the following options or a combination of them could be adopted: \n+ incresing the column wall slenderness ratio \n+ increasing the bolt diameter \n- decreasing the concrete strength \n- decreasing the gauge distance
        """ 
    
    text = scrolledtext.ScrolledText(illustrationWindow, width=36, height=19.4, wrap = tk.WORD, font = ("Helvetica", 10)) 
    text.place(relx=0.57, rely=0.02) 
    text.tag_configure('big', font=('Helvetica', 11, 'bold'))
    text.insert(tk.END, failure_detail,'big')
    text.insert(tk.END, '\n')
    text.insert(tk.END, '\n')
    text.insert(tk.END, failure_description)
    
def About():
    
    aboutWindow = tk.Toplevel()
    aboutWindow.title('About')
    aboutWindow.geometry("460x170")
    
    canvas = tk.Canvas(aboutWindow)  
    canvas.pack() 
    
    aboutLabel = tk.Label(aboutWindow, width=61, height=9, text='Version 0.0.1 January 2023 \n\n Developed by Manuela Cabrera Duran \n\n Submitted in part consideration of the degree of PhD in Civil Engineering \n Centre for Structural Engineering and Informatics (CSEI) \n Faculty of Engineering, University of Nottingham \n\n All rights reserved') 
    aboutLabel.place(relx=0.03, rely=0.07) 




"---"
root=tk.Tk()
root.title('EHB connection tool')

#Style settings
style=ttk.Style()
style.theme_use()
style.configure('TLabelframe', background='white')
style.configure('TLabelframe.Label', background='white')
style.configure('TLabel', background='white')
style.configure('TScale', background='white')
style.configure('TNotebook', background='white')
style.configure('TFrame', background='white')


canvas=tk.Canvas(root, height=Height, width=Width, bg='white')
canvas.pack()

diam_vlabel=tk.Label()
diam_scale=ttk.Scale()
sha_vlabel=tk.Label()
sha_scale=ttk.Scale()
bg_vlabel=tk.Label()
bg_scale=ttk.Scale()
gaug_vlabel=tk.Label()
gaug_scale=ttk.Scale()
concr_vlabel=tk.Label()
concr_scale=ttk.Scale()
thick_vlabel=tk.Label()
thick_scale=ttk.Scale()



""""Input"""

labelframe1=ttk.LabelFrame(root, text=" Design parameters ", style="TLabelframe")
labelframe1.place(relx=0.04, rely=0.04, relwidth=.42, relheight=.81)

label=ttk.Label(labelframe1, text='User defined',  anchor='w')
label.place(relx=0.03, rely=0.02, relwidth=.3,relheight=text_height)

diam_label=ttk.Label(labelframe1, text='Bolt diameter (mm)',  anchor='w' )
diam_label.place(relx=0.03, rely=0.02+respacing, relwidth=frame1_rewidth, relheight=text_height)

diam_scale = tk.Scale(labelframe1, from_=16, to=20, variable=concr_value, orient = 'horizontal', resolution=4, showvalue='off', troughcolor='white', sliderlength=12, sliderrelief='flat',activebackground='#007AD9',highlightthickness=0, bg='#deddd9',borderwidth=.5)
diam_scale.set(16.0)
diam_scale.place(relx=frame1_rewidth+.08, rely=0.03+respacing, relwidth=entry_width-.02)

diam_vlabel=tk.Label(labelframe1, text='16.0', anchor='w', bg='white')
diam_vlabel.place(relx=frame1_rewidth-.04, rely=0.02+respacing)


bg_label=ttk.Label(labelframe1, text='Bolt grade (unitless)',  anchor='w' )
bg_label.place(relx=0.03, rely=0.02+2*respacing, relwidth=frame1_rewidth, relheight=text_height)

bg_scale = tk.Scale(labelframe1, from_=8.8, to=10.9, variable=concr_value, orient = 'horizontal', resolution=2, showvalue='off', troughcolor='white', sliderlength=12, sliderrelief='flat',activebackground='#007AD9',highlightthickness=0, bg='#deddd9',borderwidth=.5)
bg_scale.set(8.8)
bg_scale.place(relx=frame1_rewidth+.08, rely=0.02+2*respacing, relwidth=entry_width-.02)

bg_vlabel=tk.Label(labelframe1, text='8.8', anchor='w', bg='white')
bg_vlabel.place(relx=frame1_rewidth-.04, rely=0.02+2*respacing)


sha_label=ttk.Label(labelframe1, text='Shank length (mm)',  anchor='w' )
sha_label.place(relx=0.03, rely=0.02+3*respacing, relwidth=frame1_rewidth, relheight=text_height)

sha_scale = ttk.Scale(labelframe1, from_=150, to=190, variable=concr_value, orient = 'horizontal')
sha_scale.set(170.0)
sha_scale.place(relx=frame1_rewidth+.08, rely=0.02+3*respacing, relwidth=entry_width-.02, relheight=.06)

sha_vlabel=tk.Label(labelframe1, text='170.0', anchor='w', bg='white')
sha_vlabel.place(relx=frame1_rewidth-.04, rely=0.02+3*respacing)


gaug_label=ttk.Label(labelframe1, text='Gauge distance (mm)',  anchor='w' )
gaug_label.place(relx=0.03, rely=0.02+4*respacing, relwidth=frame1_rewidth, relheight=text_height)

gaug_scale = ttk.Scale(labelframe1, from_=80, to=180, variable=concr_value, orient = 'horizontal')
gaug_scale.set(130.0)
gaug_scale.place(relx=frame1_rewidth+.08, rely=0.02+4*respacing, relwidth=entry_width-.02, relheight=.06)

gaug_vlabel=tk.Label(labelframe1, text='130.0', anchor='w', bg='white')
gaug_vlabel.place(relx=frame1_rewidth-.04, rely=0.02+4*respacing)
    
concr_label=ttk.Label(labelframe1, text='Concrete strength (MPa)',  anchor='w' )
concr_label.place(relx=0.03, rely=0.02+5*respacing, relwidth=frame1_rewidth, relheight=text_height)

concr_scale = ttk.Scale(labelframe1, from_=20, to=80, variable=concr_value, orient = 'horizontal')
concr_scale.set(50.0)
concr_scale.place(relx=frame1_rewidth+.08, rely=0.02+5*respacing, relwidth=entry_width-.02, relheight=.06)

concr_vlabel=tk.Label(labelframe1, text='50.0', anchor='w', bg='white')
concr_vlabel.place(relx=frame1_rewidth-.04, rely=0.02+5*respacing)

slend_label=ttk.Label(labelframe1, text='Slenderness ratio (unitless)',  anchor='w' )
slend_label.place(relx=0.03, rely=0.02+6*respacing, relwidth=frame1_rewidth, relheight=text_height)

slend_scale = ttk.Scale(labelframe1, from_=18.8, to=47.6, variable=concr_value, orient = 'horizontal')
slend_scale.set(33.2)
slend_scale.place(relx=frame1_rewidth+.08, rely=0.02+6*respacing, relwidth=entry_width-.02, relheight=.06)

slend_vlabel=tk.Label(labelframe1, text='11.0', anchor='w', bg='white')
slend_vlabel.place(relx=frame1_rewidth-.04, rely=0.02+6*respacing)

thick_label=ttk.Label(labelframe1, text='Tube thickness (mm)',  anchor='w' )
thick_label.place(relx=0.03, rely=0.02+7*respacing, relwidth=frame1_rewidth, relheight=text_height)

thick_label2=ttk.Label(labelframe1,  anchor='w', text='27.3' )
thick_label2.place(relx=frame1_rewidth-.04, rely=0.02+7*respacing, relwidth=entry_width, relheight=text_height)

diam_scale.configure(command=getValue)
bg_scale.configure(command=getValue)
sha_scale.configure(command=getValue)
gaug_scale.configure(command=getValue)
concr_scale.configure(command=getValue)
slend_scale.configure(command=getValue)

#---
separator = ttk.Separator(labelframe1)
separator.place(rely=0.02+8.5*respacing, relx=0.03, relwidth=.92)

fixed_label=ttk.Label(labelframe1, text='Fixed',  anchor='w')
fixed_label.place(relx=0.03, rely=0.02+9*respacing, relwidth=.3, relheight=text_height)

tube_label=ttk.Label(labelframe1, text='Square section dimension',  anchor='w' )
tube_label.place(relx=0.03, rely=0.02+10*respacing, relwidth=frame1_rewidth, relheight=text_height)

tube_label2=ttk.Label(labelframe1, text='300mm', anchor='w')
tube_label2.place(relx=frame1_rewidth+.04, rely=0.02+10*respacing, relwidth=entry_width, relheight=text_height)

tubed_label=ttk.Label(labelframe1, text='Tubular section steel',  anchor='w' )
tubed_label.place(relx=0.03, rely=0.02+11*respacing, relwidth=frame1_rewidth, relheight=text_height)

tubed_label2=ttk.Label(labelframe1, text='S355', anchor='w')
tubed_label2.place(relx=frame1_rewidth+.04, rely=0.02+11*respacing, relwidth=entry_width, relheight=text_height)



"""Notebook"""

notebook = ttk.Notebook(root)
notebook.place(relx=0.5, rely=0.60, relwidth=.46, relheight=.25)

#Tab1
notebookTab1 = ttk.Frame(notebook)
notebook.add(notebookTab1, text=' Calculation ')

fail_label=ttk.Label(notebookTab1, text='Connection failure mode',  anchor='w' )
fail_label.place(relx=0.02, rely=0.1, relwidth=.6, relheight=.2)

outfail_label=ttk.Label(notebookTab1, anchor='w')
outfail_label.place(relx=.65, rely=0.1)

outcoldispl_label=ttk.Label(notebookTab1, anchor='w')

stre_label=ttk.Label(notebookTab1, text='Connection strength (kN)',  anchor='w' )
stre_label.place(relx=0.02, rely=0.4, relwidth=.6, relheight=.2)

outstre_label=ttk.Label(notebookTab1, anchor='w')
outstre_label.place(relx=.65, rely=.4)

stif_label=ttk.Label(notebookTab1, text='Connection stiffness (kN/mm)',  anchor='w' )
stif_label.place(relx=0.02, rely=0.7, relwidth=.6, relheight=.2)

outstif_label=ttk.Label(notebookTab1, anchor='w')
outstif_label.place(relx=.65, rely=.7)


#Tab2
notebookTab2 = ttk.Frame(notebook)
notebook.add(notebookTab2, text=' Validation ')

valid_label=ttk.Label(notebookTab2, text='Plot validation graphs:',  anchor='w' )
valid_label.place(relx=0.03, rely=0.16)

button=ttk.Button(notebookTab2, text='Strength', command=lambda: ValWindow('Strength',outstre_label.cget("text"),outfail_label.cget("text")))
button.place(relx=.03, rely=.52, relwidth=.3)

button=ttk.Button(notebookTab2, text='Stiffness', command=lambda: ValWindow('Stiffness',outstif_label.cget("text"),outfail_label.cget("text")))
button.place(relx=.35, rely=.52, relwidth=.3)

button=ttk.Button(notebookTab2, text='Failure', command=lambda: ValWindow('Column displacement', outcoldispl_label.cget("text"),outfail_label.cget("text")))
button.place(relx=.67, rely=.52, relwidth=.3)


#Tab3
notebookTab3 = ttk.Frame(notebook)
notebook.add(notebookTab3, text=' Further details ')

details_label=ttk.Label(notebookTab3, text='Your failure mode is:',  anchor='w' )
details_label.place(relx=0.03, rely=0.16)

detail_label=ttk.Label(notebookTab3, anchor='w' )
detail_label.place(relx=0.39, rely=0.16, relwidth=.6, relheight=.2)

button=ttk.Button(notebookTab3, text='Failure description', command=lambda: Ilustration(outfail_label.cget("text")))
button.place(relx=.25, rely=.52, relwidth=.5)


#Calculate button 
button=ttk.Button(root, text='Calculate', command=lambda: [Pred_func(diam_scale.get(),sha_scale.get(),bg_scale.get(),gaug_scale.get(),concr_scale.get(),slend_scale.get())])
button.place(relx=.76, rely=.89, relwidth=.2, relheight=text_height)


#Info button 

button=ttk.Button(root, text='\u24D8 About', command=lambda: About())
button.place(relx=.04, rely=.89, relwidth=.1, relheight=text_height)


"""Graph"""

labelframe2=ttk.LabelFrame(root, text=" Drawing ")
labelframe2.place(relx=0.5, rely=0.04, relwidth=.46, relheight=.51)

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

graph(slend_scale.get(), sha_scale.get(),gaug_scale.get(), diam_scale.get(),concr_scale.get(),bg_scale.get())




root.mainloop()


