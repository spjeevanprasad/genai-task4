#  Image to Image Translation (Pix2Pix Style)

## Description
This project is my submission for the Generative AI internship task.

In this task, I performed simple image-to-image translation using Python PIL library.  
The program takes an input image, converts it into grayscale, and enhances the details using filters.

This is a basic simulation of the Pix2Pix concept (not a deep learning GAN model).

## Files
- genai-task4.py : Python code for image processing
- input.png : Input image
- output.png : Processed output image

## How to Run

### 1. Install required library
pip install pillow

### 2. Run the program
python main.py

### 3. Output
The processed image will be saved as output.png

## Working
- Load input image
- Convert image to grayscale
- Apply detail enhancement filter
- Save the final output image

## Example
Input: Color image  
Output: Grayscale image with enhanced details

## Note
This is not a real Pix2Pix GAN model.  
It is a simple image processing simulation using PIL.

## Author
Jeevan
