I would like to create a python script  in which, if I run my code via the following terminal commands I want to see the shortcut information for the following options only once so that I can focus on looking at which image has been cropped and saved: 


No I want 4 options:


I need a mechanism that will allow me to delete a currently selected image.


One to delete the current image.                                         “d” key


I need a mechanism that will allow me to draw a rectangle as if I am using a paint application on windows so that I can crop the images.


One to save the current image.                                            “s” key


I need a mechanism to currently ignore the selected image.


One to skip the current image to do nothing but simply ignore.             “i” key


I need a way to exit a program gracefully.


One to do nothing and quit the program.                                   “q” key


All of these options must be done gracefully, without errors and bugs. I must have a log of all the activities that append from the existing text file.


It is practically impossible for me to crop thousands if not hundreds of images in one go. Therefore I will need to run the program again and again. The next time when I run the program it should be able to skip the images that I have ignored (some images are perfect as they don't need to be cropped), it should also skip the images that I have been skipped and ignored. I should also have another option to ignore. 


I want the terminal to print as an output for every image that is successfully saved, successfully skipped, successfully deleted. The log files should also write where in the images that it has processed. Remember there are multiple folders for different drink brands.
 
This is how my images are stored:


htootayzaaung@MSI:~/Desktop/Drinks_Classifier$ ls
 data_annotation.py         gather_data.py          print.py
 data_augmentation.py   image_cropper          'Utility commands.txt'
 data_pipeline.py           image_cropper.cpp
 draw_rectangles.py         Images
htootayzaaung@MSI:~/Desktop/Drinks_Classifier$ cd Images/
htootayzaaung@MSI:~/Desktop/Drinks_Classifier/Images$ ls
carlsberg_beer_images  heineken_beer_images  red_bull_energy_drink_images
coca_cola_images           pepsi_images              tiger_beer_images
htootayzaaung@MSI:~/Desktop/Drinks_Classifier/Images$


The images read needs to be overwritten in the same location with the images that were read without creating new folders to save cropped images.
