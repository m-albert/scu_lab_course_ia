// Macro to merge DAPI, FITC and DIC images into a composite RGB image
// The user will be prompted to select each of the respective images
// to be merged.

// Prompt the user to select the DAPI image
waitForUser("Select DAPI image");

// Store the name of the selected image into the nameDAPI variable
nameDAPI = getTitle();

// Prompt the user to select the FITC image
waitForUser("Select FITC image");

// Store the name of the selected image into the nameFITC variable
nameFITC = getTitle();

// Prompt the user to select the DIC image
waitForUser("Select DIC image");

// Store the name of the selected image into the nameDIC variable
nameDIC = getTitle();

// Merge the DAPI, FITC and DIC images into the Blue, Green and Grey channels
run("Merge Channels...", "c2=["+nameFITC+"] c3=["+nameDAPI+"] c4=["+nameDIC+"] ignore");

