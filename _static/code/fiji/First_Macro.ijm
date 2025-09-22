setAutoThreshold("Default dark no-reset");
//run("Threshold...");
setOption("BlackBackground", true);
run("Convert to Mask");
run("Set Measurements...", "area mean min display redirect=None decimal=3");
run("Analyze Particles...", "display");
