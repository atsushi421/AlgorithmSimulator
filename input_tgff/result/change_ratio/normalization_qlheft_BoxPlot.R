## read data file
d1 <- read.table("./QLHEFT/1.5.txt")
d1_nume <- as.numeric(d1$V1)
d1_median <- median(d1_nume)
d1 <- d1 / d1_median  # QLHEFT_1.5_median
d2 <- read.table("./QLHEFT/3.txt")
d2_nume <- as.numeric(d2$V1)
d2_median <- median(d2_nume)
d2 <- d2 / d2_median  # QLHEFT_3_median
d3 <- read.table("./QLHEFT/6.txt")
d3_nume <- as.numeric(d3$V1)
d3_median <- median(d3_nume)
d3 <- d3 / d3_median  # QLHEFT_6_median
d4 <- read.table("./QLHEFT/12.txt")
d4_nume <- as.numeric(d4$V1)
d4_median <- median(d4_nume)
d4 <- d4 / d4_median  # QLHEFT_12_median
d5 <- read.table("./QLHEFT/24.txt")
d5_nume <- as.numeric(d5$V1)
d5_median <- median(d5_nume)
d5 <- d5 / d5_median  # QLHEFT_24_median
qlheft <- cbind(d1, d2, d3, d4, d5) # bind data

## read data file
d1 <- read.table("./Propose/1.5.txt")
d1 <- d1 / d1_median  # QLHEFT_1.5_median
d2 <- read.table("./Propose/3.txt")
d2 <- d2 / d2_median  # QLHEFT_3_median
d3 <- read.table("./Propose/6.txt")
d3 <- d3 / d3_median  # QLHEFT_6_median
d4 <- read.table("./Propose/12.txt")
d4 <- d4 / d4_median  # QLHEFT_12_median
d5 <- read.table("./Propose/24.txt")
d5 <- d5 / d5_median  # QLHEFT_24_median
propose <- cbind(d1, d2, d3, d4, d5) # bind data

## read data file
d1 <- read.table("./HEFT/1.5.txt")
d1 <- d1 / d1_median  # QLHEFT_1.5_median
d2 <- read.table("./HEFT/3.txt")
d2 <- d2 / d2_median  # QLHEFT_3_median
d3 <- read.table("./HEFT/6.txt")
d3 <- d3 / d3_median  # QLHEFT_6_median
d4 <- read.table("./HEFT/12.txt")
d4 <- d4 / d4_median  # QLHEFT_12_median
d5 <- read.table("./HEFT/24.txt")
d5 <- d5 / d5_median  # QLHEFT_24_median
heft <- cbind(d1, d2, d3, d4, d5) # bind data

all_data <- list(propose, qlheft, heft)         # merge two data (data.frame) into a list

## define x-axis scale name
xaxis_scale <- c("1.5", "3.0", "6.0", "12.0", "24.0")
box_cols <- c("pink", "lightcyan", "palegreen1")                # box colors
## border_cols <- c("red", "blue")                   # box-line colrs
border_cols <- c("red", "blue", "palegreen4")                   # box-line colors

## graphic function
comparison_BoxPlot <- function(all_data) {
    ## set parameters for graph
    par(
        xaxs="i",                      # x-axis data span has no margin
        mar = c(5,6,2,2)                #  margin
    )
    ## prepare graph feild
    plot(
        0, 0, type = "n",
        xlab = "CCR", ylab = "Makespan", # labels
        cex.lab = 1.8,                     # label font size
        font.lab = 1,                      # label font
        xlim = range(0:(ncol(propose) * 3)), # define large x-axis
        ylim = c(0.4, max(range(propose), range(qlheft), range(heft))), # y-axis data span
        font.axis = 1,                                # axis font
        xaxt = "n"                                    # no x-axis
    )
    ## draw vertical line
    abline(
        v = c(3, 6, 9, 12, 15, 18, 21), # position
        lwd = 1,                       # line width
        col = 8,                    # line color
        lty = 3                     # line style
    )
    ## draw boxplot
    for (i in 1:3){
        boxplot(
            all_data[[i]],
            at = c(1:ncol(propose)) * 3 + i - 3.5, # position of drawing boxplot
            border = border_cols[i],                 # ボックス枠線の色
            col = box_cols[i],                       # colors
            xaxt = "n",                          # no x-axis scale
            range = 0,                           # no plot outliers 
            add = TRUE)
    }
    ## legend
    legend(
        0.1, 0.65,                      # position
        legend = c("Propose", "QL-HEFT", "HEFT"),   # labels
        cex = 1.3,                      # labels font size
        pt.cex = 3,                     # marker size
        pch = 22,                       # kinds of marker
        col = border_cols,              # box-line colors
        pt.bg = box_cols,               # box colors
        lty = 0,                               
        lwd = 2,                        # box-line width
        bg = "white"                    # background color
    )
    ## x-axis scale
    axis(
        1,                                    
        at = 1:length(xaxis_scale) * 3 - 1.5, # position of scale
        labels = xaxis_scale,                 # set scale name
        cex.axis=0.73,                        # axis font size
        tick = TRUE                           
    )
}

## output file as eps
postscript("normalization_qlheft_BoxPlot.eps", horizontal = F, onefile = FALSE, paper = "special", width = 8, height = 6)
comparison_BoxPlot(all_data)
dev.off()

## output file as png
png("normalization_qlheft_BoxPlot.png", width = 600, height =400)
comparison_BoxPlot(all_data)
dev.off()