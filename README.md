# maxmu
Given a set of points (in lat,lng), find the largest area triangle.  From the set of points within that triangle (including 2 of the three outer triangle vertices), find the second largest triangle.  Repeat until there are no points within the innermost triangle.
In the degenerate case, this will yield a standard layered field, but in the typical case the spine will be non-continuous.  Build the field inside out, creating the triangle first and then linking to the third portal of the inner triangle.
[EDIT: This summary is still largely correct, but during development I found maintaing different sets of input points to be bothersome and so changed it to use a set of all points with the user supplying the outer bounds of the area of interest.]
