#!/usr/bin/env Rscript

#call `tidyverse`
if (!require(tidyverse)) install.packages("tidyverse", dependencies=T)
library(tidyverse)

#load data
ds <- read.csv("~/Desktop/data_2022.csv", sep=',', header=T)

#see if data loaded
head(ds)
summary(ds)

#filter required data and remove NA
ds <- ds %>%
    select(ds$male1, ds$male2, ds$male3, ds$female1, ds$female2, ds$female3, ds$pathogen1, ds$pathogen2, ds$pathogen3, ds$pathogen4, ds$pathogen5, ds$pathogen6, ds$pathogen7) %>%
    na.omit() %>%
    summarise()

#prepare numerical variables and factor variable 
data <- ds[,1:6] # Numerical variables
groups <- ds[,7:] #Factor variable 

pairs(data,                     # Data frame of variables
      labels = colnames(data),  # Variable names
      pch = 22,                 # Pch symbol
      bg = rainbow()[groups],  # Background colour of the symbol (pch 21 to 25)
      col = rainbow()[groups], # Border colour of the symbol
      main = "Pathogens",    # Title of the plot
      row1attop = TRUE,         # If FALSE, changes the direction of the diagonal
      gap = 1,                  # Distance between subplots
      cex.labels = NULL,        # Size of the diagonal text
      font.labels = 1)          # Font style of the diagonal text
