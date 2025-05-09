read -p "enter the 1st no: " a
read -p "enter 2nd number :" b
read -p "enter 3rd number: " c
read -p "enter 4th number: " d

if [ $a -lt $b ] && [ $a -lt $c ] && [ $a -lt $d ]
then
 	echo "$a is smallest no"
elif [ $b -lt $a ] && [ $b -lt $c ] && [ $b -lt $d ]	
then
	echo "$b is minimum"
elif [ $c -lt $a ] && [ $c -lt $b ] && [ $c -lt $d ]
then
	echo "$c minimum"
else 
	echo "$d is minimum"
fi	
