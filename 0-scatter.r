#!/usr/bin/env Rscript

#create a scatter plot with multiple circles

n <- 10
x <- runif(n, -2, 2)
y <- runif(n, -2, 2)
size <- runif(n, 0.1, 1)
fill <- sample(colors(), n)
border <- sample(colors(), n)
symbols(x, y, circles=size, inches=F, add=F, bg=fill, fg=border)