args<-commandArgs(trailingOnly=T)
cat("Number of arguments:", length(args), "\n")
for ( i in args) {
	cat(i,"\n")
}
