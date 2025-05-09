echo "enter the year for checking leap year or not: "
read n
a=`expr $n % 400`
b=`expr $n % 100`
c=`expr $n % 4`
if [ $a -eq 0 -o $b -ne 0 -a $c -eq 0 ]
  then 
    echo $n" is leap year"
  else
    echo $n" is not leap year" 
  fi   
