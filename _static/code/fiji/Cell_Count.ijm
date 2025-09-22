setAutoThreshold("Li dark");
//run("Threshold...");
setOption("BlackBackground", true);
run("Convert to Mask");
run("Watershed");
run("Set Measurements...", "area display redirect=None decimal=3");
run("Analyze Particles...", "size=75-Infinity display summarize");
