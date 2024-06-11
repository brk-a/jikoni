#!/usr/bin/env Rscript

##### idea is to extract text between two characters
##### the chars are `-` and `no` in this example

#assume file is `tende.csv`
df <- read_csv("tende", header=T, sep=",")
head(df)

########## using `stringr` #####################

#install `stringr` if not already installed
if (!library(stringr)) {
   install.packages("stringr", dependencies=T)
}
library(stringr)

#we want whatever is between `-` and `no`
df$NewColumn <- str_match(df$ColumnNameToExtract, "-\\s*(.*?)\\s*no")[,2]
df

########## using `gsub` from base R #####################

#we want whatever is between `-` and `no`
df$NewColumn <- gsub(".*- (.+) no.*", "\\1", df$ColumnNameToExtract)
df