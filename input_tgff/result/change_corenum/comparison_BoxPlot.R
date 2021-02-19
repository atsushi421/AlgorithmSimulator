## read data file
d1 <- read.table("./Propose/2.txt")
d2 <- read.table("./Propose/3.txt")
d3 <- read.table("./Propose/4.txt")
d4 <- read.table("./Propose/5.txt")
propose <- cbind(d1, d2, d3, d4) # bind data

## read data file
d1 <- read.table("./QLHEFT/2.txt")
d2 <- read.table("./QLHEFT/3.txt")
d3 <- read.table("./QLHEFT/4.txt")
d4 <- read.table("./QLHEFT/5.txt")
qlheft <- cbind(d1, d2, d3, d4) # bind data

## read data file
d1 <- read.table("./HEFT/2.txt")
d2 <- read.table("./HEFT/3.txt")
d3 <- read.table("./HEFT/4.txt")
d4 <- read.table("./HEFT/5.txt")
heft <- cbind(d1, d2, d3, d4) # bind data

all_data <- list(propose, qlheft, heft)         # merge two data (data.frame) into a list

## define x-axis scale name
xaxis_scale <- c("2", "3", "4", "5")
yaxis_scale <- c("0", "10,000", "20,000", "30,000", "40,000")
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
        xlab = "Number of cores in one CC", ylab = "Makespan", # labels
        cex.lab = 1.8,                     # label font size
        font.lab = 1,                      # label font
        xlim = range(0:(ncol(propose) * 3)), # define large x-axis
        ylim = c(0, max(range(propose), range(qlheft), range(heft))), # y-axis data span
        font.axis = 1,                                # axis font
        xaxt = "n",                                    # no x-axis
        yaxt = "n"
    )
    ## draw vertical line
    abline(
        v = c(3, 6, 9, 12, 15, 18), # position
        lwd = 1,                       # line width
        col = 8,                    # line color
        lty = 3                     # line style
    )
    ## draw boxplot
    for (i in 1:3){
        boxplot(
            all_data[[i]],
            at = c(1:ncol(propose)) * 3 + i - 3.5, # position of drawing boxplot
            border   = border_cols[i],                 # ボックス枠線の色
            col = box_cols[i],                       # colors
            xaxt = "n",                          # no x-axis scale
            yaxt = "n",
            range = 0,                           # no plot outliers 
            add = TRUE)
    }
    ## legend
    legend(
        0.1, 15000,                      # position
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
        labels = xaxis_scale,                # set scale name
        cex.axis=0.73,                        # axis font size
        tick = TRUE                      
    )
    axis(
        2,
        at = seq(0, 40000, by = 10000),
        labels = yaxis_scale,
        tick = TRUE
    )
}

## output file as eps
postscript("comparison_BoxPlot.eps", horizontal = F, onefile = FALSE, paper = "special", width = 8, height = 6)
comparison_BoxPlot(all_data)
dev.off()

## output file as png
png("comparison_BoxPlot.png", width = 600, height =400)
comparison_BoxPlot(all_data)
dev.off()
