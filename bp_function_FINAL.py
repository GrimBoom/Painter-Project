
"""
Created by Aldo Schwartz
Computational Modeling (Period 6)
December 2018

🎨 Blue Picasso 🎨

I designed this program as a way to visualize Picasso's famous 'Blue Period'
by taking yearly averages of the Red, Green, and Blue values in the pixels of 
his paintings, and plot them over time. As I was working, I had the idea of 
combining the yearly average RGB values as a single color, and then placing
those colors in a spectrum to show change over time. 

The result is a function that can turn any properly named set of images 
('y + year of composition + .jpg') into a color spectrum and a series of plots
showing change over time. 

color_spec() takes 2 arguments, start_date (the beginning of the artists career/
year of oldest image) and end_date (the artist's final work/year of newest image).

It then cycles through every year in between the start and end date, loading the
collective RGB averages into 3 2D arrays (allred,allgreen,allblue), which are later 
combined into a 3D RGB Image array. 

This image is printed in the console (along with plots of allred, allgreen, and allblue)
and saved in the working directory as 'bpspectrum.jpg'

Hope you enjoy using it!


"""

import numpy as np
import matplotlib.pyplot as plt


def color_spec(start_date, end_date):
    
    num_years = (end_date) - (start_date)
    
    # arrays to contain average RGB values from each of Picasso's paintings
    allred = np.zeros((num_years,30))
    allblue = np.zeros((num_years,30))
    allgreen = np.zeros((num_years,30))
    

    for i in range(start_date,end_date,1):
        # read in image file for each year (y + year + .jpg)
        image = plt.imread("y"+ str(i)+".jpg")
        length, width, _ = np.shape(image)
  
        # seperate R,G,B values from each pixel into arrays
        r = image[:,:,0]
        g = image[:,:,1]
        b = image[:,:,2]
  
        # sum of all R, G, B pixel values in array
        redsum = np.sum(r)
        greensum = np.sum(g)
        bluesum = np.sum(b)
  
        # average R, G, B per pixel (0-255)
        redavg = (redsum)/(length*width)
        greenavg = (greensum)/(length*width)
        blueavg = (bluesum)/(length*width)
  
        # add color averages to array of all paintings
        allred[i-start_date] = redavg
        allgreen[i-start_date] = greenavg
        allblue[i-start_date] = blueavg
    

    # combine color averages over time to make single RGB image array
    rgbArray = np.zeros((num_years,30,3), 'uint8')
    rgbArray[...,0] = allred
    rgbArray[...,1] = allgreen
    rgbArray[...,2] = allblue
   
    # print and save average color spectrum of Picasso's career
    plt.axis('off')
    plt.imshow(rgbArray)
    plt.imsave('bpspectrum.jpg',rgbArray)

    # create x axis for graphs
    dates = np.arange(start_date,end_date,1)

    # create subplots for R,G, B separately
    # label blue period
    plt.figure()

    # Make subplots displaying average R,G,B values over time
    ax1 = plt.subplot(3,1,1); plt.plot(dates, allred, color = 'r')
    ax2 = plt.subplot(3,1,2); plt.plot(dates, allgreen, color = 'g')
    ax3 = plt.subplot(3,1,3); plt.plot(dates, allblue, color = 'b')

    # Label subplots
    ax1.set_title('Average Red Value', size = 14, weight = 'bold')
    ax2.set_title('Average Green Value', size = 14, weight = 'bold')
    ax3.set_title('Average Blue Value', size = 14, weight = 'bold')

    # label x axes
    ax1.set_xlabel("Date [years]")
    ax2.set_xlabel("Date [years]")
    ax3.set_xlabel("Date [years]")

    # label y axes
    ax1.set_ylabel("R [0-255]")
    ax2.set_ylabel("G [0-255]")
    ax3.set_ylabel("B [0-255]")

    # put more space between graphs
    plt.tight_layout()


color_spec(1889, 1973)


