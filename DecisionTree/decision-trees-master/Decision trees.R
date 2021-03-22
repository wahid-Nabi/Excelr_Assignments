#this is a dataset ofBenign-Maligant##
attach(wbcd_new)

#table of diagosis
table(wbcd_new$diagnosis)
#recode diagonisis
wbcd_new$diagnosis<-factor(wbcd_new$diagnosis,levels=c("B","M"),
                           labels = c("Benign","Maligant"))
#table or proportions with more informativelabels
round(prop.table(table(wbcd_new$diagnosis))*100,digits = 1)
#summarize three numeric features
#summary(wbcd_new[c("radius_mean","area_mean","smoothness_mean")])
#crete normalizion function
normalize<-function(x){
  return((x-min(x))/(max(x)-min(x)))
}

#test normilization funiction-result should be identical
normalize(c(1,2,3,4,5))
normalize(c(10,20,30,40,50))
#normilaze the wbcd_new
wbcd_n<- as.data.frame(lapply(wbcd_new[2:31],normalize))
#normalize the wbcd data
wbcd_n1<-cbind(wbcd_n,wbcd_new$diagnosis)
#confirmthat normilazation worked 
summary(wbcd_n$area_mean)
# creat training and test data
wbcd_train<-wbcd_n[1:469,]
wbcd_test<-wbcd_n[470:569,]
 # create lable for training and test data
wbcd_train_labels<-wbcd_new[1:469,1]
wbcd_test_labels<-wbcd_new[470:569,1]
# training a model on the data

#load the "class" library
library(class)
i=1
#for(k=1;k<=20,k--){

wbcd_test_pred<- knn(train = wbcd_train, test = wbcd_test,cl = wbcd_train_labels, k =20)

#evaluating model performance

#load the "gmodel" library
install.packages("gmodels")
library(gmodels)
#create the cross tabulation of predicted vs actual

theans<-CrossTable(x = wbcd_test_labels, y = wbcd_test_pred,
           prop.chisq = FALSE,prop.c = FALSE, prop.r = FALSE)
