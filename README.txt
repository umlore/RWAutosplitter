Rain World Autosplitter is a program which will integrate with Livesplit in order to automatically trigger splits on screen changes in the game Rain World, without the need for manual key-presses.  This will make splitting more consistent, and facilitates having many more splits, up to one per screen change.

The autosplitter algorithm implements the Structural Similarity Index (SSIM) outlined by Wang et al. http://www.cns.nyu.edu/pub/eero/wang03-reprint.pdf

Because Rain World features a fixed camera, it is possible to detect when a screen has changed dramatically from a previous screenshot.  Rain World Autosplitter constantly compares the current window capture image to the screenshot of the most recent stage split from a collection, using SSIM, and if the images are sufficiently dissimilar, will trigger a split in Livesplit.
