echo "enter a number"
read n
i=2
while [ $i -lt $n ]; do
   if [ `expr $n % $i` -eq 0 ]
      then
         echo "$n is not a prime number"
         exit 0
    else 
      i=`expr $i + 1`
    fi
done
echo "$n is a prime number"             
