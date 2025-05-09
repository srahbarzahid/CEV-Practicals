file=$1
start=$2
end=$3
if [ ! -f "$file" ];then
	echo "file not found"
fi
line=0
while IFS= read -r line1; do
	line=$((line + 1))
	if [ "$line" -ge "$start" ] && [ "$line" -le "$end" ];then
		echo "$line1"
	fi
done < "$file"	
