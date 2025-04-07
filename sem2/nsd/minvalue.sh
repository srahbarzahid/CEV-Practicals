read -p "enter the 1st number:" a
read -p "enter the 2nd number:" b
read -p "enter the 3rd number:" c
read -p "enter the 4th number:" d
if [ $a -lt $b ] && [ $a -lt $c ] && [ $a -lt $d ];
   then 
     echo "$a is minimum value"
   elif [ $b -lt $a ] && [ $b -lt $c ] && [ $b -lt $d ]
     then
       echo "$b is minimum value" 
   elif [ $c -lt $a -a $c -lt $b -a $c -lt $d ]
     then 
       echo "$c is minimum"
   else 
       echo "$d is minimum"
fi
       
                
