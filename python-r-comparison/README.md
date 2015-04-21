# Python R Comparison

Notes on the differences between programming in R and Python

## Basic Building Blocks

###R - Basic command line usage

*R*

For now ignore the [1]. Its meaning will be become apparent later. 
```R
> 5 + 7
[1] 12
```
*Python*
```Python
>>> 5 + 7
12
```

### Assigning to variable.

*R*
```R
> x <- 5 + 7
> x
[1] 12
```

*Python*
```Python
>>> x = 5 + 7
>>> x
12
```
###Assignment to a vector

*R*
```R
z <- c(1.1, 9, 3.14)
```

*Python*
```Python
>>> z = [1.1, 9, 3.14]
```

### Find help on a function

*R*
```R
> ?c
```

*Python *
```Python
>>> help("list")
```
###View the contents of a Vector.

*R*
```R 
> z
[1] 1.10 9.00 3.14
```
*Python*
```Python
>>> z
[1.1, 9, 3.14]
```
### Make a new vector that contains z, 555, then z again 
*R*
```R
> c(z, 555, z )
[1]   1.10   9.00   3.14 555.00   1.10   9.00   3.14
```
### z * 2 + 100
*R*
```R
> z * 2 + 100
[1] 102.20 118.00 106.28
```

### square root of z - 1 and assign it to a new variable called my_sqrt.
*R*
```R
my_sqrt <- sqrt(z-1)
> my_sqrt
[1] 0.3162278 2.8284271 1.4628739
```

### my_div that gets the value of z divided by my_sqrt.
 *R*
```R
 > my_div <- z / my_sqrt
 > my_div
[1] 3.478505 3.181981 2.146460
```

### adding c(1, 2, 3, 4) and c(0, 10)
 *R*
```R
> c(1, 2, 3, 4) +  c(0, 10)
[1]  1 12  3 14
```

###Add c(1, 2, 3, 4) + c(0, 10, 100) for an example.
 *R*
```R

> c(1, 2, 3, 4) +  c(0, 10)
[1]  1 12  3 14
```

### Type c(1, 2, 3, 4) + c(0, 10, 100) to see how R handles adding two vectors, when the shorter vector's length does not divide evenly into the longer vector's length. 
 *R*
```R
> c(1, 2, 3, 4) + c(0, 10, 100)
[1]   1  12 103   4
Warning message:
In c(1, 2, 3, 4) + c(0, 10, 100) :
  longer object length is not a multiple of shorter object length
```
