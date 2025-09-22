
// Ask the user to pick the source directory
dir = getDirectory("Select the source directory");

// Generate a (sorted) list of files in the selected directory
list = getFileList(dir);
Array.sort(list);

// Process all files
for(i=0; i<list.length; i++) {
	filename = dir + list[i];
	open(filename);
	setAutoThreshold("Li dark");
	setOption("BlackBackground", true);
	run("Convert to Mask");
	run("Watershed");
	run("Set Measurements...", "area display redirect=None decimal=3");
	run("Analyze Particles...", "size=75-Infinity summarize");
	run("Close All");
}
