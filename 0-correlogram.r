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
ds %>%
    select(male1, male2, male3, female1, female2, female3, pathogen1, pathogen2, pathogen3, pathogen4, pathogen5, pathogen6, pathogen7) %>%
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
