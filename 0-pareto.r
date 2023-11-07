#!/usr/bin/env Rscript

#create a data frame with the product and count

if (!require(gcc)) install.packages("gcc", dependencies=T)
library(gcc)

df <- data.frame(
    product=c("Office desks", "Chairs", "Filing cabinets", "Bookcases"),
    count =c(100, 80, 70, 60)
)

pareto.chart(
    df$count,
    main="Pareto chart of product sales",
    xlab="Product",
    ylab="Count",
    col=heat.colors(length(df$count)),
    lwd=2
)