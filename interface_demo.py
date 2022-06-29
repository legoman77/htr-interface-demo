import sys
import os
import PySimpleGUI as sg
import subprocess


#GUI creation

sg.theme('Dark Blue 15')

list_filetype = [".png",".tiff",".jpg"]
list_model = ["English Cursive Handwritten"]


layout =  [[sg.Text('Path to image files:  ',tooltip="Select the folder on your computer containing the images to be transcribed."),sg.InputText(),sg.FolderBrowse()],
           [sg.Text('Select file format:     ',tooltip="Indicate what type of image files will be passed to the model. All files must be of the same type."),sg.Combo(list_filetype, size=(10,5))],
           [sg.Text('Select model:          ',tooltip="Select the most appropriate recognition model based on the language and writing style of your text."),sg.Combo(list_model, size=(25,4))],
           
           
           [sg.Button('Start')]]

window = sg.Window('Transcription Settings',layout)


while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Start':
        break

if values[1] == ".png":
  path = values[0] + "/*.png"
elif values[1] == ".tiff":
  path = values[0] + "/*.tiff"
elif values[1] == ".jpg":
  path = values[0] + "/*.jpg"

if values[2] == "English Cursive Handwritten":
  model = "model_eng_cursive.mlmodel"

process = "ketos test -m " + model + " " + path
lol = "cd data"

trueprocess = process.split()


# print(process)
subprocess.run(trueprocess, shell=True)
    