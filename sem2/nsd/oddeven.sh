echo "enter a number"
read n
if [ `expr $n % 2` -eq 0 ];
  then 
    echo "$n is even number"
  else
    echo "$n is odd number"
fi
      
