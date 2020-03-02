# Data-Science-

## Questions

- What are the endpoints?
- What functionality should the DS team provide for the endpoints to serve their requests?
- What information will be passed vy the endpoints?  What Structure?  JSON? List?
- What information is expected back?  List of 3 or 5 recommended strains?  
- Any recommendations for form?  JSON? List?



## Very Early Vision

- User enters a number of desired effects, and perhaps rates their importance.
- endpoint calls a function
- We vectorize that input
- We look for k nearest neighbors in a space of strains (target) dimensioned by effects and perhaps weights
- we retrieve names of k nearest neighbors
- we build a response piece of data (JSON doc or list)
- we return that value to the endpoint, or call a callback
