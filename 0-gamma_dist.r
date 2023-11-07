#!/usr/bin/env Rscript

#fit a gamma dist to a data set

if (!require(fitdistrplus)) install.packages("fitdistrplus", dependencies=T)
if (!require(TidyDensity)) install.packages("TidyDensity", dependencies=T)
library(fitdistrplus)
library(TidyDensity)

data <- tidy_gamma()$y

fit <- fitdist(data, distr="gamma", method="mle")
