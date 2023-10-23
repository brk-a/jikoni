#!/usr/bin/env Rscript

if (!require(ggplot2)) install.packages("ggplot2", dependencies=T)
if (!require(RColorBrewer)) install.packages("RColorBrewer", dependencies=T)
library(ggplot2)
library(RColorBrewer)

pred_val <- letters[1:26]
res_val <- sample(10:100, 26)

#random error terms btwn 0.1 and 0.8 for each bar
errors <- runif(26, min=0.1, max=0.8)

df <- data.frame(pred_val, res_val, errors)

#use set3 colour pallete with 26 distinct colours
colours <- brewer.pal(12, "Set3")[1:26]

gg <- ggplot(data=df,
    aes(reorder(x=pred_val, res_val, decreasing=T), y=res_val, fill=pred_val)) +
    geom_bar(stat="identity")+
    geom_error_bar(aes(ymin=res_val-errors, ymax=res_val+errors), width=0.2) +
    scale_fill_manual(values=colours) +
    theme_minimal() +
    theme(legend_position="none") +
    coord_polar(start=0) +
    ylim(-50, 100)

highlight_inner_gridlines <- gg +
    theme(panel.grid.major=element_line(color="darkgreen", size=0.25))

print(highlight_inner_gridlines)

scale_lines <- gg +
    geom_hline(yintercept=seq(0, 100, by=20), color="gray", linetype="dashed")

division_units <- scale_lines +
    annotate("text", x=-5, y=seq(0, 100, by=20), label=c("0%", "20%", "40%", "60%", "80%", "100%"))

print(division_units)