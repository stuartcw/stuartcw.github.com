# Python R Comparison

Notes on the differences between programming in R and Python

## Basic Building Blocks

###R
```R
> 5 + 7
[1] 12
```
###Python
```Python
>>> 5 + 7
12
```

###R
```R
> x <- 5 + 7
> x
[1] 12
```
###Python
```Python
>>> x = 5 + 7
>>> x
12
```
###R - Assignment to a vector
```R
z <- c(1.1, 9, 3.14)
```
###Python Assignment to a vector
```Python
>>> z = [1.1, 9, 3.14]
```

###R - Find help "Combine Values into a Vector or List"
```R
> ?c
```

###Python - Find help "Combine Values into a Vector or List"
```Python
>>> help("list")
```
###R - View the contents of a Vector.
```R 
> z
[1] 1.10 9.00 3.14
```

###Python -  View the contents of a Vector.
```Python
>>> z
[1.1, 9, 3.14]
```

a new vector that contains z, 555, then z again 
```R
> c(z, 555, z )
[1]   1.10   9.00   3.14 555.00   1.10   9.00   3.14
```
z * 2 + 100
```R
> z * 2 + 100
[1] 102.20 118.00 106.28
```

square root of z - 1 and assign it to a new variable called my_sqrt.

```R
my_sqrt <- sqrt(z-1)
> my_sqrt
[1] 0.3162278 2.8284271 1.4628739
```

 my_div that gets the value of z divided by my_sqrt.
 > my_div <- z / my_sqrt
 > my_div
[1] 3.478505 3.181981 2.146460


adding c(1, 2, 3, 4) and c(0, 10)
> c(1, 2, 3, 4) +  c(0, 10)
[1]  1 12  3 14

Add c(1, 2, 3, 4) + c(0, 10, 100) for an example.
> c(1, 2, 3, 4) +  c(0, 10)
[1]  1 12  3 14

Type c(1, 2, 3, 4) + c(0, 10, 100) to see how R handles adding two vectors, when the shorter vector's length does not divide evenly into the longer vector's length. 
> c(1, 2, 3, 4) + c(0, 10, 100)
[1]   1  12 103   4
Warning message:
In c(1, 2, 3, 4) + c(0, 10, 100) :
  longer object length is not a multiple of shorter object length

