echo "enter the number"
read n
fact=1
while [ $n -gt 0 ]
 do 
  fact=$(($fact * $n))
  n=`expr $n - 1`
  done
 echo "factorial:"$fact
  
    
