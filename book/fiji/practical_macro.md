# P1.3: Automation with Fiji macros

## Preparation

Download the following three image files to your computer and place them in a folder:
- Image 1
- Image 2
- Image 3

## Questions
1. Open one of the images in Fiji.
1. Open the macro recorder (Plugins > Macros > Record...).
1. Apply a combination of filters and thresholding to segment the objects in the image.
1. When you are satisfied with the result, open the macro editor (Plugins > Macros > Edit...) and copy the relevant lines of code from the recorder window to the editor window.
1. Apply the macro to the other two images. Do you get a good segmentation result? If not, try to improve your macro.
1. Use the following code snippet to process all images in a folder. Adjust the macro to save the results to a new folder.

```javascript
input = getDirectory("Choose Input Directory ");
output = getDirectory("Choose Output Directory ");
list = getFileList(input);
for (i=0; i<list.length; i++) {
    if (endsWith(list[i], ".tif")) {
        open(input + list[i]);

        // your code for image segmentation goes here
        // ...

        saveAs("Tiff", output + list[i]);
        close();
    }
}
```